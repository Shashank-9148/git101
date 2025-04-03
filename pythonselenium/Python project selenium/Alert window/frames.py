from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://ui.vision/demo/webtest/frames/")
driver.maximize_window()
driver.switch_to.frame("Web Test")
driver.find_element(By.XPATH,"//input[contains(@type,'text')]").send_keys('abc')
#driver.switch_to.default_content()
#driver.switch_to.frame("")
#driver.find_element(By.XPATH,"//*[@id='navbar-top-firstrow']/li[8]/a").click()
