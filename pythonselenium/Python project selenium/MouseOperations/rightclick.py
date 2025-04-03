import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.implicitly_wait(10)

button=driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")

act_time = ActionChains(driver)
time.sleep(5)
act_time.context_click(button).perform()