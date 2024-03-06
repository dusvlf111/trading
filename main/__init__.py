from ui.ui import *
from kiwoom.kiwoom import *

# --------------------------------------------------
from MY_logger.MY_logger import logger
from MY_load_dotenv.load_env import load_env_variables
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