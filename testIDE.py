# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest

class SeIdePy(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)

    def test_se_ide_py(self):
        driver = self.driver

        driver.get("https://www.google.com.ua/")
        driver.find_element_by_id("lst-ib").click() #search_field
        driver.find_element_by_id("lst-ib").clear()
        driver.find_element_by_id("lst-ib").send_keys("Selenium IDE export to C#")
        driver.find_element_by_id("_fZl").click() #search_button

        #Checking the found element
        self.assertIn("Selenium IDE Export to C#" , driver.find_element_by_xpath("//*[@id='rso']/div/div/div[4]/div/div/h3/a").text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()