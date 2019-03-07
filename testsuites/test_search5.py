from testsuites.base_testcase import  base_testcase
from pageobjects.index import *
import time
import unittest
class test_search5(base_testcase):
   def test_search(self):
      sort=Sort(self.driver)
      sort.sort()
      time.sleep(8)

      guidang = GuiDang(self.driver)
      guidang.guidang()

      delete = Delete(self.driver)
      delete.delete()
      time.sleep(10)

      tuichu = TuiChu(self.driver)
      tuichu.tuichu()
      time.sleep(5)
if __name__ == "__main__":
         unittest.main()