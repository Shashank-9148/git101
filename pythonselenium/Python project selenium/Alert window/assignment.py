import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
#driver.find_element(By.ID,"alertBtn").click()
#time.sleep(5)
#alertbutton = driver.switch_to.alert
#alertbutton.accept()
driver.find_element(By.CLASS_NAME,"wikipedia-search-input").send_keys("selenium")
driver.find_element(By.CLASS_NAME,"wikipedia-search-button").click()
time.sleep(3)
ele=driver.find_elements(By.XPATH,"//div[@class='wikipedia-search-results']//descendants::a")
print(ele.text)

