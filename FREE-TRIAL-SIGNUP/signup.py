# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import unittest, time, re
import helpers

locators = {
    'free_trial' : '#signup > a',
    'first_name' : 'first_name',   
    'last_name' : 'last_name',   
    'email' : 'email',   
    'company' : 'company',   
    'company_size' : 'company-size',   
    'username' : 'username',   
    'password' : 'password',   
    'password_confirm' : 'password_confirm',   
    'submit_button' : 'submit-button',
}

class Signup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = 'https://saucelabs.com/'
        self.verificationErrors = []
    
    def test_signup_happy_path(self):
        driver = self.driver
        driver.get(self.base_url)

        # Navigate to FREE TRIAL page from home page's header
        driver.find_element_by_css_selector(locators['free_trial']).click()

        # First Name and Last Name
        driver.find_element_by_id(locators['first_name']).send_keys('SauceLabs')
        driver.find_element_by_id(locators['last_name']).send_keys('Automation')

        # Email value has to be unique!
        unique_date_stamp = helpers.generate_date_stamp()
        email = helpers.generate_email(date_stamp = unique_date_stamp)
        driver.find_element_by_id(locators['email']).send_keys(email)

        # Company 
        driver.find_element_by_id(locators['company']).send_keys('Foothill CS82A')

        # Company Size
        Select(driver.find_element_by_id(locators['company_size'])).select_by_visible_text('11-50')

        # Username value has to be unique
        # Use the hhmmss-mmmmmm portion of the unique date stamp generated earlier
        driver.find_element_by_id(locators['username']).send_keys(unique_date_stamp[9:])

        # Password values have to match
        driver.find_element_by_id(locators['password']).send_keys('SauceLabs2015')
        driver.find_element_by_id(locators['password_confirm']).send_keys('SauceLabs2015')

        # Submit the form
        driver.find_element_by_id(locators['submit_button']).click()

        # Verify that the new user has an Account page now
        try: self.assertEqual('Sauce Labs | Account', driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == '__main__':
    unittest.main()
