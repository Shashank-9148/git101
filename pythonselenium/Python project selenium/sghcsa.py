from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Initialize ChromeDriver properly
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service, options=options)

# Open Google to test
driver.get("https://www.google.com")
print(driver.title)

# Close browser
driver.quit()

