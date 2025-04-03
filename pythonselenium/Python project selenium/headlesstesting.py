from selenium import webdriver
from selenium.webdriver.common.service import Service

"""def headless_chrome():
    ops = webdriver.ChromeOptions()
    ops.headless = True
    driver = webdriver.Chrome(options=ops)
    driver.implicitly_wait(10)
    return driver

driver=headless_chrome()
driver.get("https://demo.nopcommerce.com/")
print(driver.title)
print(driver.current_url)
driver.close()"""

driver=webdriver.Firefox()
driver.get("https://demo.nopcommerce.com/")