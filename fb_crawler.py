from selenium import webdriver
import os

chromedriver="/home/shubh/python/chromedriver"
os.environ["webdriver.chrome.driver"]=chromedriver
browser=webdriver.Chrome(chromedriver)

browser.get("http://www.facebook.com")
emailEle=browser.find_element_by_id('email')
emailEle.send_keys('shubh.agrawal111@gmail.com')
passEle=browser.find_element_by_id('pass')
passEle.send_keys('blackhole123')
passEle.submit()


#searchEle=browser.find_element_by_name('q')
#searchEle.send_keys('Anurag Sharma')
#searchEle.submit()
