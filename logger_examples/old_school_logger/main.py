from sat.logs import SATLogger
from logger_examples.old_school_logger.a_module import a_function

logger = SATLogger(__name__)

logger.info('start')

a_function()

logger.info('end')

