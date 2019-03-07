import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as  EC
from framework.logger import Logger
from appium.webdriver.common.touch_action import TouchAction
import os
logger=Logger(logger="BasePage").getlog()#参数 logger="BasePage"
class BasePage(object):
    def __init__(self,driver):
        self.driver=driver
    def back(self):
        self.driver.back()
    def forward(self):
        self.driver.forward()
    def get(self,url):
        self.driver.get(url)
    def quit_browser(self):
        pass
    def find_element(self,*loc):
        try:
         return self.driver.find_element(*loc)
        except:
         logger.info("输入内容")
    def send_keys(self,text,*element):
        e1=self.find_element(*element)
        e1.send_keys(text)
    def click(self,*loc):
        e1=self.find_element(*loc)
        e1.click()
    def closed(self):
        self.driver.quit()
    def jh(self):
        self.driver.switch_to.window(self.driver.current_window_handle)
    def switch_to(self,*element):
        e1=self.find_element(*element)
        self.driver.switch_to.frame(e1)
    def chang_window(self):
        window_list=self.driver.window_handles
        self.driver.switch_to.window(window_list[len(window_list)-1])
    def iframe(self):
        self.driver.switch_to.frame(0)
    def text(self,*element):
        e1 = self.find_element(*element)
        return e1.text
    def enter(self,*element):
        self.driver.keyevent(66)
    def tuichu(self):
        self.click(*self.caidan)
    def long_press(self,*element):
        e1=self.driver.find_element(*element)
        TouchAction(self.driver).long_press(e1).perform()

    def left_move(self, *element):
        e1 = self.driver.find_element(*element)
        TouchAction(self.driver).press(e1, x=100, y=50).wait(1000).move_to(e1, x=-50, y=0).release().perform()

    def down_move(self, *element):
        e1 = self.driver.find_elements(*element)
        TouchAction(self.driver).press(e1[0]).wait(1000).move_to(e1[len(e1) - 1]).release().perform()


    def get_windows_img(self):
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        rq = time.strftime(" %Y%m%d%H%M", time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshot and save to folder：/screenshots")
        except Exception as e:
            self.get_windows_img()
            logger.info("Failed to take screenshot! %s" % e)
        logger.info("截图成功。")


