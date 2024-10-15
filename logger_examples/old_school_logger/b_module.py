from sat.logs import SATLogger

logger = SATLogger(__name__)

def b_function():
    logger.info('B message')
    return