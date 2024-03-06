from MY_logger.MY_logger import logger
from exception_handler.exception_handler import *

# ------------------------------------------------------------

def logger_test():
    logger.info('info message')

logger_test()

# ------------------------------------------------------------

@exception_handler
def exception_test_pass():
    raise ValueError("This is a test1 error.")

exception_test_pass()

# ------------------------------------------------------------

# @exception_stop
# def exception_test():
#     logger.debug('exception_test')
#     int('abc')

# exception_test()

# print('hello')

# ------------------------------------------------------------
# try:
#     int('abc')
# except Exception as e:
#     logger.error(e)

# print('hello')