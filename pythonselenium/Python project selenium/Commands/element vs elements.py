from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
"""
#find element returns single webelement
#1:locator matching with single web element
element=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
element.send_keys("samsung galaxy")

#2:locator matching with multiple webelements
element = driver.find_element(By.XPATH,"//div[@class='footer']//a")
print(element.text) #prints first link from the footer "sitemap"

#3:Element not available then throw no such exception
login_element=driver.find_element(By.LINK_TEXT,"Log")
login_element.click()


#find elements return multiple web elements
#1:locator matching with single webelement
elements = driver.find_elements(By.XPATH,"//input[@id='small-searchterms']")
print(len(elements))
elements[0].send_keys("samsung galaxy")

#2:locator matching with multiple webelements
elements = driver.find_elements(By.XPATH,"//div[@class='footer']//a")
print(len(elements))
print(elements[0].text)
for i in elements:
    print(i.text)"""

#3:element not available=this doesnot throws exception
elements = driver.find_elements(By.LINK_TEXT,"Log")
print("elements returned :",len(elements))
