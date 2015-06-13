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
    'error_container' : 'p.error-text',
}

in_use_email_error = '''Sorry, that email address is already in use. If you're having trouble signing up or want to add more users to your account, please click here.'''
in_use_username_error = '''Sorry, that username is taken.\nPlease choose a different username.'''

class Signup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = 'https://saucelabs.com/'
        self.verificationErrors = []

    def signup(self,
               first_name = 'SauceLabs',
               last_name = 'Automation',
               email = helpers.generate_email(helpers.generate_date_stamp()),
               company = 'Foothill CS82A',
               company_size = '11-50',
               username = helpers.generate_date_stamp()[9:],
               password1='SauceLabs2015',
               password2='SauceLabs2015',
              ):
        driver = self.driver
        driver.get(self.base_url)

        # Navigate to FREE TRIAL page from home page's header
        driver.find_element_by_css_selector(locators['free_trial']).click()

        # First Name and Last Name
        driver.find_element_by_id(locators['first_name']).send_keys(first_name)
        driver.find_element_by_id(locators['last_name']).send_keys(last_name)

        # Email
        driver.find_element_by_id(locators['email']).send_keys(email)

        # Company 
        driver.find_element_by_id(locators['company']).send_keys(company)

        # Company Size
        Select(driver.find_element_by_id(locators['company_size'])).select_by_visible_text(company_size)

        # Username value has to already exist
        driver.find_element_by_id(locators['username']).send_keys(username)

        # Password values have to match
        driver.find_element_by_id(locators['password']).send_keys(password1)
        driver.find_element_by_id(locators['password_confirm']).send_keys(password2)

        # Submit the form
        driver.find_element_by_id(locators['submit_button']).click()

        return driver
    
    def test_signup_happy_path(self):
        driver = self.driver
        driver.get(self.base_url)

        # Sign up with all default values
        driver = self.signup()

        # Verify that the new user has an Account page now
        try: self.assertEqual('Sauce Labs | Account', driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
   
    def test_signup_already_used_email_neg(self):

        # Sign up with all default values except for already-existing email
        driver = self.signup(email='saucelabs.automation@gmail.com')

        # Verify that the appropriate error message has been issued 
        selector = driver.find_element_by_css_selector(locators['error_container'])
        try: self.assertEqual(in_use_email_error, selector.text)
        except AssertionError as e: self.verificationErrors.append(str(e))
    
    def test_signup_already_used_username_neg(self):

        # Sign up with all default values except for already-existing username
        driver = self.signup(username='sbssgm')

        # Verify that the appropriate error message has been issued 
        selector = driver.find_element_by_css_selector(locators['error_container'])
        try: self.assertEqual(in_use_username_error, selector.text)
        except AssertionError as e: self.verificationErrors.append(str(e))
   
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == '__main__':
    unittest.main()
