import os.path
from configparser import ConfigParser
from appium import webdriver
from framework.logger import Logger
import yaml
import time
logger=Logger(logger="Model").getlog()
class Model(object):
    apk_path = os.path.dirname(os.path.abspath('.'))
    znbwl_driver_path=apk_path+'/app/znbwl.apk'

    def appium_desired(self):
        config=ConfigParser()
        # file_path=os.path.dirname(os.path.abspath('.'))+'/config/config.yaml'
        with open(self.apk_path+'/config/config.yaml','r',encoding='utf-8') as file:
              data=yaml.load(file)
        desired_caps = {}
        desired_caps['platformName'] = data['platformName']  # 设备系统
        desired_caps['platformVersion'] = data['platformVersion']  # 设备系统版本
        desired_caps['deviceName'] = data['deviceName']   # 设备名称
        desired_caps['sessionOverride'] = True
        # 测试apk包的路径
        desired_caps['app'] = self.apk_path + '/app/'+data['app']
        # 不需要每次都安装apk
        desired_caps['noReset'] = True
        # #应用程序的包名
        # desired_caps['appPackage']='com.example.todolist'
        # desired_caps['appActivity']='com.example.todolist.LoginActivity'
        desired_caps['appPackage'] = data['appPackage']
        desired_caps['appActivity'] = data['appActivity']
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)#启动
        time.sleep(10)

    def quit(self):
        self.driver.quit()


if __name__== '__main__':
    Model().appium_desired()

