import logging
import os
import pprint
from unittest.mock import MagicMock

from sat.logs import setup_sat_logging
from logger_examples.get_logger.helpers.some_module_1 import some_function



elastic_client = MagicMock()

setup_sat_logging(client=elastic_client, index_name='test', app_name='lol')

logger = logging.getLogger(__name__)


logger.info('hello')

a = some_function()

logger.info('Finished with the stuff, shutting down')