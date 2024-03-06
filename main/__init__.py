from ui.ui import *
from kiwoom.kiwoom import *
from MY_logger.MY_logger import logger

class Main():
    def __init__(self):
        logger.debug('Main init')

        Ui_class()
        Kiwoom()
    
    
if __name__=='__main__':
    
    logger.info('start programe')
    
    Main()
    
    logger.info('and programe')