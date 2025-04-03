from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.techlistic.com/2017/02/automate-demo-web-table-with-selenium.html")
driver.maximize_window()

#col=driver.find_elements(By.XPATH,"//thead//th")
#print(len(col))

#for r in range(1,len(col)+1):
 #   name = driver.find_element(By.XPATH,"//thead//th["+str(r)+"]").text
  #  print(name.title())

row=driver.find_elements(By.XPATH,"//table[@class='tsc_table_s13']//td")
print(len(row))

for c in range(1,len(row)+1):
    num = driver.find_element(By.XPATH,"//table[@class='tsc_table_s13']//tr["+str(c)+"]").text
    print(num.title())

driver.close()


