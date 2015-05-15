# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest

links_landing_titles = {
    "PRICING" : "Pricing",
    "ENTERPRISE" : "Enterprise",
    "DOCS" : "Docs",
    "PLATFORMS" : "Platforms",
    }

class SauceLabsHeaders(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://saucelabs.com/"
        self.verificationErrors = []
    
    def test_sauce_labs_headers(self):
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
