from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import os
location=os.getcwd()

def firefox_setup():
    driver=webdriver.Firefox()
    #serv_obj=Service("C:\Drivers\geckodriver-v0.35.0-win64 extracted")
    #ops=webdriver.FirefoxOptions()
    #driver = webdriver.Firefox(service=serv_obj, options=ops)
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk","application/msword")
    ops.set_preference("browser.download.manager.showWhenStarting",False)
    ops.set_preference("browser.download.folderList",1)
    ops.set_preference("browser.download.dir",location)
    return driver
driver=firefox_setup()
driver.get("https://filesamples.com/formats/doc")
driver.maximize_window()
driver.find_element(By.XPATH,"//div[@class='output']//div[1]//a[1]").click()