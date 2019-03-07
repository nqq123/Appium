from appium import webdriver
import os
import time
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import By
from framework.base import BasePage
#注册
class Register(BasePage):
   caidan = (By.ID, 'com.pdswp.su.smartcalendar:id/ab_icon2')
   # 登录按钮进入注册
   register1 = (By.ID, 'com.pdswp.su.smartcalendar:id/email')
   # 注册按钮
   register2 = (By.ID, 'com.pdswp.su.smartcalendar:id/register')
   # 注册昵称输入框
   username = (By.ID, 'com.pdswp.su.smartcalendar:id/username')
   # 注册邮箱输入框
   mail = (By.ID, 'com.pdswp.su.smartcalendar:id/email')
   # 注册密码输入框
   password = (By.ID, 'com.pdswp.su.smartcalendar:id/password')
   # 提交注册
   button = (By.ID, 'com.pdswp.su.smartcalendar:id/reguser')

   def register(self, username, mail, password):
      self.click(*self.caidan)
      self.click(*self.register1)
      self.click(*self.register2)
      self.send_keys(username, *self.username)
      self.send_keys(mail, *self.mail)
      self.send_keys(password, *self.password)
      self.click(*self. button)


#登陆失败
class Login(BasePage):
   caidan = (By.ID, 'com.pdswp.su.smartcalendar:id/ab_icon')
   register1 = (By.ID, 'com.pdswp.su.smartcalendar:id/email')
   email=(By.ID,'com.pdswp.su.smartcalendar:id/email')
   pwd=(By.ID,'com.pdswp.su.smartcalendar:id/password')
   login_button=(By.ID,"com.pdswp.su.smartcalendar:id/login")
   retern2 = (By.ID, "com.pdswp.su.smartcalendar:id/ab_icon")
   def login(self,email,pwd):
      self.click(*self.caidan)
      self.click(*self.register1)
      self.send_keys(email, *self.email)
      self.send_keys(pwd, *self.pwd)
      self.click(*self.login_button)
      self.click(*self.retern2)
      self.get_windows_img()

#登陆成功
class reLogin(BasePage):
   retern2=(By.ID,"com.pdswp.su.smartcalendar:id/ab_icon")
   register1 = (By.ID, 'com.pdswp.su.smartcalendar:id/email')
   email = (By.ID, 'com.pdswp.su.smartcalendar:id/email')
   pwd = (By.ID, 'com.pdswp.su.smartcalendar:id/password')
   login_button = (By.ID, "com.pdswp.su.smartcalendar:id/login")
   def relogin(self,email,pwd):
      self.click(*self.retern2)
      self.click(*self.register1)
      self.send_keys(email, *self.email)
      self.send_keys(pwd, *self.pwd)
      self.click(*self.login_button)
      self.get_windows_img()
#退出当前账户
class TuiChu(BasePage):
   caidan = (By.ID, 'com.pdswp.su.smartcalendar:id/ab_icon2')
   register1 = (By.ID, 'com.pdswp.su.smartcalendar:id/email')
   exit = (By.ID,'com.pdswp.su.smartcalendar:id/exit')
   def tuichu(self):
      self.click(*self.caidan)
      self.click(*self.register1)
      self.click(*self.exit)
#修改用户名
class Amend(BasePage):
   caidan = (By.ID, 'com.pdswp.su.smartcalendar:id/ab_icon2')
   user=(By.ID,'com.pdswp.su.smartcalendar:id/login')
   user1=(By.ID,'com.pdswp.su.smartcalendar:id/title')
   user2=(By.ID,'com.pdswp.su.smartcalendar:id/username')
   sure=(By.ID,'com.pdswp.su.smartcalendar:id/quick_add')
   tuichu1 = (By.ID, 'com.pdswp.su.smartcalendar:id/exit')   # 退出
   def amend(self,user2):
      self.click(*self.caidan)
      self.click(*self.user)
      self.click(*self.user1)
      self.send_keys(user2,*self.user2)
      self.click(*self.sure)
      self.click(*self.tuichu1)

#添加备忘录
class Add(BasePage):
   caidan = (By.ID, 'com.pdswp.su.smartcalendar:id/ab_icon2')
   add1=(By.ID,'com.pdswp.su.smartcalendar:id/design_menu_item_text')
   content=(By.ID,'com.pdswp.su.smartcalendar:id/add_input_content')
   sure1=(By.ID,'com.pdswp.su.smartcalendar:id/quick_add')
   add2=(By.ID,'com.pdswp.su.smartcalendar:id/menuAdd')
   def add(self,content,content1):
      self.click(*self.caidan)
      self.click(*self.add1)
      self.send_keys(content,*self.content)
      self.click(*self.sure1)
      self.click(*self.add2)
      self.send_keys(content1,*self.content)
      self.click(*self.sure1)
#搜索
class Find(BasePage):
   find1=(By.ID,'com.pdswp.su.smartcalendar:id/toolbar_search')
   find2=(By.ID,'android:id/search_src_text')
   def find(self,find2):
      self.click(*self.find1)
      self.send_keys(find2,*self.find2)
      self.driver.keyevent(66)

#排序
class Sort(BasePage):
   button_a=(By.ID,'com.pdswp.su.smartcalendar:id/note_all')
   sort1=(By.NAME,'排序')
   sort2=(By.ID,"com.pdswp.su.smartcalendar:id/sortBtn")
   sort3=(By.ID,'com.pdswp.su.smartcalendar:id/sortBtn')
   button_ok=(By.ID,'com.pdswp.su.smartcalendar:id/toolbar_ok')
   def sort(self):
      self.long_press(*self.button_a)
      self.click(*self.sort1)
      self.down_move(*self.sort2)
      self.click(*self.button_ok)
class GuiDang(BasePage):
   first = (By.ID,'com.pdswp.su.smartcalendar:id/note_title')
   caidan = (By.ID, 'com.pdswp.su.smartcalendar:id/ab_icon2')
   gd1 = (By.NAME,'归档')
   gd2 = (By.ID,'com.pdswp.su.smartcalendar:id/note_all')
   hf = (By.ID,'com.pdswp.su.smartcalendar:id/menu')
   def guidang(self):
      self.long_press(*self.first)
      self.click(*self.gd1)
      self.click(*self.caidan)
      self.click(*self.gd1)
      self.left_move(*self.gd2)
      self.click(*self.hf)
      self.click(*self.caidan)
#删除
class Delete(BasePage):
   first = (By.ID, 'com.pdswp.su.smartcalendar:id/note_all')
   delete1 = (By.NAME,'删除备忘')
   caidan = (By.ID, 'com.pdswp.su.smartcalendar:id/ab_icon2')
   huishou = (By.NAME,'回收站')
   qk = (By.NAME,'清空回收站')
   ok = (By.NAME,'确定')
   hsz = (By.ID,'com.pdswp.su.smartcalendar:id/ab_icon')
   def delete(self):
      self.long_press(*self.first)
      self.click(*self.delete1)
      self.click(*self.caidan)
      self.click(*self.huishou)
      self.click(*self.qk)
      self.click(*self.ok)
      self.click(*self.hsz)







