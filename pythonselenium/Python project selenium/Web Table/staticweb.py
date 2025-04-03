from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#count number of rows and columns
noofrows=driver.find_elements(By.XPATH,"//*[@name='BookTable']//tr")
print(len(noofrows))
noofcolumns=driver.find_elements(By.XPATH,"//*[@name='BookTable']//th")
print(len(noofcolumns))
"""
#read specific row and column data
ec=driver.find_element(By.XPATH,"//*[@name='BookTable']//tr[5]/td[3]").text
print(ec)

#read all the rows and columns data
for r in range(2,len(noofrows)+1):
    for c in range(1,len(noofcolumns)+1):
        ec = driver.find_element(By.XPATH, "//*[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(ec,end="   ")
    print()"""

#read data based on condition(list booksname whose author is mukesh)
for r in range(2,len(noofrows)+1):
    authors=driver.find_element(By.XPATH,"//*[@name='BookTable']//tr["+str(r)+"]/td[2]").text
    if authors == "Amit":
        bookname=driver.find_element(By.XPATH,"//*[@name='BookTable']//tr["+str(r)+"]/td[1]").text
        price=driver.find_element(By.XPATH,"//*[@name='BookTable']//tr["+str(r)+"]/td[4]").text
        print(bookname," : ",authors," : ",price)

driver.close()
