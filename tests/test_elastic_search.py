from unittest.mock import MagicMock

import pytest

from sat.logs import ElasticClientHandler, SATLogger


@pytest.fixture
def mock_elastic_client():
    mock_client = MagicMock()
    return mock_client

@pytest.fixture
def logger():
    logger = SATLogger(__name__)
    return logger

def test_log_sent(mock_elastic_client, logger):

    elastic_handler = ElasticClientHandler(mock_elastic_client, 'test-index', None)
    logger.add_handlers([elastic_handler])
    logger.info('test message')

def test_extra_handling(mock_elastic_client, logger):

    elastic_handler = ElasticClientHandler(mock_elastic_client, 'test-index', None)
    logger.add_handlers([elastic_handler])
    logger.info('test message', extra={'cid': 'test_cid'})
