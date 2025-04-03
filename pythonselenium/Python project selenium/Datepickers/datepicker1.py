from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)
month = "August"
year = "2019"
date = "27"
#driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("26/07/2001")
driver.find_element(By.XPATH,"//*[@id='datepicker']").click()
#below code is to click month and date
while True:
    mnt = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yer = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
    if mnt == month and yer == year:
        break
#below code is to click the next or backward arrrow mark
    else:
        driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[1]/span").click()

#below code to click the date picker
dte=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//tbody/tr/td/a")
for d in dte:
    if d.text == date:
        d.click()
        break