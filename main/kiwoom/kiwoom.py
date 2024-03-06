from PyQt5.QAxContainer import *
from MY_logger.MY_logger import logger

class Kiwoom(QAxWidget):
    """ Kiwoom API 컨트롤 """
    
    def __init__(self):
        logger.debug('Kiwoom init')
        
        super().__init__()
        self.get_ocx_instance()
        
    def get_ocx_instance(self):
        logger.debug('set API')
        
        self.setControl('KHOPENAPI.KHOpenAPICtrl.1')
        