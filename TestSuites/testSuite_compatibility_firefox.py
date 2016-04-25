import  unittest
from Controller import ControllerRunner
from Model.Result import TestResult


__author__ = 'kzhu'
class CompatibilityFirefox(unittest.TestCase):

    FIREFOX = ControllerRunner.Runner('firefox')

    @classmethod
    def setUpClass(cls):
        cls.FIREFOX.open('www.baidu.com')
        return cls.FIREFOX

    @classmethod
    def tearDownClass(cls):
        cls.FIREFOX.quit('firefox')


    def setUp(self):
        self.suite_name = "%s.%s" % (self.__class__.__module__, self.__class__.__name__)
        self.case_name = self.id().split('.')[-1]
        self.now_handle = self.FIREFOX.get_window_handle()


    def test_search(self):
        try:
            self.FIREFOX.search('selenium')
            self.assertIn('selenium',self.FIREFOX.get_title())
            TestResult().addSuccess(self.suite_name,0,self.case_name,'')
        except AssertionError as ae:
            TestResult().addFail(self.suite_name,1,self.case_name,str(ae))
        except Exception as e:
            TestResult().addError(self.suite_name,2,self.case_name,str(e))

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
