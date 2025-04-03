from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/")
#driver.save_screenshot(os.getcwd()+"\homepage.png")
driver.save_screenshot("C:\\Users\\Shashank L\\OneDrive\\Pictures\\Screenshots\\homepage.png")
#driver.get_screenshot_as_png()
#driver.get_screenshot_as_file(os.getcwd()+"\\homepage.png")
#driver.get_screenshot_as_base64()
driver.quit()