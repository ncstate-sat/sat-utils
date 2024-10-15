from sat.logs import SATLogger

from logger_examples.old_school_logger.b_module import b_function

logger = SATLogger(__name__)

def a_function():
    logger.info('A message')
    b_function()

    return