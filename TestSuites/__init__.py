import unittest
import datetime
from Controller import ControllerRunner

__author__ = 'kzhu'


class __init__(unittest.TestCase):


    DRIVER = ControllerRunner.Runner('chrome')
    url = 'www.baidu.com'
    g_pass_count  = 0
    g_fail_count  = 0
    g_error_count = 0
    startTime = datetime.datetime.now()
    result = []

    @classmethod
    def setUpClass(cls):
        cls.DRIVER.open(cls.url)
        return cls.DRIVER

    @classmethod
    def tearDownClass(cls):
        cls.DRIVER.quit()











