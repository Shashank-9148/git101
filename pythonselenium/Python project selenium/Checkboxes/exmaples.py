from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.automationtesting.co.uk/dropdown.html")
driver.maximize_window()
"""drpcountry=Select(driver.find_element(By.XPATH,"//select[@id='cars']"))
#drpcountry.select_by_visible_text('Volkswagen')
alloptions = drpcountry.options
for option in alloptions:
#  print(len(alloptions))
 for options in alloptions:
    if option.text == 'Audi':
        option.click()
        break"""

ed=driver.find_elements(By.NAME,"demo-priority")
print(len(ed))
for links in ed:
    links.click()
