from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

min_slider=driver.find_element(By.XPATH,"//div[@id='slider-range']//span[1]")
max_slider=driver.find_element(By.XPATH,"//*[@id='slider-range']/span[2]")

print("Location of sliders before moving..")
print(min_slider.location) #{'x': 59, 'y': 288}
print(max_slider.location) #{'x': 612, 'y': 288}

act_chain= ActionChains(driver)
act_chain.drag_and_drop_by_offset(min_slider,110,288).perform()
act_chain.drag_and_drop_by_offset(max_slider,-50,288).perform()

print("Location of sliders after moving.....")
print(min_slider.location)
print(max_slider.location)