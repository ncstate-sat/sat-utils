import logging
import os

from sat.logs import setup_sat_logging, get_elasticsearch_client
from logger_examples.get_logger.helpers.some_module_1 import some_function



# This example uses a function that takes the elastic client and parameters as arguments
# We could also ues a `setup_sat_logging` function that defaults to pulling from specific
# env variables automatically so that the application entrypoints aren't as complex
# The benefit to this is that testing is much easier, since `setup_sat_logging` can be called with a mock client
elastic_client = get_elasticsearch_client(os.getenv('ELASTIC_URL'), username=os.getenv('ELASTIC_USERNAME'), password=os.getenv('ELASTIC_PASSWORD'))
setup_sat_logging(client=elastic_client, index_name='test', app_name='lol')

logger = logging.getLogger(__name__)


logger.info('hello')

a = some_function()

logger.info('Finished with the stuff, shutting down')
