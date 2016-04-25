import  unittest
from Controller import ControllerRunner
from Model.Log import logger
from Model.Result import TestResult
from TestSuites import __init__


__author__ = 'kzhu'


class EndToEndModule(__init__):

    log = logger()


    @classmethod
    def setUpClass(cls):
        try:
            super(EndToEndModule, cls).setUpClass()

        except Exception:
            cls.log.log('[+] Trying to start a webdriver but not the first one')
            cls.DRIVER = ControllerRunner.Runner('chrome')
            cls.DRIVER.open(__init__.url)


    @classmethod
    def tearDownClass(cls):
        super(EndToEndModule, cls).tearDownClass()

    def setUp(self):
        self.suite_name = "%s.%s" % (self.__class__.__module__, self.__class__.__name__)
        self.case_name = self.id().split('.')[-1]
        self.now_handle = self.DRIVER.get_window_handle()


    def test_search(self):
        try:
            self.DRIVER.search('selenium')
            self.assertIn('selenium',self.DRIVER.get_title())
            TestResult().addSuccess(self.suite_name,0,self.case_name,'')
        except AssertionError as ae:
            TestResult().addFail(self.suite_name,1,self.case_name,str(ae))
        except Exception as e:
            TestResult().addError(self.suite_name,2,self.case_name,str(e))


    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
