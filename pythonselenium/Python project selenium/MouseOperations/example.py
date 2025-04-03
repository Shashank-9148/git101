import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(10)
"""one=driver.find_element(By.XPATH,"//input[@id='field1']")
one.send_keys("Hello lisha")
button=driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")
act = ActionChains(driver)
time.sleep(5)
act.double_click(button).perform()"""

slide=driver.find_element(By.XPATH,"//div[@id='draggable']")
targ=driver.find_element(By.XPATH,"//div[@id='droppable']")
act = ActionChains(driver)
time.sleep(3)
act.drag_and_drop(slide,targ).perform()