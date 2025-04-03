from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os
location=os.getcwd()

def chrome_setup():
    driver=webdriver.Chrome()
    ops=webdriver.ChromeOptions()
    preferences={"download.default_directory":location,"plugins.always_open_pdf_externally":True}
    ops.add_experimental_option("prefs",preferences)
    return driver
driver = chrome_setup()
driver.get("https://examplefile.com/document/pdf/1-mb-pdf")
driver.maximize_window()
button=driver.find_element(By.XPATH,"//a[@title='1 MB PDF Download']")
driver.execute_script("arguments[0].scrollIntoView();",button)
value=driver.execute_script("return window.pageYOffset;")
button.click()