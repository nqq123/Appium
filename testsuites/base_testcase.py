import unittest
from appium import webdriver
from framework.browser_engine import Model


class base_testcase(unittest.TestCase):
    def setUp(self):
        self.browserengine=Model()
        self.browserengine.appium_desired()
        self.driver=self.browserengine.driver



    def tearDown(self):
        self.browserengine.quit()
        print("结束")
