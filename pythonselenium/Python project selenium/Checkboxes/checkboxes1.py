import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
#driver.find_element(By.XPATH,"//*[@id='sunday']").click()
checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
print(len(checkboxes))
#below code clicks every checkbox
"""for i in range(len(checkboxes)):
    checkboxes[i].click()"""

#below code clicks checkbox based on my choice
for checkbox in checkboxes:
    weekname = checkbox.get_attribute('id')
    if weekname == 'sunday' or weekname == 'monday':
        checkbox.click()
"""
#to select last two check boxes
for i in range(len(checkboxes)-2,len(checkboxes)):
    checkboxes[i].click()

#to select first two check boxes
for i in range(len(checkboxes)):
    if i<2:
     checkboxes[i].click()
time.sleep(5)
#to clear all the checkboxes
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()"""
