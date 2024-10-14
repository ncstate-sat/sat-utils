import logging
import os
from unittest.mock import MagicMock

import requests
from elasticsearch import Elasticsearch, BadRequestError


class SingletonLoggerMixin(object):
    _instance = None
    client_mock = None

    def __new__(cls, *args, **kwargs):

        # Only call this setup block the first time a SATLoggerSingleton is instantiated
        # Prevents multiple setup function calls
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
            cls.client_mock = MagicMock()
            setup_sat_logging(client=cls.client_mock, index_name='test', app_name='test')

        return cls._instance


class SATLoggerSingleton(SingletonLoggerMixin):
    def __init__(self, name: str = __name__, level: int = logging.INFO) -> None:
        self.logger = logging.getLogger(name)

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


class SATLoggerStripped:

    def __init__(self, name: str = __name__,) -> None:
        self.logger = logging.getLogger(name)


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

    elastic_url = os.environ['ELASTIC_URL']
    elastic_username = os.environ['ELASTIC_USERNAME']
    elastic_password = os.environ['ELASTIC_PASSWORD']
    elastic_index = os.environ['ELASTIC_INDEX']

    app_name = os.environ['APP_NAME']

    elastic_client = get_elasticsearch_client(elastic_url, elastic_username, elastic_password)

    setup_sat_logging(elastic_client, elastic_index, app_name)

def setup_sat_logging(client: Elasticsearch, index_name: str, app_name: str, loglevel: int = logging.INFO):

    if os.getenv('DEBUG'):
        loglevel = logging.DEBUG

    elastic_handler = ElasticClientHandler(client, index_name=index_name, document_labels={"app": app_name}, level=loglevel)
    elastic_handler.addFilter(ElasticModuleFilter())

    logging.basicConfig(
        level=loglevel,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(),
            elastic_handler
        ]
    )

class SATLogger:
    def __init__(self, name: str = __name__, level: int = logging.INFO) -> None:
        self.logger = logging.getLogger(name)
        if os.getenv("DEBUG"):
            self.logger.setLevel(logging.DEBUG)
        else:
            self.logger.setLevel(level)
        self.formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        self.handler = logging.StreamHandler()
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)

    def add_handlers(self, handlers: list[(logging.Handler, logging.Formatter)]) -> None:
        """
        Add additional handlers to the logger.
        Handlers should be a list of tuples with a logging.Handler and an
        optional logging.Formatter.
        """
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

def get_elasticsearch_client(elastic_url: str, username: str, password: str) -> Elasticsearch:
    return Elasticsearch(
        elastic_url,
        basic_auth=(username, password),
        verify_certs=False
    )


class ElasticClientHandler(logging.Handler):

    def __init__(self, client: Elasticsearch, index_name: str, document_labels: dict = None, level=logging.NOTSET):
        super().__init__(level)
        self.client = client
        self.index_name = index_name
        self.document_labels = document_labels

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

        self.client.index(index=self.index_name, document=document)
