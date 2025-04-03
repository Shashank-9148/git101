import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(By.XPATH,"//*[@id='content']/div/ul/li[1]/button").click()
driver.maximize_window()
time.sleep(5)
alertwindow=driver.switch_to.alert #this will give access to alert window
print(alertwindow.text) #this will gives the text which is captured in the alert window
#alertwindow.send_keys("welcome") #this will sends the input to the alert window
alertwindow.accept() #this will clicks the alert window
#alertwindow.dismiss() #this will clicks the alert window