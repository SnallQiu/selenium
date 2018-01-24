# -- coding: utf-8 --
# author: snall  time: 2018/1/24

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
import time
class Login:
    url = 'https://login.taobao.com/member/login.jhtml'
    def __init__(self,tel='',passwd=''):
        self.tel = tel #账号
        self.passwd = passwd

    def login(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(self.url)
        element_switch = WebDriverWait(driver,60).until(lambda driver:\
                    driver.find_element_by_xpath('//*[@id= "J_Quick2Static"]'))
        time.sleep(5)
        element_switch.click()
        tel_name = driver.find_element_by_name('TPL_username')
        tel_name.send_keys(self.tel)
        time.sleep(5)
        driver.implicitly_wait(10)
        password = driver.find_element_by_name('TPL_password')
        password.send_keys(self.passwd)
        time.sleep(5)
        '''拖动滑块'''
        try:
            first_area = driver.find_element_by_xpath('//span[@id="nc_1_n1z"]')
            after_area = driver.find_element_by_xpath('//span[@class="nc-lang-cnt"]')
            ActionChains(driver).drag_and_drop(first_area,after_area).perform()
        except:
            pass
        driver.find_element_by_xpath('//button[@id="J_SubmitStatic"]').click()



tel = '17854212463'
password = ''
mytao = Login(tel,password)
mytao.login()