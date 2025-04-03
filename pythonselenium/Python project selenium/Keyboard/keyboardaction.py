from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://text-compare.com/")
driver.maximize_window()
act=ActionChains(driver)
driver.implicitly_wait(10)

input1=driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
input2=driver.find_element(By.XPATH,"//textarea[@id='inputText2']")
input1.send_keys("Welcome to Home")

#input1 -->ctrl+A select text
#act.key_down(Keys.CONTROL)
#act.send_keys("a")
#act.key_up(Keys.CONTROL)
#act.perform()
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

#input1-->ctrl+C copy text
#act.key_down(Keys.CONTROL)
#act.send_keys("c")
#act.key_up(Keys.CONTROL)
#act.perform()
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

#press tab key to navigate to input2
#act.send_keys(Keys.TAB)
#act.perform()
act.send_keys(Keys.TAB).perform()

#input2-->ctrl+v paste text
#act.key_down(Keys.CONTROL)
#act.send_keys("v")
#act.key_up(Keys.CONTROL)
#act.perform()
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()



#input2--> ctrl+V paste the text
act.key_down(Keys.CONTROL)
act.send_keys("v")
act.key_up(Keys.CONTROL)
act.perform()