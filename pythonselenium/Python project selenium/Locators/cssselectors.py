#syntax of tag id(tagname#value of id)
#syntax of tag class(tagname.value of class)
#syntax of tag attribute(tagname[attribute=value]
#syntax of tag class attribute(tagname.valueofclass[attribute=value])

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

"""driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc@gmail.com") #using tag id
driver.find_element(By.CSS_SELECTOR,"#email").send_keys("abc@gmail.com") #using tag id
driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("abc@gmail.com") #using valueofclass
driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys("abc@gmail.com") #using value of class
driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").send_keys("abc@123") #using tag attribute
driver.find_element(By.CSS_SELECTOR,"[data-testid=royal_email]").send_keys("shashanklokesh2001@gmail.com")
driver.find_element(By.CSS_SELECTOR,".inputtext[data-testid=royal_email]").send_keys("shashank@gmail.com") #using tag class attribute
driver.find_element(By.CSS_SELECTOR,".inputtext[data-testid=royal_pass]").send_keys(123456)
driver.find_element(By.CSS_SELECTOR,"[data-testid=royal_login_button]").click()
driver.maximize_window()


#this code is for udemy
driver = webdriver.Chrome()
driver.get("https://partnerportal.udemy.com")
driver.find_element(By.CSS_SELECTOR,"#UserName").send_keys("shashanklokesh2001")
driver.find_element(By.CSS_SELECTOR,"#Password").send_keys("1234")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,".btn btn-primary btnOrange btnLogin loginBtn btn-lg").click()
"""

