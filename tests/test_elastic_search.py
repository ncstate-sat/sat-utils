from unittest.mock import MagicMock
import datetime
import logging

import pytest

from sat.logs import ElasticClientHandler, SATLogger, ActualSatLogger, setup_sat_logging


@pytest.fixture
def mock_elastic_client():
    mock_client = MagicMock()
    return mock_client

@pytest.fixture
def logger():
    logger = ActualSatLogger(__name__)
    return logger

def mock_time(self, record, datefmt=None):
    return datetime.datetime(2000,1,2,3,4,5,678).strftime('%Y-%m-%d %H:%M:%S,%f')[:-3]


def test_setup_log(mock_elastic_client):
    setup_sat_logging(client=mock_elastic_client, index_name='test', app_name='test')
    test_logger = logging.getLogger(__name__)
    test_logger.info('lol', extra={'cid': 'test-cid'})

    expected_log_document = {
        "log_message": "2000-01-02 03:04:05,000 - tests.test_elastic_search - INFO - test message",
        "cid": "test_cid"
    }

    mock_elastic_client.index.assert_called_with(index='test-index', document=expected_log_document)


def test_log_sent(mock_elastic_client, logger):

    elastic_handler = ElasticClientHandler(mock_elastic_client, 'test-index', None)
    logger.add_handlers([(elastic_handler, None)])
    logger.formatter.formatTime = mock_time

    logger.info('test message')

def test_extra_handling(mock_elastic_client, logger):

    elastic_handler = ElasticClientHandler(mock_elastic_client, 'test-index', None)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    formatter.formatTime = mock_time
    elastic_handler.setFormatter(formatter)

    logger.addHandler(elastic_handler)
    logger.info('test message', extra={'cid': 'test_cid'})

    expected_log_document = {
        "log_message": "2000-01-02 03:04:05,000 - tests.test_elastic_search - INFO - test message",
        "cid": "test_cid"
    }

    mock_elastic_client.index.assert_called_with(index='test-index', document=expected_log_document)
