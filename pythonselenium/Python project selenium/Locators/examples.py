from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from  selenium.webdriver.support.select import Select
#sample code to run dummy visa website
driver = webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
driver.find_element(By.XPATH,"//*[@id='travname']").send_keys("Shashank")
driver.find_element(By.XPATH,"//input[@id='travlastname']").send_keys("L")
driver.find_element(By.XPATH,"//input[@id='dob']").click()

month=Select(driver.find_element(By.XPATH,"//select[@data-handler='selectMonth']"))
month.select_by_visible_text("Jul")
year=Select(driver.find_element(By.XPATH,"//select[@data-handler='selectYear']"))
year.select_by_value("2001")
dates = driver.find_elements(By.XPATH,"//div[@id='ui-datepicker-div']//table/tbody/tr/td/a")
for date in dates:
    if date.text == "26":
        date.click()
        break
driver.find_element(By.XPATH,"//*[@id='sex_1']").click()
driver.find_element(By.XPATH,"//*[@id='traveltype_1']").click()
driver.find_element(By.XPATH,"//*[@id='fromcity']").send_keys('Tiptur')
driver.find_element(By.XPATH,"//*[@id='tocity']").send_keys('KSR Bengaluru')
driver.find_element(By.ID,"deliverymethod_1").click()
driver.find_element(By.ID,"billname").send_keys("Deepak")
driver.find_element(By.ID,"billing_phone").send_keys("7892119045")
driver.find_element(By.ID,"billing_email").send_keys("deepakshetty1273@gmail.com")
driver.find_element(By.ID,"billing_address_1").send_keys("Near Shadaksharamutt,Honnavalli Main road")
driver.find_element(By.ID,"billing_address_2").send_keys("No #43")
driver.find_element(By.ID,"billing_city").send_keys("Tiptur")
driver.find_element(By.ID,"billing_postcode").send_keys("572201")
