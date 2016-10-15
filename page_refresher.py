from selenium import webdriver
import os, time

chromedriver="/home/shubh/python/chromedriver"
os.environ["webdriver.chrome.driver"]=chromedriver
browser=webdriver.Chrome(chromedriver)

browser.get("http://192.168.0.104")

while 1:
	browser.refresh()
	time.sleep(1)
