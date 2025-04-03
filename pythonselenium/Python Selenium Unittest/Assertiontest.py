import unittest
from selenium import webdriver

"""class Test(unittest.TestCase):
    def testcase(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.google.com/")
        titleofpage=self.driver.title

        self.assertEqual("Google",titleofpage,"Page not found")
        self.assertNotEqual("Google123", titleofpage,"Page error")

if __name__=="__main__":
    unittest.main()"""


class Test(unittest.TestCase):
  def testcase(self):
    self.driver = webdriver.Chrome()
    self.driver.get("https://www.google.com/")
    titleofbrowser=self.driver.title

    #self.assertTrue(titleofbrowser=="Google")
    self.assertFalse(titleofbrowser=="Google1234")

if __name__=="__main__":
    unittest.main()