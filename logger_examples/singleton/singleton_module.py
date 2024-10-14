from sat.logs import SATLoggerSingleton


logger = SATLoggerSingleton(__name__)

def singleton_example_function():

    logger.info('Doing some module stuff', extra={'cid': 'test-cid'})
    
    return 'lol'

