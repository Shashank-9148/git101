import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def setUpModule(): #will be executed before executing any class or  any method present in the test class
    print("setup module")

def tearDownModule(): #will be executed after completing everything present in the python module
    print("teardown module")

class Apptesting(unittest.TestCase):
    @classmethod
    def setUp(self): #execute everytime when the class is started
        print("This is login test")

    @classmethod
    def tearDown(self):  #execute every time when the class is closed
        print("This is logout test")

    @classmethod
    def setUpClass(cls): #execute once when the class started
        print("Application started")

    @classmethod
    def tearDownClass(cls):  #execute once when the class is closed
        print("Application closed")

    def testsearch(self):
        print("This is search test")

    def test_advanced_search(self):
        print("This is advanced search test")

    def test_prepaid_recharge(self):
        print("This is prepaid recharge test")

    def test_postpaid_recharge(self):
        print("This is postpaid recharge test")


if __name__=="__main__":
    unittest.main()