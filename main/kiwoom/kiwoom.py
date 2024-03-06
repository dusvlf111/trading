from PyQt5.QAxContainer import *
from PyQt5.QtCore import *

from MY_logger.MY_logger import logger


class Kiwoom(QAxWidget):
    """ Kiwoom API 컨트롤 """
    
    def __init__(self):
        super().__init__()
        logger.debug('Kiwoom init')
        
        ###########################evnet loop 모음##############################
        self.login_event_loop = None
        
        
        #######################################################################
        
        self.get_ocx_instance()
        self.event_slots()
        self.signal_login_commConnect()
        
        
    def get_ocx_instance(self):
        '''
        
        '''
        logger.debug('set API')
        
        self.setControl('KHOPENAPI.KHOpenAPICtrl.1')
        
        
    def event_slots(self):
        logger.debug('event_slots')
        self.OnEventConnect.connect(self.login_slot)
        
    def login_slot(self, errCode):
        logger.debug('login_slot')
        print(errCode)
        
        self.login_event_loop.exit()
        
    def signal_login_commConnect(self):
        logger.debug('signal_login_commConnect')

        self.dynamicCall('CommConnect()')
        self.login_event_loop = QEventLoop()
        self.login_event_loop.exec_()
        