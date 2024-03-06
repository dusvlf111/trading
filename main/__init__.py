from ui.ui import *
from kiwoom.kiwoom import *

# --------------------------------------------------
from MY_logger.MY_logger import logger
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