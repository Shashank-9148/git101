#general syntax of contains //tagname[contains(@id,value)]
#general syntax of starts with //tagname[startswith(@id,value)]
#general syntax of or,and //tagname[@id=value or @id=value]
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#using contains,startswith,or functions
driver = webdriver.Chrome()
driver.get("http://www.automationpractice.pl/")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[contains(@id,'search_query_top')]").send_keys('shirts')
driver.find_element(By.XPATH,"//*[starts-with(@name,'submit_')]").click()
driver.find_element(By.XPATH,"//*[@id='search_query_top' or @name='search']").send_keys('tshirts')
driver.find_element(By.XPATH,"//a[text()='Women']").click()
