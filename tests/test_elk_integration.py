from unittest.mock import MagicMock, patch
import datetime
import logging

import pytest

from sat.logs import ElasticClientHandler


@pytest.fixture
def log_stuff(request):
    mock_client = MagicMock()
    elastic_handler = ElasticClientHandler(client=mock_client, index_name='test', document_labels={'app': 'test'}, level=logging.INFO)
    elastic_handler.setLevel(logging.INFO)
    test_formatter = logging.Formatter('%(message)s')
    elastic_handler.setFormatter(test_formatter)
    logger = logging.getLogger(request.node.name)
    logger.setLevel(logging.INFO)
    logger.addHandler(elastic_handler)

    return logger, mock_client


def test_without_fixture():
    mock_client = MagicMock()
    elastic_handler = ElasticClientHandler(client=mock_client, index_name='test', document_labels={'app': 'test'},
                                           level=logging.INFO)
    elastic_handler.setLevel(logging.INFO)
    test_formatter = logging.Formatter('%(message)s')
    elastic_handler.setFormatter(test_formatter)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(elastic_handler)
    logger.info('test 1 message 1')
    logger.info('test 1 message 2')


def test_log_sent(log_stuff):
    """Just assert that the bulk upload method is called if a single message is sent"""
    test_logger, mock_elastic_client = log_stuff
    test_logger.info('test 2 message 1', extra={'cid': 'test-cid'})
    mock_elastic_client.index.assert_called()


def test_extra_handling(log_stuff):

    logger, mock_elastic_client = log_stuff

    logger.info('test 3 message 1', extra={'cid': 'test 3 cid 1'})

    expected_log_document = {
        'app': 'test',
        "log_message": "test 3 message 1",
        "cid": "test 3 cid 1"
    }
    mock_elastic_client.index.assert_called_with(index='test', document=expected_log_document)
