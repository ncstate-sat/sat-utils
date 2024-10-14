from logging import getLogger

LOGGER = getLogger(__name__)

def some_other_function(): 
    LOGGER.info('Did some stuff over here')
    return None