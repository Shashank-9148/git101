#is_displayed()
#is_enabled()
#is_selected()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
driver.maximize_window()
"""display_status = driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
print("display status:",display_status.is_displayed())
print("display status:",display_status.is_enabled())"""

rd_male = driver.find_element(By.XPATH,"//input[@id='gender-male']")
rd_female = driver.find_element(By.XPATH,"//input[@id='gender-female']")

print("Default radio button status")
print(rd_male.is_selected()) #false
print(rd_female.is_selected()) #false
rd_male.click()
print("After selecting male radio button")
print("Male radio button is selected :",rd_male.is_selected()) #true

print("Default radio button status")
print(rd_male.is_selected())#true
print(rd_female.is_selected())#false
rd_female.click() #true
print("After selecting female radio button")
print("Female radio button is selected :",rd_female.is_selected())