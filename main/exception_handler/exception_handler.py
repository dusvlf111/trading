# 에러처리 데코레이터

from MY_logger.MY_logger import logger
import sys

def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"An exception occurred: {e}")
    return wrapper


def exception_stop(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.critical(f"An exception occurred: {e}")
            logger.critical('-'*20+"Forcefully terminating the program"+'-'*20)
            sys.exit()
    return wrapper
