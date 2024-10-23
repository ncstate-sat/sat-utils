import logging
import os
from unittest.mock import MagicMock
import time

from elasticsearch import Elasticsearch, BadRequestError
from elasticsearch.helpers import bulk


class SingletonLoggerMixin(object):
    _instance = None
    client_mock = None

    def __new__(cls, *args, **kwargs):

        # Only call this setup block the first time a SATLoggerSingleton is instantiated
        # Prevents multiple setup function calls
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
            setup_sat_logging_with_defaults()

        return cls._instance


class SATLogger(SingletonLoggerMixin):
    def __init__(self, name: str = __name__, level: int = logging.INFO) -> None:
        self.logger = logging.getLogger(name)

    def add_handlers(self, handlers: list[(logging.Handler, logging.Formatter)]) -> None:
        """
        Add additional handlers to the logger.
        Handlers should be a list of tuples with a logging.Handler and an
        optional logging.Formatter.
        """

        self.logger.warning('Adding handlers to this instance of the logger only, will not persist throughout project. Update logging config to persist changes.')

        for tup in handlers:
            handler, formatter = tup
            if formatter:
                handler.setFormatter(formatter)
            else:
                handler.setFormatter(self.formatter)
            self.logger.addHandler(handler)

    def debug(self, msg: str, *args, **kwargs) -> None:
        self.logger.debug(msg, *args, **kwargs)

    def info(self, msg: str, *args, **kwargs) -> None:
        self.logger.info(msg, *args, **kwargs)

    def warning(self, msg: str, *args, **kwargs) -> None:
        self.logger.warning(msg, *args, **kwargs)

    def error(self, msg: str, *args, **kwargs) -> None:
        self.logger.error(msg, *args, **kwargs)

    def critical(self, msg: str, *args, **kwargs) -> None:
        self.logger.critical(msg, *args, **kwargs)


class ElasticModuleFilter(logging.Filter):

    def filter(self, record):
        return 'elastic' not in record.name

def setup_sat_logging_with_defaults():


    # Elastic loging feature flag defaults to false, don't want to blow up local development if no environment variables are set
    enable_elastic_string = os.getenv('ELASTIC_ENABLE_LOGGING', '')
    if enable_elastic_string.lower() == 'true':
        enable_elastic_logging = True
    else:
        enable_elastic_logging = False

    if enable_elastic_logging:
        elastic_url = os.environ['ELASTIC_URL']
        elastic_username = os.environ['ELASTIC_USERNAME']
        elastic_password = os.environ['ELASTIC_PASSWORD']
        elastic_index = os.environ['ELASTIC_INDEX']
        app_name = os.environ['APP_NAME']
        elastic_client = get_elasticsearch_client(elastic_url, elastic_username, elastic_password)
    else:
        app_name = os.getenv('APP_NAME')  # If logging without elastic enabled, APP_NAME is optional
        elastic_client = None
        elastic_index = None


    log_level_string = os.getenv('LOGLEVEL', 'INFO')
    log_level = getattr(logging, log_level_string.upper())


    setup_sat_logging(elastic_client, elastic_index, app_name, enable_elastic_logging, log_level)

def setup_sat_logging(client: Elasticsearch, index_name: str, app_name: str, enable_elastic_logging, loglevel: int = logging.INFO, batch_size: int=100, batch_time: float=2.):

    log_handlers = [logging.StreamHandler(), logging.StreamHandler(), logging.StreamHandler()]

    if os.getenv('DEBUG'):
        loglevel = logging.DEBUG

    if enable_elastic_logging:
        elastic_handler = ElasticClientHandler(client, index_name=index_name, document_labels={"app": app_name}, level=loglevel, batch_size=batch_size, batch_time=batch_time)
        elastic_handler.addFilter(ElasticModuleFilter())
        log_handlers.append(elastic_handler)

    logging.basicConfig(
        level=loglevel,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=log_handlers
    )


def get_elasticsearch_client(elastic_url: str, username: str, password: str) -> Elasticsearch:
    return Elasticsearch(
        elastic_url,
        basic_auth=(username, password),
        verify_certs=False
    )

class ElasticClientHandler(logging.Handler):

    def __init__(self, client: Elasticsearch, index_name: str, document_labels: dict = None, level=logging.NOTSET, batch_size: int=10, batch_time: float=5.):
        super().__init__(level)
        self.client = client
        self.index_name = index_name
        self.document_labels = document_labels
        self.batch_size = batch_size
        self.batch_time = batch_time
        self._queue = []
        self._batch_start_time = time.time()

        self.addFilter(ElasticModuleFilter())  # Need a filter here to prevent the elasticsearch module from recursively sending logging calls

        # Create index if none exists
        try:
            self.client.indices.create(index=index_name)
        except BadRequestError:
            pass  # Index already exists so one doesn't have to be created

    def emit(self, record):
        formatted_data = self.format(record)

        # Explicitly handle messages where a CID field is not provided
        try:
            message_cid = record.cid
        except AttributeError:
            message_cid = None

        document = {"log_message": formatted_data, "cid": message_cid}

        if self.document_labels:
            document.update(self.document_labels)

        self._queue.append(document)

        if len(self._queue) >= self.batch_size:
            self.flush()
        elif time.time() - self.batch_time >= self._batch_start_time:
            self.flush()

    def flush(self):
        upload_result = bulk(self.client, self._queue)
        self._queue = []
        self._batch_start_time = time.time()
        super().flush()

    def close(self):
        self.flush()
        super().close()
