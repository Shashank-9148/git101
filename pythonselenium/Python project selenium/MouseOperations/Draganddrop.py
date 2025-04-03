from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html#google_vignette")
driver.maximize_window()

act = ActionChains(driver)
source_ele=driver.find_element(By.ID,"box2")
target_ele=driver.find_element(By.ID,"box103")
act.drag_and_drop(source_ele,target_ele).perform()