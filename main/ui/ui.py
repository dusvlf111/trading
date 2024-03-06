from kiwoom.kiwoom import *
from PyQt5.QtWidgets import *
import sys
from MY_logger.MY_logger import logger

class Ui_class():

    def __init__(self):

        logger.debug('ui_class init')
        self.app = QApplication(sys.argv)
        
        self.kiwoom = Kiwoom()
        self.app.exec_()