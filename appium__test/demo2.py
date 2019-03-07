from appium import webdriver
import os
import time
apk_path=os.path.dirname(os.path.abspath('.'))

desired_caps={}
desired_caps['platformName']='Android'
desired_caps['platformVersion']='6.2.7.1'
desired_caps['deviceName']='127.0.0.1:62001'
desired_caps['sessionOverride'] = True

desired_caps['app'] = apk_path + '/app/znbwl.apk'
desired_caps['noReset']=True

desired_caps['appPackage'] = 'com.pdswp.su.smartcalendar'
desired_caps['appActivity'] = 'com.pdswp.su.smartcalendar.WelcomeNote'

driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)#启动
time.sleep(4)

#注册
driver.find_element_by_id('com.pdswp.su.smartcalendar:id/ab_icon').click()
driver.find_element_by_id('com.pdswp.su.smartcalendar:id/email').click()
driver.find_element_by_id('com.pdswp.su.smartcalendar:id/register').click()
driver.find_element_by_id('com.pdswp.su.smartcalendar:id/username').send_keys('Nikey')
driver.find_element_by_id('com.pdswp.su.smartcalendar:id/email').send_keys('qwer@12.com')
driver.find_element_by_id('com.pdswp.su.smartcalendar:id/password').send_keys('1234567')
driver.find_element_by_id('com.pdswp.su.smartcalendar:id/reguser').click()