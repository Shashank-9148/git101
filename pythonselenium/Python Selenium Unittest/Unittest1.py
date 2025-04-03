import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class searchEngineTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_google(self):
        self.driver.get("https://www.google.com/")
        print("Title of this page :",self.driver.title)

    def test_bing(self):
        self.driver.get("https://www.bing.com/")
        print("Title of this page :",self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
