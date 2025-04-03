from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@title='Sign in']").click()
alertwindow=driver.switch_to.alert
alertwindow.accept()
