from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/")
driver.maximize_window()
#this code is to access get_attribute value
box=driver.find_element(By.XPATH,"//input[@id='Email']")
box.clear()
box.send_keys("abc@gmail.com")

print(box.text) #returns inner text of the element
print(box.get_attribute('id')) #returns values of any attribute of web element

#this code is to access text value
box=driver.find_element(By.XPATH,"//button[normalize-space()='Log in']")
print("text value :",box.text)