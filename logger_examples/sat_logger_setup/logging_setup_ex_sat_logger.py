import logging

from sat.logs import setup_sat_logging_with_defaults, SATLoggerStripped
from sat.some_module_1 import some_function


setup_sat_logging_with_defaults()  # Has to be called once in the project main file

# Just use logging.getLogger(__name__) wherever to get an appropriate logger
# Any logger configured will use the correct handlers that were assigned in the setup function
logger = SATLoggerStripped(__name__)



logger.info('hello')

a = some_function()

logger.info('Finished with the stuff, shutting down')
