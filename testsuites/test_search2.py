from testsuites.base_testcase import  base_testcase
from pageobjects.index import *
import time
import unittest
from framework.util import Util

filepath = "E:/Appium__test/data/data.xlsx"
sheetName = "Sheet1"

class test_search2(base_testcase):
   def test_search(self):

      login=Login(self.driver)
      login.login("ccccffvghhh@122.com","bvddv")
      time.sleep(10)

      u = Util()
      users = u.read_excel(filepath, sheetName)
      data = users[0]
      email = data["email"]
      pwd = data["password"]
      print(email, pwd)
      relogin=reLogin(self.driver)
      relogin.relogin(email,pwd)
      time.sleep(10)

      tuichu=TuiChu(self.driver)
      tuichu.tuichu()
      time.sleep(5)

if __name__=="__main__":
   unittest.main()
