import logging
import os

import requests
from elasticsearch import Elasticsearch


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

    def debug(self, msg: str) -> None:
        self.logger.debug(msg)

    def info(self, msg: str) -> None:
        self.logger.info(msg)

    def warning(self, msg: str) -> None:
        self.logger.warning(msg)

    def error(self, msg: str) -> None:
        self.logger.error(msg)

    def critical(self, msg: str) -> None:
        self.logger.critical(msg)

def get_elasticsearch_client(elastic_url: str, username: str, password: str) -> Elasticsearch:
    return Elasticsearch(
        elastic_url,
        basic_auth=(username, password)
    )


class ElasticClientHandler(logging.Handler):

    def __init__(self, client: Elasticsearch, index_name: str, document_labels: dict = None, level=logging.NOTSET):
        super().__init__(level)
        self.client = client
        self.index_name = index_name
        self.document_labels = document_labels

    def emit(self, record):
        formatted_data = self.format(record)

        document = {"log_message": formatted_data, "cid": record.extra.get('cid')}
        if self.document_lables:
            document.update(self.document_labels)

        self.client.index(index=self.index_name, document=document)
