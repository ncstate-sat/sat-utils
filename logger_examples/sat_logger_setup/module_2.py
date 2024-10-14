from sat.logs import SATLoggerStripped

LOGGER = SATLoggerStripped(__name__)

def some_other_function(): 
    LOGGER.info('Did some stuff over here')
    return None
