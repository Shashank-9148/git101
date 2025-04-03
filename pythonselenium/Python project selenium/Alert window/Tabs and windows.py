import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.maximize_window()
"""driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
reglink=Keys.CONTROL + Keys.RETURN
driver.find_element(By.LINK_TEXT,"Register").send_keys(reglink)

#New Tab-Selenium 4:opens a new tab & switches to new tab
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.switch_to.new_window('tab')
driver.get("https://demo.nopcommerce.com/")"""

#New Tab-Selenium 4:opens a new browser window & switches to new window
driver.get("https://demo.nopcommerce.com/")
time.sleep(5)
driver.switch_to.new_window("window")
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")