from testsuites.base_testcase import  base_testcase
from pageobjects.index import *
import time
import unittest

class test_search3(base_testcase):
    def test_search(self):
        relogin = reLogin(self.driver)
        relogin.relogin("qwzvxw@12.com","1234567")
        time.sleep(10)

        amend=Amend(self.driver)
        amend.amend('asdd')
        time.sleep(8)



if __name__=="__main__":
   unittest.main()
