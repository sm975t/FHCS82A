# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class SauceLabsLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://saucelabs.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_sauce_labs_login(self):
        driver = self.driver
        driver.get(self.base_url)

        driver.find_element_by_xpath("//li/a[@class='hamburger']/../following-sibling::li/a").click()

        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("???")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("???")
        driver.find_element_by_id("submit").click()
        try: self.assertEqual("Sauce Labs | Account", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
