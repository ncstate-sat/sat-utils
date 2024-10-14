import logging

from sat.logs import SATLoggerSingleton
from logger_examples.singleton.singleton_module import singleton_example_function

logger = SATLoggerSingleton(__name__)


logger.info('hello')

a = singleton_example_function()

logger.info('Finished with the stuff, shutting down')
