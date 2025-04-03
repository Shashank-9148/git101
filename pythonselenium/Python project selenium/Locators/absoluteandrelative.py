from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

"""#using absolute Xpath
driver = webdriver.Chrome()
driver.get("http://www.automationpractice.pl")
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/header[1]/div[3]/div[1]/div[1]/div[2]/form[1]/input[4]").send_keys("T-shirts")
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/header[1]/div[3]/div[1]/div[1]/div[2]/form[1]/button[1]").click()
driver.maximize_window()

#using relative Xpath
driver.find_element(By.XPATH,"//input[@id='search_query_top']").send_keys("shirts")
driver.find_element(By.XPATH,"//button[@name='submit_search']").click()
driver.maximize_window()"""

