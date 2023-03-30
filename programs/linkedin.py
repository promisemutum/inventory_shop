from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime

driver = webdriver.Chrome(r"C:\Users\Blaze Pro\Documents\python\chromedriver.exe")

url = 'https://www.linkedin.com/feed/'
driver.get(url)
time.sleep(10)