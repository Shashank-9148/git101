from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://practice.expandtesting.com/dropdown")
driver.maximize_window()
drpcountry=Select(driver.find_element(By.XPATH,"//*[@id='country']"))

#select option from the dropdown
#drpcountry.select_by_visible_text("Iceland")
#drpcountry.select_by_index("15")
#drpcountry.select_by_value("AU")

#capture all the options and print them
alloptions = drpcountry.options
print("number of options :",len(alloptions))
#for opt in alloptions:
#    print(opt.text)

#select option from dropdown  without using built in method
for opt in alloptions:
    if opt.text == "India":
        opt.click()
        break