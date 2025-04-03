#using implicitly_wait()
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.google.com/")
driver.maximize_window()
ed=driver.find_element(By.NAME,"q")
ed.send_keys("amazon")
ed.submit()
#time.sleep(5)
driver.find_element(By.XPATH,"//span[text()='Shop online at Amazon India']").click()
#driver.quit()