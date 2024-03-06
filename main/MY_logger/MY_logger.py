# logger.py

import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime

# 로거 생성
logger = logging.getLogger("My_log")
logger.setLevel(logging.DEBUG)

# 포매터 생성 (함수 이름 추가)
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(funcName)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# 콘솔 핸들러 생성
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# 파일 핸들러 생성 
log_file = f"log.log" #로그파일 이름
file_handler = RotatingFileHandler(log_file, maxBytes=1024 * 1024, backupCount=3)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


# 사용 예시
if __name__ == "__main__":
    logger.debug('debugg')
    logger.info('info')
    logger.warning('warnging')
    logger.error('error')
    logger.critical('critical')
    
