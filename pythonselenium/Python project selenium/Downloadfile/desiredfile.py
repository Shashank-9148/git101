from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os
location=os.getcwd()

def chrome_setup():
    driver=webdriver.Chrome()
    preferences = {"download.default_directory":location}
    ops=webdriver.ChromeOptions()
    ops.add_experimental_option("prefs",preferences)
    return driver
driver = chrome_setup()


driver.get("https://filesamples.com/formats/doc")
driver.maximize_window()
button=driver.find_element(By.XPATH,"//div[@class='output']//div[1]//a[1]")
driver.execute_script("arguments[0].scrollIntoView();",button)
value=driver.execute_script("return window.pageYOffset;")
button.click()