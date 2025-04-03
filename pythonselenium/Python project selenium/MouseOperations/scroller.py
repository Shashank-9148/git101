import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver=webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_area")
driver.maximize_window()

"""#1 scroll down page by pixel
driver.execute_script("window.scrollBy(0,3000)"," ")
value=driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:",value)

#2 scroll down page till the element is visible
country=driver.find_element(By.XPATH,"//a[@title='United Kingdom']")
driver.execute_script("arguments[0].scrollIntoView();",country)
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:",value) #4280.7998046875
"""
#3 scroll down page till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:",value) #16493.599609375
"""
time.sleep(5)
#4scrollup to starting position
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:",value)