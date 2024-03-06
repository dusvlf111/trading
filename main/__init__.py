from ui.ui import *
from kiwoom.kiwoom import *

# --------------------------------------------------
#내 모듈
from MY_logger.MY_logger import logger  #로거 설정 모듈 (전역)
from MY_load_dotenv.load_env import load_env_variables  #env읽기 모듈
from exception_handler.exception_handler import *
# --------------------------------------------------


class Main():
    def __init__(self):
        logger.debug('Main init')

        Ui_class()
        
        Kiwoom()
    
    
if __name__=='__main__':
    
    logger.info('-'*20+'start programe'+'-'*20)
    
    Main()
    
    logger.info('-'*20+'end programe'+'-'*20)