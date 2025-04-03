from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/")

#capture cookies from the browser
cookies=driver.get_cookies()
print("size of cookies:",len(cookies))

#print details of all cookies
for c in cookies:
    print(c)
    print(c.get('name'),":",c.get('value'))

#print cookie to the browser
driver.add_cookie({"name":"my cookie","value" : "1234"})
cookies = driver.get_cookies()
print("size of cookies after adding new one:",len(cookies))

for c in cookies:
    print(c)
    print(c.get("name") ,":", c.get("value"))

#delete specific cookie from the browser
driver.delete_cookie("my cookie")
cookies=driver.get_cookies()
print("size of cookies after deleted one :",len(cookies))

#delete all the cookies
driver.delete_all_cookies()
cookies = driver.get_cookies()
print("After deletion of all cookies :",len(cookies))
