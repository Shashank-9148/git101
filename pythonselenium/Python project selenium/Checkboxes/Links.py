
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

""""#click action on links
driver.find_element(By.LINK_TEXT,"Digital downloads").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Digital downloa").click()
"""
#find number of links in the page
no_of_links=driver.find_elements(By.TAG_NAME,"A")
print(len(no_of_links))
#below is to print the link names
for link in no_of_links:
    print(link.text)

driver.close()