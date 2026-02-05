# File:     test_manager.py
# Type:     Python (.py) file
# Authors:  Kyle Angeles, Mathuran Chandramohan, Pratig Thapa,  Maxximillion Thomas
# Date:     Aug 7, 2025
# Desc.:    Perform tests on a dummy banking website to simulate Manager privileges

# ==========  IMPORTS  ==========
# TESTING
import unittest

# WEBDRIVER
from app.manager import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeS
from webdriver_manager.chrome import ChromeDriverManager as ChromeDM

# ==========  CLASS  ==========
class TestManager(unittest.TestCase):
    # ==========  CONSTANTS  ==========
    CUSTOMER_ID = "25208"
    CUSTOMER_ID_DELETE = "94979"
    ACCOUNT_ID_DELETE = "175680"

    # ==========  CLASS METHODS  ==========
    @classmethod
    def setUpClass(cls):
        """Initialize the Chrome browser with the Selenium extension"""
        cls.browser = webdriver.Chrome(service=ChromeS(ChromeDM().install()))
        cls.browser.maximize_window()
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        """Close the Chrome browser"""
        cls.browser.quit()
        print('tearDownClass')

    def setUp(self):
        """Inform the user which test case is being tested"""
        self.m = Manager(self.browser)
        self.m.login_manager()
        print(f'setUp:\t\t\t{self._testMethodName}')

    def tearDown(self):
        """Provide a short description of the test case that was tested"""
        # Dismiss any leftover alerts
        try:
            alert = self.browser.switch_to.alert
            alert.accept()
        except:
            pass
        print(f'End of test:\t{self.shortDescription()}')

    # =======================================
    # ==========  1. NEW CUSTOMER  ==========
    # =======================================
    # Verify name field
    def test_NC1(self):
        """Name cannot be empty"""
        self.assertEqual("Customer name must not be blank", self.m.add_customer("", "m", "2025-01-01", "address", "city", "state", "123456", "1234567890", "email@gmail.com", "password"))
        self.assertEqual("Customer name must not be blank", self.m.add_customer(Keys.TAB, "m", "2025-01-01", "address", "city", "state", "123456","1234567890", "email@gmail.com", "password"))

    def test_NC2(self):
        """Name cannot be numeric"""
        self.assertEqual("Numbers are not allowed", self.m.add_customer("1234", "m", "2025-01-01", "address", "city", "state", "123456", "1234567890", "email@gmail.com", "password"))
        self.assertEqual("Numbers are not allowed", self.m.add_customer("name123", "m", "2025-01-01", "address", "city", "state", "123456", "1234567890", "email@gmail.com", "password"))

    def test_NC3(self):
        """Name cannot have special characters"""
        self.assertEqual("Special characters are not allowed", self.m.add_customer("name!@#", "m", "2025-01-01", "address", "city", "state", "123456", "1234567890", "email@gmail.com", "password"))
        self.assertEqual("Special characters are not allowed", self.m.add_customer("!@#", "m", "2025-01-01", "address", "city", "state", "123456", "1234567890", "email@gmail.com", "password"))

    def test_NC4(self):
        """Name cannot have first character as blank space"""
        self.assertEqual("First character can not have space", self.m.add_customer(" name", "m", "2025-01-01", "address", "city", "state", "123456", "1234567890", "email@gmail.com", "password"))

    # Verify address field
    def test_NC5(self):
        """Address cannot be empty"""
        self.assertEqual("Address Field must not be blank", self.m.add_customer("name", "m", "2025-01-01", "", "city", "state", "123456", "1234567890", "email@gmail.com", "password"))
        self.assertEqual("Address Field must not be blank", self.m.add_customer("name", "m", "2025-01-01", Keys.TAB, "city", "state", "123456", "1234567890", "email@gmail.com", "password"))

    def test_NC6(self):
        """Address cannot have first blank space"""
        self.assertEqual("First character can not have space", self.m.add_customer("name", "m", "2025-01-01", " address", "city", "state", "123456", "1234567890", "email@gmail.com", "password"))

    # Verify city field
    def test_NC7(self):
        """City cannot be empty"""
        self.assertEqual("City Field must not be blank", self.m.add_customer("name", "m", "2025-01-01", "address", "", "state", "123456", "1234567890", "email@gmail.com", "password"))
        self.assertEqual("City Field must not be blank", self.m.add_customer("name", "m", "2025-01-01", "address", Keys.TAB, "state", "123456", "1234567890", "email@gmail.com", "password"))

    def test_NC8(self):
        """City cannot be numeric"""
        self.assertEqual("Numbers are not allowed", self.m.add_customer("name", "m", "2025-01-01", "address", "1234", "state", "123456", "1234567890", "email@gmail.com", "password"))
        self.assertEqual("Numbers are not allowed", self.m.add_customer("name", "m", "2025-01-01", "address", "city123", "state", "123456", "1234567890", "email@gmail.com", "password"))

    def test_NC9(self):
        """City cannot have special character"""
        self.assertEqual("Special characters are not allowed", self.m.add_customer("name", "m", "2025-01-01", "address", "City!@#", "state", "123456", "1234567890", "email@gmail.com", "password"))
        self.assertEqual("Special characters are not allowed", self.m.add_customer("name", "m", "2025-01-01", "address", "!@#", "state", "123456", "1234567890", "email@gmail.com", "password"))

    def test_NC10(self):
        """City cannot have first blank space"""
        self.assertEqual("First character can not have space", self.m.add_customer("name", "m", "2025-01-01", "address", " city", "state", "123456", "1234567890", "email@gmail.com", "password"))

    # Verify state field
    def test_NC11(self):
        """State cannot be empty"""
        self.assertEqual("State must not be blank", self.m.add_customer("name", "m", "2025-01-01", "address", "city", "", "123456", "1234567890", "email@gmail.com", "password"))
        self.assertEqual("State must not be blank", self.m.add_customer("name", "m", "2025-01-01", "address", "city", Keys.TAB, "123456", "1234567890", "email@gmail.com", "password"))

    def test_NC12(self):
        """State cannot be numeric"""
        self.assertEqual("Numbers are not allowed", self.m.add_customer("name", "m", "2025-01-01", "address", "city", "1234", "123456", "1234567890", "email@gmail.com", "password"))
        self.assertEqual("Numbers are not allowed", self.m.add_customer("name", "m", "2025-01-01", "address", "city", "State123", "123456", "1234567890", "email@gmail.com", "password"))

    def test_NC13(self):
        """State cannot have special character"""
        self.assertEqual("Special characters are not allowed", self.m.add_customer("name", "m", "2025-01-01", "address", "city", "State!@#", "123456", "1234567890", "email@gmail.com", "password"))
        self.assertEqual("Special characters are not allowed", self.m.add_customer("name", "m", "2025-01-01", "address", "city", "!@#", "123456", "1234567890", "email@gmail.com", "password"))

    def test_NC14(self):
        """State cannot have first blank space"""
        self.assertEqual("First character can not have space", self.m.add_customer("name", "m", "2025-01-01", "address", "city", " state", "123456", "1234567890", "email@gmail.com", "password"))

    # Verify pin field
    def test_NC15(self):
        """PIN must be numeric"""
        self.assertEqual("Characters are not allowed", self.m.add_customer("name", "m", "2025-01-01", "address", "city", "state", "PIN", "1234567890", "email@gmail.com", "password"))
        self.assertEqual("Characters are not allowed", self.m.add_customer("name", "m", "2025-01-01", "address", "city", "state", "1234PIN", "1234567890", "email@gmail.com", "password"))

    def test_NC16(self):
        """PIN cannot be empty"""
        self.assertEqual("PIN Code must not be blank", self.m.add_customer("name", "m", "2025-01-01", "address", "city", "state", "", "1234567890", "email@gmail.com", "password"))
        self.assertEqual("PIN Code must not be blank", self.m.add_customer("name", "m", "2025-01-01", "address", "city", "state", Keys.TAB, "1234567890", "email@gmail.com", "password"))

    def test_NC17(self):
        """PIN must have 6 digits"""
        self.assertEqual("PIN Code must have 6 Digits", self.m.add_customer("name", "m", "2025-01-01", "address", "city", "state", "1234567", "1234567890", "email@gmail.com", "password"))
        self.assertEqual("PIN Code must have 6 Digits", self.m.add_customer("name", "m", "2025-01-01", "address", "city", "state", "123", "1234567890", "email@gmail.com", "password"))

    def test_NC18(self):
        """PIN cannot have special character"""
        self.assertEqual("Special characters are not allowed", self.m.add_customer("name", "m", "2025-01-01", "address", "city", "state", "!@#", "1234567890", "email@gmail.com", "password"))
        self.assertEqual("Special characters are not allowed", self.m.add_customer("name", "m", "2025-01-01", "address", "city", "state", "123!@#", "1234567890", "email@gmail.com", "password"))

    def test_NC19(self):
        """PIN cannot have first blank space"""
        self.assertEqual("First character can not have space", self.m.add_customer("name", "m", "2025-01-01", "address", "city", "state", " 123456", "1234567890", "email@gmail.com", "password"))

    def test_NC20(self):
        """PIN cannot have blank space"""
        self.assertEqual("Characters are not allowed", self.m.add_customer("name", "m", "2025-01-01", "address", "city", "state", "123 456", "1234567890", "email@gmail.com", "password"))

    # Verify number field
    def test_NC21(self):
        """Mobile number cannot be empty"""
        self.assertEqual("Mobile no must not be blank", self.m.add_customer("name", "m", "2025-01-01", "address", "city", "state", "123456", "", "email@gmail.com", "password"))
        self.assertEqual("Mobile no must not be blank", self.m.add_customer("name", "m", "2025-01-01", "address", "city", "state", "123456", Keys.TAB, "email@gmail.com", "password"))

    def test_NC22(self):
        """Mobile numberTelephone cannot have first character as blank space"""
        self.assertEqual("First character can not have space", self.m.add_customer("name", "m", "2025-01-01", "address", "city", "state", "123456", " 1234567890", "email@gmail.com", "password"))

    def test_NC23(self):
        """Mobile number cannot have spaces"""
        self.assertEqual("Characters are not allowed", self.m.add_customer("name", "m", "2025-01-01", "address", "city", "state", "123456", "123 123", "email@gmail.com", "password"))

    def test_NC24(self):
        """Mobile number cannot have special character"""
        self.assertEqual("Special characters are not allowed", self.m.add_customer("name", "m", "2025-01-01", "address", "city", "state", "123456", "886636!@12", "email@gmail.com", "password"))
        self.assertEqual("Special characters are not allowed", self.m.add_customer("name", "m", "2025-01-01", "address", "city", "state", "123456", "!@88662682", "email@gmail.com", "password"))
        self.assertEqual("Special characters are not allowed", self.m.add_customer("name", "m", "2025-01-01", "address", "city", "state", "123456", "88663682!@", "email@gmail.com", "password"))

    # Verify email field
    def test_NC25(self):
        """Email cannot be empty"""
        self.assertEqual("Email-ID must not be blank", self.m.add_customer("name", "m", "2025-01-01", "address", "city", "state", "123456", "1234567890", "", "password"))
        self.assertEqual("Email-ID must not be blank", self.m.add_customer("name", "m", "2025-01-01", "address", "city", "state", "123456", "1234567890", Keys.TAB, "password"))

    def test_NC26(self):
        """Email must be in correct format"""
        self.assertEqual("Email-ID is not valid", self.m.add_customer("name", "m", "2025-01-01", "address", "city", "state", "123456", "1234567890", "guru99@gmail", "password"))
        self.assertEqual("Email-ID is not valid", self.m.add_customer("name", "m", "2025-01-01", "address", "city", "state", "123456", "1234567890", "guru99", "password"))
        self.assertEqual("Email-ID is not valid", self.m.add_customer("name", "m", "2025-01-01", "address", "city", "state", "123456", "1234567890", "Guru99@", "password"))
        self.assertEqual("Email-ID is not valid", self.m.add_customer("name", "m", "2025-01-01", "address", "city", "state", "123456", "1234567890", "guru99@gmail.", "password"))
        self.assertEqual("Email-ID is not valid", self.m.add_customer("name", "m", "2025-01-01", "address", "city", "state", "123456", "1234567890", "guru99gmail.com", "password"))

    def test_NC27(self):
        """Email cannot have space"""
        self.assertEqual("Email-ID is not valid", self.m.add_customer("name", "m", "2025-01-01", "address", "city", "state", "123456", "1234567890", "email@ gmail.com", "password"))

    # Verify password field
    def test_NC28(self):
        """Password cannot be empty"""
        self.assertEqual("Password must not be blank", self.m.add_customer("name", "m", "2025-01-01", "address", "city", "state", "123456", "1234567890", "email@gmail.com", ""))
        self.assertEqual("Password must not be blank", self.m.add_customer("name", "m", "2025-01-01", "address", "city", "state", "123456", "1234567890", "email@gmail.com", Keys.TAB))

    # ========================================
    # ==========  2. EDIT CUSTOMER  ==========
    # ========================================
    # VERIFY CUSTOMER ID
    def test_EC1(self):
        """Customer ID cannot be empty"""
        self.assertEqual("Customer ID is required", self.m.navigate_to_edit_customer(Keys.TAB))

    def test_EC2(self):
        """Customer ID must be numeric"""
        self.assertEqual("Characters are not allowed", self.m.navigate_to_edit_customer("1234Acc"))
        self.assertEqual("Characters are not allowed", self.m.navigate_to_edit_customer("Acc1234"))

    def test_EC3(self):
        """Customer ID cannot have special character"""
        self.assertEqual("Special characters are not allowed", self.m.navigate_to_edit_customer("123!@#"))
        self.assertEqual("Special characters are not allowed", self.m.navigate_to_edit_customer("!@#"))

    def test_EC4(self):
        """Valid Customer ID"""
        self.m.navigate_to_edit_customer(TestManager.CUSTOMER_ID)
        self.m.submit_edit_customer_login()
        self.assertEqual("https://demo.guru99.com/V4/manager/editCustomerPage.php", self.browser.current_url)

    # VERIFY ADDRESS FIELD
    def test_EC5(self):
        """Address cannot be empty"""
        self.m.navigate_to_edit_customer(TestManager.CUSTOMER_ID)
        self.m.submit_edit_customer_login()
        self.assertEqual("Address Field must not be blank", self.m.edit_customer_address(Keys.TAB))

    # VERIFY CITY FIELD
    def test_EC6(self):
        """City cannot be empty"""
        self.m.navigate_to_edit_customer(TestManager.CUSTOMER_ID)
        self.m.submit_edit_customer_login()
        self.assertEqual("City Field must not be blank", self.m.edit_customer_city(Keys.TAB))

    def test_EC7(self):
        """City cannot be numeric"""
        self.m.navigate_to_edit_customer(TestManager.CUSTOMER_ID)
        self.m.submit_edit_customer_login()
        self.assertEqual("Numbers are not allowed", self.m.edit_customer_city("1234"))
        self.assertEqual("Numbers are not allowed", self.m.edit_customer_city("city123"))

    def test_EC8(self):
        """City cannot have special characters"""
        self.m.navigate_to_edit_customer(TestManager.CUSTOMER_ID)
        self.m.submit_edit_customer_login()
        self.assertEqual("Special characters are not allowed", self.m.edit_customer_city("City!@#"))
        self.assertEqual("Special characters are not allowed", self.m.edit_customer_city("!@#"))

    # VERIFY STATE FIELD
    def test_EC9(self):
        """State cannot be empty"""
        self.m.navigate_to_edit_customer(TestManager.CUSTOMER_ID)
        self.m.submit_edit_customer_login()
        self.assertEqual("State must not be blank", self.m.edit_customer_state(Keys.TAB))

    def test_EC10(self):
        """State cannot be numeric"""
        self.m.navigate_to_edit_customer(TestManager.CUSTOMER_ID)
        self.m.submit_edit_customer_login()
        self.assertEqual("Numbers are not allowed", self.m.edit_customer_state("1234"))
        self.assertEqual("Numbers are not allowed", self.m.edit_customer_state("State123"))

    def test_EC11(self):
        """State cannot have special character"""
        self.m.navigate_to_edit_customer(TestManager.CUSTOMER_ID)
        self.m.submit_edit_customer_login()
        self.assertEqual("Special characters are not allowed", self.m.edit_customer_state("State!@#"))
        self.assertEqual("Special characters are not allowed", self.m.edit_customer_state("!@#"))

    # VERIFY PIN
    def test_EC12(self):
        """PIN must be numeric"""
        self.m.navigate_to_edit_customer(TestManager.CUSTOMER_ID)
        self.m.submit_edit_customer_login()
        self.assertEqual("Characters are not allowed", self.m.edit_customer_PIN0("PIN1234"))
        self.assertEqual("Characters are not allowed", self.m.edit_customer_PIN0("1234PIN"))

    def test_EC13(self):
        """PIN cannot be empty"""
        self.m.navigate_to_edit_customer(TestManager.CUSTOMER_ID)
        self.m.submit_edit_customer_login()
        self.assertEqual("PIN Code must not be blank", self.m.edit_customer_PIN1(Keys.TAB))


    def test_EC14(self):
        """PIN must have 6 digits"""
        self.m.navigate_to_edit_customer(TestManager.CUSTOMER_ID)
        self.m.submit_edit_customer_login()

        self.assertEqual("PIN Code must have 6 Digits", self.m.edit_customer_PIN("1234567"))
        self.assertEqual("PIN Code must have 6 Digits", self.m.edit_customer_PIN("123"))


    def test_EC15(self):
        """PIN cannot have special character"""
        self.m.navigate_to_edit_customer(TestManager.CUSTOMER_ID)
        self.m.submit_edit_customer_login()
        self.assertEqual("Special characters are not allowed", self.m.edit_customer_PIN("!@#"))
        self.assertEqual("Special characters are not allowed", self.m.edit_customer_PIN("123!@#"))

    # VERIFY MOBILE NUMBER FIELD
    def test_EC16(self):
        """Mobile No. cannot be empty"""
        self.m.navigate_to_edit_customer(TestManager.CUSTOMER_ID)
        self.m.submit_edit_customer_login()
        self.assertEqual("Mobile no must not be blank", self.m.edit_customer_mobile_number(Keys.TAB))

    def test_EC17(self):
        """Mobile No. cannot have special character"""
        self.m.navigate_to_edit_customer(TestManager.CUSTOMER_ID)
        self.m.submit_edit_customer_login()
        self.assertEqual("Special characters are not allowed", self.m.edit_customer_mobile_number("886636!@12"))
        self.assertEqual("Special characters are not allowed", self.m.edit_customer_mobile_number("!@88662682"))
        self.assertEqual("Special characters are not allowed", self.m.edit_customer_mobile_number("88663682!@"))

    # VERIFY EMAIL FIELD
    def test_EC18(self):
        """Email cannot be empty"""
        self.m.navigate_to_edit_customer(TestManager.CUSTOMER_ID)
        self.m.submit_edit_customer_login()
        self.assertEqual("Email-ID must not be blank", self.m.edit_customer_email(Keys.TAB))

    def test_EC19(self):
        """Email must be in format 'career@guru99.com'"""
        self.m.navigate_to_edit_customer(TestManager.CUSTOMER_ID)
        self.m.submit_edit_customer_login()
        self.assertEqual("Email-ID is not valid", self.m.edit_customer_email("guru99@gmail"))
        self.assertEqual("Email-ID is not valid", self.m.edit_customer_email("guru99"))
        self.assertEqual("Email-ID is not valid", self.m.edit_customer_email("Guru99@"))
        self.assertEqual("Email-ID is not valid", self.m.edit_customer_email("guru99gmail.com"))

    # SUBMIT BUTTON
    def test_EC20(self):
        """Successful submit after every update"""
        self.m.navigate_to_edit_customer(TestManager.CUSTOMER_ID)
        self.m.submit_edit_customer_login()
        sleep(1)

        self.assertEqual("Update done successfully", self.m.submit_edit_customer_form())

    # ========================================
    # =========  3. DELETE CUSTOMER  =========
    # ========================================
    def test_DC1(self):
        """Customer ID cannot be empty"""
        self.assertEqual("Customer ID is required", self.m.delete_customer(Keys.TAB))

    def test_DC2(self):
        """Customer ID must be numeric"""
        self.assertEqual("Characters are not allowed",self.m.delete_customer("1234Acc"))
        self.assertEqual("Characters are not allowed",self.m.delete_customer("Acc123"))

    def test_DC3(self):
        """Customer ID cannot have special character"""
        self.assertEqual("Special characters are not allowed",self.m.delete_customer("123!@#"))
        self.assertEqual("Special characters are not allowed",self.m.delete_customer("!@#"))

    def test_DC4(self):
        """Customer ID cannot have blank space"""
        self.assertEqual("Characters are not allowed",self.m.delete_customer("123 12"))

    def test_DC5(self):
        """First Character cannot be space"""
        self.assertEqual("First character can not have space",self.m.delete_customer(" a     q"))

    def test_DC6(self):
        """Incorrect Customer ID"""
        self.m.delete_customer("123456")
        self.m.submit_delete_form()
        self.assertEqual("Customer does not exist!!", self.m.accept_customer_does_not_exist())

    def test_DC7(self):
        """Correct Customer ID"""
        self.m.delete_customer(TestManager.CUSTOMER_ID_DELETE)
        self.m.submit_delete_form()
        self.assertEqual("Customer could not be deleted!!. First delete all accounts of this customer then delete the customer", self.m.accept_customer_does_not_exist())

    def test_DC8(self):
        """Reset Button"""
        self.m.delete_customer("qwer")
        self.m.reset_delete_form()
        sleep(1)
        self.assertEqual("", self.m.browser.find_element(By.NAME, "cusid").text)
        self.m.delete_customer("123456")
        self.m.reset_delete_form()
        sleep(1)
        self.assertEqual("", self.m.browser.find_element(By.NAME, "cusid").text)

    # ========================================
    # ===========  4. NEW ACCOUNT  ===========
    # ========================================
    # NA 1 - 5 VERIFYING CUSTOMER ID
    def test_NA1(self):
        """ID Cannot be empty"""
        self.m.navigate_to_new_account()
        self.assertEqual("Customer ID is required", self.m.add_customer_id(Keys.TAB))

    def test_NA2(self):
        """Customer id must be numeric """
        self.m.navigate_to_new_account()
        self.assertEqual("Characters are not allowed", self.m.add_customer_id("1234Acc"))
        self.assertEqual("Characters are not allowed", self.m.add_customer_id("Acc123"))

    def test_NA3(self):
        """Customer ID cannot have a special character"""
        self.m.navigate_to_new_account()
        self.assertEqual("Special characters are not allowed", self.m.add_customer_id("1234!@#"))
        self.assertEqual("Special characters are not allowed", self.m.add_customer_id("!@#"))

    def test_NA4(self):
        """Customer ID cannot have a blank space"""
        self.m.navigate_to_new_account()
        self.assertEqual("Characters are not allowed", self.m.add_customer_id("123 12" + Keys.TAB))

    def test_NA5(self):
        """First character cannot be space"""
        self.m.navigate_to_new_account()
        self.assertEqual("First character can not have space", self.m.add_customer_id(" " + Keys.TAB))

    # NA 6 - 10 VERFYING INITIAL DEPOSIT
    def test_NA6(self):
        """Initial deposit must not be blank"""
        self.m.navigate_to_new_account()
        self.assertEqual("Initial Deposit must not be blank", self.m.add_initial_deposit(Keys.TAB))

    def test_NA7(self):
        """Must be numeric"""
        self.m.navigate_to_new_account()
        self.assertEqual("Characters are not allowed", self.m.add_initial_deposit("1234Acc"))
        self.assertEqual("Characters are not allowed", self.m.add_initial_deposit("Acc123"))

    def test_NA8(self):
        """Cannot have a special char"""
        self.m.navigate_to_new_account()
        self.assertEqual("Special characters are not allowed", self.m.add_initial_deposit("123!@#"))
        self.assertEqual("Special characters are not allowed", self.m.add_initial_deposit("!@#"))

    def test_NA9(self):
        """Deposit cannot have a blank space"""
        self.m.navigate_to_new_account()
        self.assertEqual("Characters are not allowed", self.m.add_initial_deposit("123 12"))

    def test_NA10(self):
        """First char cannot be spaced"""
        self.m.navigate_to_new_account()
        self.assertEqual("First character can not have space", self.m.add_initial_deposit(" " + Keys.TAB))

    # NA 11 - 12 for VERIFYING ACCOUNT TYPE DROPDOWN
    def test_NA11(self):
        """Savings account type"""
        self.m.navigate_to_new_account()
        self.assertEqual("Savings", self.m.add_account_type("Savings"))

    def test_NA12(self):
        """Current account type"""
        self.m.navigate_to_new_account()
        self.assertEqual("Current", self.m.add_account_type("Current"))

    # NA 13 Designed for Reset button
    # Verfying Reset Button
    def test_NA13(self):
        """Confirmed reset form"""
        self.m.navigate_to_new_account()
        self.m.add_customer_id("qwer")
        self.m.add_initial_deposit("123456")
        self.m.new_account_reset()

        self.assertEqual("", self.browser.find_element(By.NAME, "cusid").text)
        self.assertEqual("", self.browser.find_element(By.NAME, "inideposit").text)

    # NA 14 - 15 Verifying Submit Button
    def test_NA14(self):
        """Incorrect Customer ID"""
        self.m.navigate_to_new_account()
        self.m.add_customer_id("123456")
        self.m.new_account_submit()

    def test_NA15(self):
        """Correct customer ID and correct amount"""
        self.m.navigate_to_new_account()
        self.m.add_customer_id(TestManager.CUSTOMER_ID)
        self.m.add_initial_deposit("200")
        self.m.new_account_submit()

    def test_NA16(self):
        """Continue hyperlink on next page after successful creation of account"""
        self.assertEqual("Continue hyperlink on next page after successful creation of account",
                         self.m.new_account_continue(12345 ,1000))

    # ========================================
    # ===========  5. EDIT ACCOUNT  ==========
    # ========================================
    def test_EA1(self):
        """Account number in the edit section cannot be blank"""
        self.assertEqual("Account Number must not be blank", self.m.edit_customer_account(Keys.TAB))

    def test_EA2(self):
        """Account number cannot be in characters has to be numbers"""
        self.assertEqual("Characters are not allowed", self.m.edit_customer_account("1234Acc"))
        self.assertEqual("Characters are not allowed", self.m.edit_customer_account("Acc123"))

    def test_EA3(self):
        """Account Number with special characters (must be numeric)"""
        self.assertEqual("Special characters are not allowed", self.m.edit_customer_account("123!@#"))
        self.assertEqual("Special characters are not allowed", self.m.edit_customer_account("!@#"))

    def test_EA4(self):
        """Account number cannot have blank space"""
        self.assertEqual("Characters are not allowed", self.m.edit_customer_account("123 12"))

    def test_EA5(self):
        """First Character cannot be space"""
        self.assertEqual("First character cannot have space", self.m.edit_customer_account(" Savings"))

    def test_EA6(self):
        """Valid Account Number"""
        self.m.edit_customer_account(TestManager.CUSTOMER_ID)
        self.assertEqual("demo.guru99.com", self.m.submit_edit_account_form())

    # Bug Code
    def test_EA7(self):
        """Invalid account number"""
        self.m.edit_customer_account("123456763")
        self.assertEqual("Account does not exist", self.m.submit_edit_account_form())

    def test_EA8(self):
        """Reset Button"""
        self.m.edit_customer_account("qwer")
        self.m.reset_edit_account_form()
        sleep(1)

        self.assertEqual("", self.browser.find_element(By.XPATH, "//input[@name='accountno']").text)

        self.m.edit_customer_account("123456")
        self.m.reset_edit_account_form()
        sleep(1)

        self.assertEqual("", self.browser.find_element(By.XPATH, "//input[@name='accountno']").text)
    # ========================================
    # ==========  6. DELETE ACCOUNT  =========
    # ========================================
    def test_DA1(self):
        """Account cannot be empty"""
        result = self.m.delete_account(" ")
        self.assertEqual("Account Number must not be blank", result)
        self.assertEqual("Account Number must not be blank", self.m.delete_account(Keys.TAB))

    def test_DA2(self):
        """Account must be numeric"""
        result = self.m.delete_account("1234abc")
        self.assertEqual("Characters are not allowed", result)
        self.assertEqual("Characters are not allowed", self.m.delete_account("Acc123"))

    def test_DA3(self):
        """Account cannot have special characters"""
        self.assertEqual("Special characters are not allowed", self.m.delete_account("123!@#"))
        self.assertEqual("Special characters are not allowed", self.m.delete_account("!@#"))

    def test_DA4(self):
        """Account cannot have spaces"""
        result = self.m.delete_account("123 12")
        self.assertEqual("Characters are not allowed", result)

    def test_DA5(self):
        """Account cannot have first character as blank space"""
        result = self.m.delete_account(" 123")
        self.assertEqual("Characters are not allowed", result)

    def test_DA6(self):
        """Submit with valid Account Number shows success message"""
        # First test with a non-existent account
        result = self.m.delete_account("123456")
        self.assertEqual("Account does not exist", result)

        # Note: For actual successful deletion, you would need a valid account number
        # result = self.m.delete_account("VALID_ACCOUNT_NUMBER")
        # self.assertEqual("Account deleted successfully", result)

    def test_DA7(self):
        """Do You really want to delete this customer?"""
        self.assertEqual("Account deleted successfully", self.m.delete_customer_account(TestManager.ACCOUNT_ID_DELETE))

    def test_DA8(self):
        """Reset Button test"""
        test_value = "12345"
        sleep(2)
        result = self.m.delete_account(test_value, False)
        self.assertTrue(result)  # Should return True if the field was cleared


    # ==========================================
    # ==========  7. BALANCE ENQUIRY  ==========
    # ==========================================
    #Verify account number
    def test_BE1(self):
        """Account number cannot be empty"""
        self.assertEqual("Account Number must not be blank", self.m.balance_enquiry_validate(""))
        self.assertEqual("Account Number must not be blank", self.m.balance_enquiry_validate(Keys.TAB))

    def test_BE2(self):
        """Account number must be numeric"""
        self.assertEqual("Characters are not allowed", self.m.balance_enquiry_validate("1234Acc"))
        self.assertEqual("Characters are not allowed", self.m.balance_enquiry_validate("Acc123"))

    def test_BE3(self):
        """Account number cannot have special character"""
        self.assertEqual("Special characters are not allowed", self.m.balance_enquiry_validate("123!@#"))
        self.assertEqual("Special characters are not allowed", self.m.balance_enquiry_validate("!@#"))

    def test_BE4(self):
        """First Character cannot be space"""
        self.assertEqual("First character cannot have space", self.m.balance_enquiry_validate1(" 1234"))
        self.assertEqual("First character cannot have space", self.m.balance_enquiry_validate1(" "))

    # Verify submit button
    def test_BE5(self):
        """Valid Account Number"""
        self.m.balance_enquiry_validate("175228")
        self.assertEqual("demo.guru99.com", self.m.balance_enquiry_submit())

    def test_BE6(self):
        """InValid Account Number"""
        self.m.balance_enquiry_validate("12345")
        self.assertEqual("Account does not exist", self.m.balance_enquiry_submit())

    # Verify reset button
    def test_BE7(self):
        """Reset the Account No field"""
        self.m.balance_enquiry_fill("qwer")
        self.assertEqual("", self.m.balance_enquiry_reset())
        self.m.balance_enquiry_fill("123456")
        self.assertEqual("", self.m.balance_enquiry_reset())

    # ========================================
    # ==========  8. MINI STATEMENT  =========
    # ========================================
    # VERIFY ACCOUNT NUMBER
    def test_MS1(self):
        """Account number cannot be empty"""
        self.assertEqual("Account Number must not be blank", self.m.navigate_to_mini_statement(Keys.TAB))

    def test_MS2(self):
        """Account number must be numeric"""
        self.assertEqual("", self.m.navigate_to_mini_statement("1234"))
        self.assertEqual("Characters are not allowed", self.m.navigate_to_mini_statement("Acc123"))

    def test_MS3(self):
        """Account number cannot have special characters"""
        self.assertEqual("Special characters are not allowed", self.m.navigate_to_mini_statement("123!@#"))
        self.assertEqual("Special characters are not allowed", self.m.navigate_to_mini_statement("!@#"))

    def test_MS4(self):
        """Account number cannot contain blank space"""
        self.assertEqual("Characters are not allowed", self.m.navigate_to_mini_statement("123 12"))

    def test_MS5(self):
        """First Character cannot be space"""
        self.assertEqual("First character cannot have space", self.m.navigate_to_mini_statement(" " + Keys.TAB))

    # VERIFY SUBMIT BUTTON
    def test_MS6(self):
        """Valid account number should navigate to mini statement page"""
        self.m.navigate_to_mini_statement(TestManager.CUSTOMER_ID)
        self.m.submit_mini_statement_login()

        # Wait until the URL is the expected one
        sleep(10)

        self.assertEqual(
            "https://demo.guru99.com/V4/manager/MiniStatement.php",
            self.browser.current_url
        )

    def test_MS7(self):
        """Invalid Account Number"""
        self.m.navigate_to_mini_statement("12345")
        self.m.submit_mini_statement_login()

        # Wait for the alert to be present
        sleep(10)

        alert = self.browser.switch_to.alert
        self.assertEqual("Account does not exist", alert.text)

    # VERIFY RESET BUTTON
    def test_MS8(self):
        """Account number is reset when field is not empty"""
        self.m.navigate_to_mini_statement("qwer")
        self.m.reset_mini_statement_login()
        self.assertEqual("", self.m.browser.find_element(By.XPATH, "//input[@name='accountno']").get_attribute("value"))

        self.m.navigate_to_mini_statement("123456")
        self.m.reset_mini_statement_login()
        self.assertEqual("", self.m.browser.find_element(By.XPATH, "//input[@name='accountno']").get_attribute("value"))

    # ========================================
    # =======  9. CUSTOMIZED STATEMENT  ======
    # ========================================
    def test_CS1(self):
        """Account number cannot be empty"""
        result = self.m.customized_statement(" ")
        self.assertEqual("Account Number must not be blank", result)

    def test_CS2(self):
        """Account number must be numeric"""
        result = self.m.customized_statement("Acc123")
        self.assertEqual("Characters are not allowed", result)

    def test_CS3(self):
        """Account number cannot have a special character"""
        result = self.m.customized_statement("123!@#")
        self.assertEqual("Special characters are not allowed", result)
        self.assertEqual("Special characters are not allowed", self.m.customized_statement("!@#"))

    def test_CS4(self):
        """Account number cannot have blank space"""
        result = self.m.customized_statement("123 12")
        self.assertEqual("Characters are not allowed", result)

    def test_CS5(self):
        """First character cannot be space"""
        result = self.m.customized_statement(" 1")
        self.assertEqual("First character cannot have space", result)

    def test_CS6(self):
        """From Date field cannot be empty"""
        result = self.m.customized_statement("12345", fdate=" ")
        self.assertEqual("From Date Field must not be blank", result)

    def test_CS7(self):
        """To Date field cannot be empty"""
        result = self.m.customized_statement("12345", tdate=" ")
        self.assertEqual("To Date Field must not be blank", result)

    def test_CS8(self):
        """Minimum Transaction Value must be numeric"""
        result = self.m.customized_statement("12345", amountlowerlimit="abc")
        self.assertEqual("Characters are not allowed", result)

    def test_CS9(self):
        """Minimum Transaction Value cannot have a special character"""
        result = self.m.customized_statement("12345", amountlowerlimit="100!")
        self.assertEqual("Special characters are not allowed", result)

    def test_CS10(self):
        """Minimum Transaction Value cannot have blank space"""
        result = self.m.customized_statement("12345", amountlowerlimit="10 0")
        self.assertEqual("Characters are not allowed", result)
        self.assertEqual("Characters are not allowed", self.m.customized_statement(Keys.TAB))

    def test_CS11(self):
        """Minimum Transaction Value first character cannot be space"""
        result = self.m.customized_statement("12345", amountlowerlimit=" 100")
        self.assertEqual("Characters are not allowed", result)
        self.assertEqual("Characters are not allowed", self.m.customized_statement(Keys.TAB))


    def test_CS12(self):
        """Number of Transactions must be numeric"""
        result = self.m.customized_statement("12345", numtransaction="abc")
        self.assertEqual("Characters are not allowed", result)

    def test_CS13(self):
        """Number of Transactions cannot have a special character"""
        result = self.m.customized_statement("12345", numtransaction="100!")
        self.assertEqual("Special characters are not allowed", result)

    def test_CS14(self):
        """Number of Transactions cannot have blank space"""
        result = self.m.customized_statement("12345", numtransaction="1 0")
        self.assertEqual("Characters are not allowed", result)
        self.assertEqual("Characters are not allowed", self.m.customized_statement(Keys.TAB))

    def test_CS15(self):
        """Number of Transaction first character cannot be space"""
        result = self.m.customized_statement("12345", numtransaction=" 10")
        self.assertEqual("Characters are not allowed", result)
        self.assertEqual("Characters are not allowed", self.m.customized_statement(Keys.TAB))


    def test_CS16(self):
        """Reset Button test"""
        test_value = "12345"
        result = self.m.customized_statement(test_value, submit=False)
        self.assertTrue(result)  # Should return True if the field was cleared

    def test_CS17(self):
        """Submit with valid Account Number but blank To Date"""
        result = self.m.check_filed_error("1234545",fdate="0020021205", tdate="", amountlowerlimit="10000",numtransaction="20")
        self.assertEqual("Please fill all fields", result)

# ==========  EXECUTION  ==========
if __name__ == '__main__':
    unittest.main()
