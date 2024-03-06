from MY_logger.MY_logger import logger
from exception_handler.exception_handler import *
from MY_load_dotenv.load_env import load_env_variables

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
# ------------------------------------------------------------

# .env 파일 내의 환경 변수 읽어오기
env_variables = load_env_variables()

# 결과 출력
for key, value in env_variables.items():
        print(f"{key}: {value}")
