from testsuites.base_testcase import  base_testcase
from pageobjects.index import *
import time
import unittest
class test_search4(base_testcase):
   def test_search(self):
       relogin = reLogin(self.driver)
       relogin.relogin("qwder@12.com", "1234567")
       time.sleep(10)

       add=Add(self.driver)
       add.add("bbbbj","mmmmmi")
       time.sleep(8)


       find=Find(self.driver)
       find.find("fff")
       time.sleep(5)

if __name__=="__main__":
   unittest.main()


