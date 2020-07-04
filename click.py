from selenium import webdriver
import time
from random import randrange
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
#click_time = 50
#xpath = '//*[@id="reload-button"]'
#click_time_2 = 30
#xpath = '/html/body/div[11]/div/div[33]/a[12]'

#browser_one = webdriver.Chrome('C:\\Users\\ziraf\\Downloads\\chromedriver')
browser_one = webdriver.Firefox()


#browser = webdriver.Chrome('C:\\Users\\ziraf\\Downloads\\chromedriver')

browser_one.get("https://www.pronworld.com/")

#browser_list.append(browser_one)

while(True):
    browser_one.maximize_window()
    browser_one.implicitly_wait(1000)
    btn = browser_one.find_element_by_class_name("next")
    time.sleep(120)
    browser_one.implicitly_wait(1000)
    #browser_one.refresh()
    btn.click()
    print('browser has been clicked')






#xpath_1 = '/html/body/div[2]/div/div[1]/form/div[4]/ul/li/a/img'

#btn = driver.find_element_by_xpath(xpath_1)
#btn = browser.find_element_by_link_text('Priljubljeno')
#btn.click()
#xpath = '//*[@id="torrentlist"]/div/div[7]/ul/li[2]/a'
#browser.implicitly_wait(20)

#btn_2 = browser.find_element_by_link_text('MC STOJAN X HURRICANE - TUTURUTU (OFFICIAL VIDEO)')
#btn_2.click()
