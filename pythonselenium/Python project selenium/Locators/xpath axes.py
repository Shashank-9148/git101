from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()
#using self
#text_use=driver.find_element(By.XPATH,"//*[contains(text(),'Techno Electric&Eng')]/self::a").text
#print(text_use)

#using parent
#text_use=driver.find_element(By.XPATH,"//a[contains(text(),'Techno Electric&Eng')]/parent::td").text
#print(text_use)

#using child
#child=driver.find_elements(By.XPATH,"//a[contains(text(),'Techno Electric&Eng')]/ancestor::tr/child::td")
#print(len(child))

#using ancestor
#text_use=driver.find_element(By.XPATH,"//a[contains(text(),'Techno Electric&Eng')]/ancestor::tr").text
#print(text_use)

#using descendant
#descendants=driver.find_elements(By.XPATH,"//a[contains(text(),'Techno Electric&Eng')]/ancestor::tr/descendant::*")
#print("Number of Descendants :",len(descendants))

#using following
#following=driver.find_elements(By.XPATH,"//a[contains(text(),'Techno Electric&Eng')]/ancestor::tr/following::*")
#print("Number of descendants :",len(following))

#using following-siblings
#following_siblings=driver.find_elements(By.XPATH,"//a[contains(text(),'Techno Electric&Eng')]/ancestor::tr/following-sibling::*")
#print("Number of descendants :",len(following_siblings))

#using preceding
#preceding=driver.find_elements(By.XPATH,"//a[contains(text(),'Techno Electric&Eng')]/ancestor::tr/preceding::tr")
#print("Number of descendants :",len(preceding))

#using preceding-sibling
preceding_sibling=driver.find_elements(By.XPATH,"//a[contains(text(),'Techno Electric&Eng')]/ancestor::tr/preceding-sibling::tr")
print("Number of descendants :",len(preceding_sibling))

driver.close()