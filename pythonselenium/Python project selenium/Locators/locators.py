"""#program to access linktext,partial linktext,name and id
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.find_element(By.ID,"small-searchterms").send_keys("HP Spectre XT Pro UltraBook") #ID locator
driver.find_element(By.NAME,"q").send_keys("Apple icam") #Name locator
driver.maximize_window() #to maximize the window
driver.find_element(By.LINK_TEXT,"Register").click() #Link text
driver.find_element(By.PARTIAL_LINK_TEXT,"Reg").click() #Partial link  ttext
driver.find_element(By.LINK_TEXT,"Log in").click()

driver.quit()
driver.close()
"""


#program to access with classname or tagname
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("http://www.automationpractice.pl/")
sliders = driver.find_elements(By.CLASS_NAME,"homeslider-container") #to access if one or more classnames
print(len(sliders))
links = driver.find_elements(By.TAG_NAME,"li,a") #to access this one or more tag names
print(len(links))
driver.find_element(By.ID,"search_query_top").send_keys("Printed Summer Dress")
driver.maximize_window()
#driver.close()

