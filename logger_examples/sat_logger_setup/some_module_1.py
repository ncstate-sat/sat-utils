from sat.logs import SATLoggerStripped


from logger_examples.sat_logger_setup.module_2 import some_other_function


logger = SATLoggerStripped(__name__)

def some_function():
    logger.info('Going to do some stuff')
    some_other_function()
    logger.info('Done with the stuff', extra={'cid': '00102301'})
    return None
