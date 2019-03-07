#utf-8
from appium import webdriver
import os
import time
from appium.webdriver.common.touch_action import TouchAction
apk_path= os.path.dirname(os.path.abspath('.'))

desired_caps={}
desired_caps['platformName']="Android" #设备系统
desired_caps['platformVersion'] = '6.2.7.1' #设备系统版本
desired_caps['deviceName'] = '127.0.0.1:62001'  #设备名称
desired_caps['sessionOverride'] = True

desired_caps['app'] = apk_path + '/app/znbwl.apk'

desired_caps['noReset']=True
#应用程序的包名
desired_caps['appPackage'] = 'com.example.todolist'
desired_caps['appActivity']='com.example.todolist.LoginActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)#启动
#登陆
driver.find_element_by_id('com.example.todolist:id/nameET').send_keys('1')
driver.find_element_by_id('com.example.todolist:id/passwordET').send_keys('1')
driver.find_element_by_id('com.example.todolist:id/loginBtn').click()
#待办事项
driver.find_element_by_id('com.example.todolist:id/action_new').click()
driver.find_element_by_class_name('android.widget.EditText').send_keys('grbb')
driver.find_element_by_id('com.example.todolist:id/saveBtn').click()
#删除
delete1=driver.find_element_by_id('com.example.todolist:id/toDoItemDetailTv')
TouchAction(driver).long_press(delete1).perform()
time.sleep(3)
driver.find_element_by_name('删除').click()
driver.find_element_by_id('android:id/button1').click()