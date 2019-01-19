from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
def open_amazon(item):#setup Edge browser to use the proxies
    driver = webdriver.Firefox() 

    #apparently amazon pantry doesn't sell veggies
    driver.get('https://www.bigbasket.com/')#open amazon 
    text_box = driver.find_element_by_xpath('//*[@id="input"]')
    text_box.send_keys(item)
    text_box.send_keys(Keys.RETURN)
    time.sleep(20)
    print('closing driver')
    driver.close()
