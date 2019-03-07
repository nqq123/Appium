from testsuites.base_testcase import  base_testcase
from pageobjects.index import *
import time
import unittest

class test_search1(base_testcase):


       def test_search(self):
          index=Register(self.driver)
          index.register("Nikcey","1zxc@12.com","1234567")
          time.sleep(5)

          tuichu = TuiChu(self.driver)
          tuichu.tuichu()
          time.sleep(5)



if __name__=="__main__":
   unittest.main()

