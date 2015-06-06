# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest

links_landing_titles = {
    "Basic Skills Initiative" : "Basic Skills Initiative",
    "Bio/Health Division" : "Biological, Health and Environmental",
    "Biology Department" : "Biology.*Home",
    "Bookstore" : "Bookstore",
    "Business, Computer Science and Applied Technologies" : "Business/Computer Systems",
    "Business Department" : "Business.*Home",
    "Japanese Department " : "Japanese",
    "Journalism and Mass Communication" : "Journalism",
    }

class DeAnzaAtoZ(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://deanza.edu/directory/dir-az.html"
        self.verificationErrors = []
    
    def test_deanza_a_to_z_links(self):
        driver = self.driver

        for link in links_landing_titles:
            driver.get(self.base_url)
            driver.find_element_by_link_text(link).click()
            expected_title = links_landing_titles[link]
            try: self.assertRegexpMatches(driver.title, expected_title)
            except AssertionError as e: self.verificationErrors.append(str(e))

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
