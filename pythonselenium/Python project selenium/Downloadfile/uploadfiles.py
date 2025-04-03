from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.foundit.in/")
driver.find_element(By.XPATH,"//span[@class='upr case semi-bold']").click()
driver.find_element(By.XPATH,"//*[@id='file-upload']").send_keys("Downloads\Shashank.New")