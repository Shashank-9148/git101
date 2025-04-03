from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
#mywait = WebDriverWait(driver,10)#basic syntax
mywait = WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException])
ed=driver.find_element(By.NAME,"q")
ed.send_keys("amazon")
ed.submit()
search_title = mywait.until(EC.presence_of_element_located((By.XPATH,"//span[text()='Shop online at Amazon India']")))
search_title.click()