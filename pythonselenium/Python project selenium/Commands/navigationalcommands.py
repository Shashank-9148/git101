#driver.back()
#driver.forward()
#driver.refresh()
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.amazon.com/")
driver.get("https://snapdeal.com/")
driver.back()
driver.forward()
driver.refresh()
time.sleep(5)
driver.close()