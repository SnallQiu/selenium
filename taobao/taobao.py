# -- coding: utf-8 --
# author: snall  time: 2018/1/24
import requests
import re
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
import time
class Login:
    url = 'https://login.taobao.com/member/login.jhtml'
    url_taobao = 'https://buyertrade.taobao.com/trade/itemlist/asyncBought.htm?action=itemlist/BoughtQueryAction&event_submit_do_query=1&_input_charset=utf8'
    def __init__(self,tel='',passwd=''):
        self.tel = tel #账号
        self.passwd = passwd

    def login(self):
        driver = webdriver.PhantomJS()
        driver.maximize_window()
        driver.get(self.url)
        element_switch = WebDriverWait(driver,60).until(lambda driver:\
                    driver.find_element_by_xpath('//*[@id= "J_Quick2Static"]'))
        time.sleep(2)
        element_switch.click()
        tel_name = driver.find_element_by_name('TPL_username')
        tel_name.send_keys(self.tel)
        time.sleep(5)
        driver.implicitly_wait(10)
        '''
        password = driver.find_element_by_name('TPL_password')
        password.send_keys(self.passwd)
        time.sleep(2)
        '''
        '''拖动滑块'''
        while True:
            driver.find_element_by_name('TPL_username').clear()
            driver.find_element_by_name('TPL_username').send_keys(self.tel)
            password = driver.find_element_by_name('TPL_password')
            password.clear()
            password.send_keys(self.passwd)
            time.sleep(2)


            try:
                first_area = driver.find_element_by_xpath('//span[@id="nc_1_n1z"]')
                ActionChains(driver).drag_and_drop_by_offset(first_area,258,0).perform()
                text = driver.find_element_by_xpath('//*[@id="nc_1__scale_text"]/span')
                print(text.text)
                time.sleep(5)
                if text.text == '验证通过':
                    break
                print(driver.find_element_by_xpath('//*[@id="nocaptcha"]/div/span/').text)
                if driver.find_element_by_xpath('//*[@id="nocaptcha"]/div/span/').text[1] =='哎呀，出错了，点击':
                    driver.find_element_by_xpath('//*[@id="nocaptcha"]/div/span/a').claik()

            except Exception as e:
                driver.find_element_by_xpath('//button[@id="J_SubmitStatic"]').click()


                #print(str(e))

                pass



        driver.find_element_by_xpath('//button[@id="J_SubmitStatic"]').click()
        print(driver.get_cookies())

        x
    def login_alipay(self):
        session = requests.session()
        session.headers.clear()

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(self.url)
        element_switch = WebDriverWait(driver, 60).until(lambda driver: \
                                                             driver.find_element_by_xpath('//*[@id= "J_Quick2Static"]'))
        time.sleep(2)
        element_switch.click()
        driver.find_element_by_xpath('//*[@id="J_OtherLogin"]').click()
        element_switch = WebDriverWait(driver,60).until(lambda driver:\
                                                            driver.find_element_by_xpath('//*[@id="J-loginMethod-tabs"]/li[2]'))
        element_switch.click()
        account = driver.find_element_by_xpath('//*[@id="J-input-user"]')
        account.send_keys(self.tel)
        password = driver.find_element_by_xpath('//*[@id="password_rsainput"]')
        password.send_keys(self.passwd)

        driver.find_element_by_xpath('//*[@id="J-login-btn"]').click()

        cookies = driver.get_cookies()
        print("登陆成功！")
        for cookie in cookies:
            session.cookies.set(cookie['name'], cookie['value'])
        return session

    def getinfo(self, session):

        form_data = {
            'buyerNick':'',
            'dateBegin':0,
        'dateEnd': 0,
        'lastStartRow': '2144670213_9223370573317340807_1912483380051302_1912483380051302',
        'logisticsService':'',
        'options':0,
        'orderStatus':'',
        'pageNum':1,
        'pageSize': 15,
        'queryBizType':'',
        'queryOrder':'desc',
        'rateStatus':'',
        'refund':'',
        'sellerNick':'',
        'prePageNo':'7',
        }
        r = session.post(self.url_taobao,data = form_data).text
        print('+++++++')
        print(r)
        print('+++++++')




        '''
        page_money = re.search('realTotal.*?(\d*\.\d*)',r).group(1)
        all_money = 0
        for i in page_money:
            all_money = int(i)+all_money
        print(all_money)
        '''













tel = '17854212463'
password = ''
mytao = Login(tel,password)
session = mytao.login_alipay()
mytao.getinfo(session)