import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://app.bamboohr.com/login/")
driver.maximize_window()
windowid=driver.current_window_handle
print('window id :',windowid) #window id : 3F087798D2DAC6A0BA5585EE48C70CA7

driver.find_element(By.XPATH,"//div[@class='front']//ba-icon[@name='fab-bamboohr-logo-115x17']").click()
windowIds=driver.window_handles

#below code prints the ids of parent and child
parentwindowid = windowIds[0] #A56A89455D2CCA763970B1C9F6D707D7
childwindowid = windowIds[1]  #AD84A477F74BDC0ABD12D298BE90D955
print(parentwindowid,childwindowid)

#below code prints the title of the parent and child window
"""driver.switch_to.window(parentwindowid)
print("title of parent window:",driver.title) #Login Page for BambooHR Users

driver.switch_to.window(childwindowid)
print("title of the child window:",driver.title) #The Complete HR Software for People, Payroll & Benefits

#below code also prints the title of the parent and child window
for ids in windowIds:
    driver.switch_to.window(ids)
    print(driver.title)"""

#below code closes the web page window according to title
"""for ids in windowIds:
    driver.switch_to.window(ids)
    if driver.title == "BambooHR: The Complete HR Software for People, Payroll & Benefits":
        time.sleep(3)
        driver.close()
"""
for ids in windowIds:
    if driver.switch_to.window(ids):
        if driver.title == "BambooHR: The Complete HR Software for People, Payroll & Benefits":
            driver.close()