import time
from Controller.Base import Base
from Model.Log import logger
from Views.ObjectRepo import Element


__author__ = 'kzhu'

class HomePage(Base):
    def __init__(self,browser):
        Base.__init__(self,browser)

    def navigate_to_hao123(self):
        log = logger()
        driver = self.driver
        try:
            Element(driver,'HomePage','Hao123').get().click()
            time.sleep(3)
        except Exception as e:
            log.log('[-] Error occur @navigate_to_hao123')
            log.log('[-] Error is '+str(e))

    def search(self,search_text):
        log = logger()
        driver = self.driver
        try:
            Element(driver,'HomePage','Search').get().send_keys(search_text)
            time.sleep(1)
            Element(driver,'HomePage','BaiDu').get().click()
        except Exception as e:
            log.log('[-] Error occur @search')
            log.log('[-] Error is '+str(e))

    def get_title(self):
        return super(HomePage,self).get_title()





