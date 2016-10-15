#!/usr/bin/env python

from selenium import webdriver
from pyvirtualdisplay import Display
import webbrowser
import time
import os
i=0

chromedriver = "/home/shubh/python/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver

while 1:
	driver = webdriver.Chrome(chromedriver)
	driver.get("http://shubhagrawal.in")
	time.sleep(7)
	driver.quit()
	i=i+1
	print i
	time.sleep(10)

#display = Display(visible=0, size=(1024, 768))

#display.start()
#browser2=webdriver.Firefox()
#browser2.get("http://www.shubhagrawal.in")
#webbrowser.open_new_tab("http://www.shubhagrawal.in")

#time.sleep(10)
#display.stop()


