# File:     Manager.py
# Type:     Python (.py) file
# Author:   Maxximillion Thomas
# Date:     Jul 25, 2024
# Desc.:    Perform tests on a dummy banking website to simulate adding clients and performing balance enquiries

# ==========  IMPORTS  ==========
# Import modules to allow Chrome browsing through Selenium
#import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeS
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager as ChromeDM

#from unittest import skipIf     # Temporary

# ==========  CLASS  ==========
class Manager:
    # ==========  OBJECT CONSTRUCTION  ==========
    def __init__(self, driver):
        self.browser = driver

    # ==========  ADD NEW CUSTOMER PAGE   ==========
    def log_in(self):
        """Log into the guru banking website."""
        self.browser.get("https://demo.guru99.com/V4/")
        self.browser.find_element(By.NAME, "uid").send_keys("mngr629176")
        self.browser.find_element(By.NAME, "password").send_keys("mUqazev")
        self.browser.find_element(By.NAME, "btnLogin").click()

    def add_customer_page(self):
        """Navigate to the Add New Customer page."""
        self.browser.find_element(By.XPATH, "//a[normalize-space()='New Customer']").click()

    # ==========  ADD CUSTOMER   ==========
    def add_customer(self, name, gender, dob, address, city, state, pin, number, email, password):
        """Add a new customer to the database."""
        self.log_in()
        self.add_customer_page()

        # Use the arguments as data for the customer add page
        self.browser.find_element(By.NAME, "name").send_keys(name)
        if gender == "m":
            self.browser.find_element(By.XPATH, "//input[@value='m']").click()
        else:
            self.browser.find_element(By.XPATH, "//input[@value='f']").click()
        self.browser.find_element(By.NAME, "dob").send_keys(dob) # 4-tab-2-2
        self.browser.find_element(By.NAME, "addr").send_keys(address)
        self.browser.find_element(By.NAME, "city").send_keys(city)
        self.browser.find_element(By.NAME, "state").send_keys(state)
        self.browser.find_element(By.NAME, "pinno").send_keys(pin)
        self.browser.find_element(By.NAME, "telephoneno").send_keys(number)
        self.browser.find_element(By.NAME, "emailid").send_keys(email)
        self.browser.find_element(By.NAME, "password").send_keys(password)
        self.browser.find_element(By.NAME, "sub").click()

        # Validation data
        special_characters = ["`","~","!","@","#","$","%","^","&","*","(",")",
                              "-","_","=","+",r"\\","|",";",":",r"\"",",","<",
                              ".",">","/","?"]

        # Argument validation:  name
        # Cannot be empty
        if len(name) == 0:
            raise ValueError('Customer name must not be blank')
        # Cannot be numeric
        for c in name:
            if c.isdigit():
                raise TypeError('Numbers are not allowed')
            # Cannot have special characters
            if c in special_characters:
                raise TypeError('Special characters are not allowed')
        # Cannot have first character as blank space
        if name[0] == "":
            raise ValueError('First character can not have space')

        # Argument validation:  gender
        # Cannot have length greater than 1
        pass
        # Cannot be numeric
        pass
        # Cannot have special characters
        pass
        # Must be equal to 'm' or 'f'
        pass

        # Argument validation:  name
        # Cannot be empty
        pass
        # Cannot be numeric
        pass
        # Cannot have special characters
        pass
        # Cannot have first character as blank space
        pass

        # Argument validation:  address
        # Cannot be empty
        pass
        # Cannot be numeric
        pass
        # Cannot have special characters
        pass
        # Cannot have first character as blank space
        pass

        # Argument validation:  city
        # Cannot be empty
        pass
        # Cannot be numeric
        pass
        # Cannot have special characters
        pass
        # Cannot have first character as blank space
        pass

        # Argument validation:  state
        # Cannot be empty
        pass
        # Cannot be numeric
        pass
        # Cannot have special characters
        pass
        # Cannot have first character as blank space
        pass

        # Argument validation:  pin
        # Cannot be empty
        pass
        # Cannot be numeric
        pass
        # Cannot have special characters
        pass
        # Cannot have first character as blank space
        pass

        # Argument validation:  number
        # Cannot be empty
        pass
        # Cannot be numeric
        pass
        # Cannot have special characters
        pass
        # Cannot have first character as blank space
        pass

        # Argument validation:  email
        # Cannot be empty
        pass
        # Cannot be numeric
        pass
        # Cannot have special characters
        pass
        # Cannot have first character as blank space
        pass

        # Argument validation:  password
        # Cannot be empty
        if len(password) == 0:
            raise ValueError('Customer name must not be blank')
        # Cannot be numeric
        pass
        # Cannot have special characters
        pass
        # Cannot have first character as blank space
        pass

    # ==========  BALANCE ENQUIRY PAGE   ==========
    pass

    # ==========  BALANCE ENQUIRY   ==========
    pass












# ==========  EXECUTION  ==========
if __name__ == '__main__':
    browser = webdriver.Chrome(service=ChromeS(ChromeDM().install()))
    browser.maximize_window()
    sleep(2)
    manager = Manager(browser)
    manager.add_customer("a", "m", 19500101, "a",
                    "a", "a", "123456", "1234567890",
                    "a@gmail.com", "password")


