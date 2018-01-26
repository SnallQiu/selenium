# -- coding: utf-8 --
# author: snall  time: 2018/1/26

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
import requests
import time
from  lxml  import etree

class Zhihu:
    url_login = 'https://www.zhihu.com/signin'
    url = 'https://www.zhihu.com/'
    def __init__(self,account,passwd):
        self.account = account
        self.passwd = passwd


    def login(self):
        session = requests.session()
        session.headers.clear()

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(self.url_login)
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div[1]/input').send_keys(self.account)
        driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/input').send_keys(self.passwd)
        driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/button').click()
        cookies = driver.get_cookies()
        for cookie in cookies:
            session.cookies.set(cookie['name'],cookie['value'])
        return session
    def getinfo(self,session):
        r = session.get(self.url).text
        selector = etree.HTML(r)
        titles = selector.xpath("//title/text()")
        for title in titles:
            print(title)








account = '17854212463'
passwd = 'qq345817576!'
myzhihu = Zhihu(account,passwd)
session = myzhihu.login()
myzhihu.getinfo(session)