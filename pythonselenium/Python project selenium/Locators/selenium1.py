#open web browser(chrome/edge/firefox)
#open url "www.orangehrm.com"
#Enter username(Admin)
#Enter password(admin123)
#click on login
#capture title of the homepage(actual title)
#verify title of the page (orangeHRM)
#close browser


"""from selenium import webdriver
driver = webdriver.Chrome(r"C:\Drivers\chrome extracted\chromedriver-win64\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com")
driver.find_element_by_name("username").send_keys("Admin")
driver.find_element_by_name("oxd-input oxd-input--active")
driver.find_element_by_class_name("oxd-button oxd-button--medium oxd-button--main orangehrm-login-button").click()
act_title = driver.title
exp_title = "OrangeHRM"
if act_title == exp_title:
    print("Login test passed")
else:
    print("login test failed")

driver.close()"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#serv_obj = Service(r"C:\Drivers\chrome extracted\chromedriver-win64\chromedriver.exe")
#driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com")
driver.find_element(By.XPATH).send_keys("Admin")
driver.find_element(By.XPATH,).send_keys("admin123")
driver.find_element(By.XPATH,).click()

act_title = driver.title
exp_title = "OrangeHRM"

if act_title == exp_title:
    print('Login test passed')
else:
    print('Login test failed')

#driver.close()