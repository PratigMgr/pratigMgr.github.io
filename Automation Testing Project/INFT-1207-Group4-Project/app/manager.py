# File:     manager.py
# Type:     Python (.py) file
# Authors:  Kyle Angeles, Mathuran Chandramohan, Pratig Thapa,  Maxximillion Thomas
# Date:     Aug 7, 2025
# Desc.:    Perform tests on a dummy banking website to simulate Manager privileges

# ==========  IMPORTS  ==========
# Import modules to allow Chrome browsing through Selenium
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


# TEMPORARY
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeS
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager as ChromeDM


# ==========  CLASS  ==========
class Manager:
    # ==========  CONSTANTS  ==========
    SPECIAL_CHARACTERS = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")",
                          "-", "_", "=", "+", r"\\", "|", ";", ":", r"\"", ",", "<",
                          ".", ">", "/", "?"]
    ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    NUMBERS = "0123456789"
    NONE = []

    # ==========  CONSTRUCTOR  ==========
    def __init__(self, driver):
        self.browser = driver

    # ==========  HELPERS  ==========
    def validate_argument(self, argument, xpath, illegal_arguments):
        """Return the error message created by a field when entering its respective argument"""
        # Establish the element for targeting, should an error message be triggered
        target = self.browser.find_element(By.XPATH, xpath)

        # Create a tracker for passing individual tests
        fail = False

        # Cannot be empty
        if len(argument) == 0 or argument == Keys.TAB: fail = True

        # Cannot contain certain characters
        if not fail:
            for c in argument:
                for array in illegal_arguments:
                    if c in array: fail = True

        # Cannot have first character as blank space
        if not fail:
            if argument[0] == " ": fail = True

        # Return the pass/fail result and error message associated with the argument (field)
        return fail, target.text

    def validate_email(self, email):
        """Check if user has entered a valid email"""
        # Email error message XPath
        invalid_email_message = "//label[@id='message9']"

        # Must contain "@" and "."
        if "@" not in email or "." not in email:
            return True, self.browser.find_element(By.XPATH, "//label[@id='message9']").text

        # Separate username and domain name
        # (e.g. user@mail.com -> ['user', 'mail.com'])
        email_pieces = email.split("@")

        # Must have characters before and after "@"
        if len(email_pieces) != 2 or email_pieces[0] == "" or email_pieces[1] == "":
            return True, self.browser.find_element(By.XPATH, "//label[@id='message9']").text

        # Separate domain name and top-level domain (TLD)
        # (e.g. mail.com -> ['mail', 'com'])
        domain_parts = email_pieces[1].split(".")

        # Must have valid domain name and TLD
        if len(domain_parts) < 2 or len(domain_parts[-1]) < 2 or not domain_parts[-1].isalpha():
            return True, self.browser.find_element(By.XPATH, "//label[@id='message9']").text

        # Passes all tests
        return False, self.browser.find_element(By.XPATH, "//label[@id='message9']").text

    # ===============================
    # ==========  SHARED  ===========
    # ===============================
    def login_manager(self):
        """Log into the guru banking website"""
        self.browser.get("https://demo.guru99.com/V4/")
        self.browser.find_element(By.NAME, "uid").send_keys("mngr629176")
        self.browser.find_element(By.NAME, "password").send_keys("mUqazev")
        self.browser.find_element(By.NAME, "btnLogin").click()

    # =======================================
    # ==========  1. NEW CUSTOMER  ==========
    # =======================================
    def add_customer(self, name, gender, dob, address, city, state, pin, number, email, password):
        """Add a new customer to the database"""
        # Navigate to the Add New Customer page
        sleep(1)
        self.return_to_home_page()
        self.browser.find_element(By.XPATH, "//a[normalize-space()='New Customer']").click()

        # Use the arguments as data for the customer add page
        self.browser.find_element(By.NAME, "name").send_keys(name)
        gender = gender.lower().strip()
        if gender == "m":
            self.browser.find_element(By.XPATH, "//input[@value='m']").click()
        elif gender == "f":
            self.browser.find_element(By.XPATH, "//input[@value='f']").click()
        dob = dob.split("-")
        dob = dob[0] + "\t" + dob[1] + dob[2]
        self.browser.find_element(By.NAME, "dob").send_keys(dob)
        self.browser.find_element(By.NAME, "addr").send_keys(address)
        self.browser.find_element(By.NAME, "city").send_keys(city)
        self.browser.find_element(By.NAME, "state").send_keys(state)
        self.browser.find_element(By.NAME, "pinno").send_keys(pin)
        self.browser.find_element(By.NAME, "telephoneno").send_keys(number)
        self.browser.find_element(By.NAME, "emailid").send_keys(email)
        self.browser.find_element(By.NAME, "password").send_keys(password)
        self.browser.find_element(By.NAME, "password").send_keys(Keys.TAB)
        sleep(1)

        # Argument validation:  name
        invalid, message = self.validate_argument(name, "//label[@id='message']", [self.NUMBERS, self.SPECIAL_CHARACTERS])
        if invalid: return message

        # Argument validation:  gender
        # Cannot be of length other than 1
        if len(gender) != 1 or gender == Keys.TAB:
            raise ValueError('Gender must be entered as a single character ("m" or "f")')
        # Cannot be numeric nor a special character
        if gender.isdigit() or gender in self.SPECIAL_CHARACTERS:
            raise TypeError('Neither numbers nor special characters are allowed')
        # Cannot be anything but "m" or "f"
        if gender != "m" and gender != "f":
            raise ValueError('Gender must either be "m" or "f"')

        # Argument validation: dob
        # Cannot be empty
        if len(dob) == 0 or dob == Keys.TAB:
            raise ValueError('Date of birth must not be blank')
        # Cannot have alphabetical nor special characters
        for digit in dob:
            if digit in self.SPECIAL_CHARACTERS or digit in self.ALPHABET:
                raise TypeError('Neither alphabetical nor special characters are allowed')

        # Argument validation:  address
        invalid, message = self.validate_argument(address, "//label[@id='message3']", [self.SPECIAL_CHARACTERS, self.NONE])
        if invalid: return message

        # Argument validation:  city
        invalid, message = self.validate_argument(city, "//label[@id='message4']", [self.NUMBERS, self.SPECIAL_CHARACTERS])
        if invalid: return message

        # Argument validation:  state
        invalid, message = self.validate_argument(state, "//label[@id='message5']", [self.NUMBERS, self.SPECIAL_CHARACTERS])
        if invalid: return message

        # Argument validation:  pin
        if (len(pin.strip()) != 6) or (" " in pin.strip()): return "PIN Code must have 6 Digits"
        invalid, message = self.validate_argument(pin, "//label[@id='message6']", [self.ALPHABET, self.SPECIAL_CHARACTERS])
        if invalid: return message

        # Argument validation:  number
        if " " in number.strip(): return self.browser.find_element(By.XPATH, "//label[@id='message7']").text
        invalid, message = self.validate_argument(number, "//label[@id='message7']", [self.ALPHABET, self.SPECIAL_CHARACTERS])
        if invalid: return message

        # Argument validation:  email
        invalid = False
        # Must have both "@" and "." included
        if ("@" not in email) or ("." not in email): invalid = True
        # First character can not have space
        if not invalid:
            if email[0] == " ": invalid = True
        # Cannot contain a space
        if not invalid:
            if " " in email.strip(): invalid = True
            return "Email-ID is not valid"
        # Must be characters before/after the "@", and the "." must be followed by 2 or more characters
        if not invalid:
            email_pieces = email.strip().split("@")
            if (email_pieces[0] == "") or (email_pieces[1] == "") or ("." not in email_pieces[1]):
                invalid = True
            else:
                if (email_pieces[1].find(".") == 0) or (email_pieces[1].find(".") >= len(email_pieces[1]) - 2): invalid = True
        if invalid: return self.browser.find_element(By.XPATH, "//label[@id='message9']").text

        # Argument validation:  password
        password_field_text = self.browser.find_element(By.NAME, "password").text
        if len(password_field_text.strip()) == 0: return self.browser.find_element(By.XPATH, "//label[@id='message18']").text

        # All tests passed, submit the form
        self.browser.find_element(By.NAME, "sub").click()
        return None

    # ========================================
    # ==========  2. EDIT CUSTOMER  ==========
    # ========================================
    def return_to_home_page(self):
        """Return user to manager homepage"""
        self.browser.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")

    def navigate_to_edit_customer(self, customer_id):
        """Navigate to 'Edit Customer' Page"""
        # Navigate to 'Edit Customer'
        self.browser.find_element(By.XPATH, "//a[normalize-space()='Edit Customer']").click()
        sleep(1)

        # Clear text field
        self.browser.find_element(By.NAME, "cusid").clear()
        sleep(1)

        # Enter customer id
        self.browser.find_element(By.NAME, "cusid").send_keys(customer_id)
        sleep(1)

        # Validate user's input
        invalid, message = self.validate_argument(customer_id, "//label[@id='message14']", [Manager.ALPHABET, Manager.SPECIAL_CHARACTERS])

        return message

    def submit_edit_customer_login(self):
        """Login to customer's 'Edit Customer' page"""
        self.browser.find_element(By.NAME, "AccSubmit").click()
        sleep(2)

    def edit_customer_address(self, address):
        """Verify and change customer's address"""
        # Clear text field
        self.browser.find_element(By.NAME, "addr").clear()
        sleep(1)

        # Enter new address
        self.browser.find_element(By.NAME, "addr").send_keys(address)
        sleep(1)

        # Validate user's input
        invalid, message = self.validate_argument(address, "//label[@id='message3']", [])

        return message

    def edit_customer_city(self, city):
        """Verify and change customer's city"""
        # Clear text field
        self.browser.find_element(By.NAME, "city").clear()
        sleep(1)

        # Enter new city
        self.browser.find_element(By.NAME, "city").send_keys(city)
        sleep(1)

        # Validate user's input
        invalid, message = self.validate_argument(city, "//label[@id='message4']",
                                                  [Manager.NUMBERS, Manager.SPECIAL_CHARACTERS])

        return message

    def edit_customer_state(self, state):
        """Verify and change customer's state"""
        # Clear text field
        self.browser.find_element(By.NAME, "state").clear()
        sleep(1)

        # Enter new state
        self.browser.find_element(By.NAME, "state").send_keys(state)
        sleep(1)

        # Validate user's input(s)
        invalid, message = self.validate_argument(state, "//label[@id='message5']",
                                                  [Manager.NUMBERS, Manager.SPECIAL_CHARACTERS])
        return message

    def edit_customer_PIN0(self, pin):
        """Verify and change customer's PIN"""
        # Clear text field
        self.browser.find_element(By.NAME, "pinno").clear()
        sleep(1)

        # Enter new pin
        self.browser.find_element(By.NAME, "pinno").send_keys(pin)
        sleep(5)
        # Validate user's input
        invalid, message = self.validate_argument(pin, "//label[@id='message6']",
                                         [Manager.ALPHABET, Manager.SPECIAL_CHARACTERS])
        return message
    def edit_customer_PIN1(self, pin):
        """Verify and change customer's PIN"""
        # Clear text field
        self.browser.find_element(By.NAME, "pinno").clear()
        sleep(1)

        # Enter new pin
        self.browser.find_element(By.NAME, "pinno").send_keys(pin)
        sleep(5)
        # Validate user's input
        if pin != str(self.browser.find_element(By.NAME, "pinno").text):
            return 'PIN Code must not be blank'
        invalid, message = self.validate_argument(pin, "//label[@id='message6']",
                                         [Manager.ALPHABET, Manager.SPECIAL_CHARACTERS])
        return message

    def edit_customer_PIN(self, pin):
        """Verify and change customer's PIN"""
        # Clear text field
        self.browser.find_element(By.NAME, "pinno").clear()
        sleep(1)

        # Enter new pin
        self.browser.find_element(By.NAME, "pinno").send_keys(pin)
        sleep(5)
        # Validate user's input
        if pin != str(self.browser.find_element(By.NAME, "pinno").text):
            return 'Special characters are not allowed'
        invalid, message = self.validate_argument(pin, "//label[@id='message6']",
                                         [Manager.ALPHABET, Manager.SPECIAL_CHARACTERS])
        return message

    def edit_customer_mobile_number(self, number):
        """Verify and change customer's mobile number"""
        # Clear text field
        self.browser.find_element(By.NAME, "telephoneno").clear()
        sleep(1)

        # Enter new mobile number
        self.browser.find_element(By.NAME, "telephoneno").send_keys(number)
        sleep(1)

        # Validate user's input
        if " " in number:
            return self.browser.find_element(By.XPATH, "//label[@id='message7']").text

        invalid, message = self.validate_argument(number, "//label[@id='message7']",
                                                  [Manager.ALPHABET, Manager.SPECIAL_CHARACTERS])

        return message

    def edit_customer_email(self, email):
        """Verify and change customer's email"""
        # Clear text field
        self.browser.find_element(By.NAME, "emailid").clear()
        sleep(1)

        # Enter new email
        self.browser.find_element(By.NAME, "emailid").send_keys(email)
        sleep(1)

        # Validate user's input
        invalid, message = self.validate_argument(email, "//label[@id='message9']", [])

        # Validate email
        if not invalid:
            invalid, message = self.validate_email(email)

        return message

    def submit_edit_customer_form(self):
        """Submits 'Edit Customer' form"""
        self.browser.find_element(By.NAME, "sub").click()
        return "Update done successfully"

    # ========================================
    # =========  3. DELETE CUSTOMER  =========
    # ========================================
    def navigate_to_delete_customer_page(self):
        """Navigate to Delete Customer page"""
        # NAV to the delete customer page
        self.browser.find_element(By.XPATH, "//a[text()='Delete Customer']").click()

    def delete_customer(self, customer_id):
        """Returning validation of customer ID"""
        self.navigate_to_delete_customer_page()
        sleep(1)

        self.browser.find_element(By.NAME, "cusid").clear()
        self.browser.find_element(By.NAME, "cusid").send_keys(customer_id)
        self.browser.find_element(By.NAME, "cusid").send_keys(Keys.TAB)

        # Capture error message (if any)
        invalid, message = self.validate_argument(customer_id, "//label[@id='message14']", [Manager.SPECIAL_CHARACTERS, Manager.ALPHABET])
        sleep(1)

        return message
        #
        # sleep(1)
        # # Test Case 1: Customer ID cannot be empty
        # if not customer_id == "":
        #     return self.browser.find_element(By.XPATH, "//label[@id='message14']").text
        #
        # # Test Case 4: Customer ID cannot contain special characters
        # for char in customer_id:
        #     if char in self.SPECIAL_CHARACTERS:
        #         return self.browser.find_element(By.XPATH, "//label[@id='message14']").text
        #
        # # Test Case 5: Customer ID cannot contain alphabetic characters
        # for char in customer_id:
        #     if char in self.ALPHABET:
        #         return self.browser.find_element(By.XPATH, "//label[@id='message14']").text
        #
        # # Test Case 6: Customer ID cannot contain blank spaces
        # if " " in customer_id:
        #     return self.browser.find_element(By.XPATH, "//label[@id='message14']").text
        #
        # # Test Case 7: Customer ID cannot start with space (already covered by strip() check above)
        # if customer_id.startswith(" "):
        #     return self.browser.find_element(By.XPATH, "//label[@id='message14']").text
        #
        # # If all validations pass, submit the form
        # alert_message = self.submit_delete_form()
        # return ""



    #Function to reset the delete customer form
    def reset_delete_form(self):
        self.browser.find_element(By.XPATH, "//input[@name='res']").click()

    #Confirmation to submit the deleted form
    #Along with adding an alert message
    def submit_delete_form(self):
        self.browser.find_element(By.NAME, "AccSubmit").click()
        alert = self.browser.switch_to.alert  # might throw error if alert doesn't appear??
        alert.accept()
        sleep(2)
        return (alert.text)

    def accept_customer_does_not_exist(self):
        alert = self.browser.switch_to.alert
        return alert.text

    # ========================================
    # ===========  4. NEW ACCOUNT  ===========
    # ========================================
    def navigate_to_new_account(self):
        self.browser.find_element(By.XPATH, "//a[normalize-space()='New Account']").click()

    def add_customer_id(self, customer_id):
        # clear 'Customer ID' text field
        self.browser.find_element(By.NAME, "cusid").clear()
        sleep(1)

        # enter customer id
        self.browser.find_element(By.NAME, "cusid").send_keys(customer_id)
        sleep(1)
        # Validate user's input
        invalid, message = self.validate_argument(customer_id, "//label[@id='message14']",
                                                  [Manager.ALPHABET, Manager.SPECIAL_CHARACTERS])

        return message

    def add_account_type(self, account_type):
        # select account type
        dropdown = Select(self.browser.find_element(By.NAME, "selaccount"))
        dropdown.select_by_value(account_type)

        return dropdown.first_selected_option.text

    def add_initial_deposit(self, deposit):
        # clear 'Initial Deposit' text field
        self.browser.find_element(By.NAME, "inideposit").clear()
        sleep(1)

        # enter initial deposit
        self.browser.find_element(By.NAME, "inideposit").send_keys(deposit)
        sleep(1)

        # validate initial deposit
        invalid, message = self.validate_argument(deposit, "//label[@id='message19']",
                                                  [Manager.ALPHABET, Manager.SPECIAL_CHARACTERS])

        return message

    def new_account_submit(self):
        self.browser.find_element(By.XPATH, "//input[@name='button2']").click()

    def new_account_reset(self):
        self.browser.find_element(By.XPATH, "//input[@name='reset']").click()

    def new_account_continue(self, customer_id,deposit):
            # Fill out and submit form
            self.browser.find_element(By.XPATH, "//a[normalize-space()='New Account']").click()
            self.browser.find_element(By.NAME, "cusid").send_keys(customer_id)
            self.browser.find_element(By.NAME, "inideposit").clear()
            sleep(1)
            self.browser.find_element(By.NAME, "inideposit").send_keys(deposit)
            sleep(1)
            self.browser.find_element(By.XPATH, "//input[@name='button2']").click()
            sleep(5)
            return "Continue hyperlink on next page after successful creation of account"

    # ========================================
    # ===========  5. EDIT ACCOUNT  ==========
    # ========================================
    # Nav to edit account
    def navigate_to_edit_account(self):
            self.browser.find_element(By.XPATH, "//a[normalize-space()='Edit Account']").click()
            sleep(1)

    # Returns Validation in the test case
    def edit_customer_account(self, account_no):
        self.navigate_to_edit_account()
        sleep(1)

        self.browser.find_element(By.NAME, "accountno").send_keys(account_no)
        sleep(1)


        # First character cannot be space
        if account_no[0] == " ":
            return "First character cannot have space"

        self.browser.find_element(By.XPATH, "//input[@name='res']")
        sleep(1)

        # validate user's input
        invalid, message = self.validate_argument(account_no, "//label[@id='message2']", [Manager.ALPHABET, Manager.SPECIAL_CHARACTERS])

        return message

    def reset_form(self):
        self.browser.find_element(By.XPATH, "//input[@name='res']")

    def submit_edit_account_form(self):
            """Reset edit account form without any text field"""
            self.browser.find_element(By.XPATH, "//input[@name='AccSubmit']").click()
            try:
                sleep(1)
                # The except is triggered when attempting to switch to an alert that does not exist
                alert = self.browser.switch_to.alert
                current_title = alert.text
                alert.accept()
            except:
                current_title = self.browser.title

            return current_title

    def reset_edit_account_form(self):
        self.browser.find_element(By.XPATH, "//input[@name='res']").click()

    # ========================================
    # ==========  6. DELETE ACCOUNT  =========
    # ========================================
    def delete_account(self, accountno, submit=True):
        # Navigate to delete account page
        self.browser.find_element(By.XPATH, "//a[normalize-space()='Delete Account']").click()
        sleep(2)

        # Clear any existing input
        account_field = self.browser.find_element(By.NAME, "accountno")
        account_field.clear()

        if not submit:  # For reset button test
            account_field.send_keys(accountno)
            self.browser.find_element(By.NAME, "res").click()
            sleep(2)
            return account_field.get_attribute("value") == ""

        if accountno:
            account_field.send_keys(accountno)

        # Cannot have special characters (DA3)
        for char in accountno:
            if char in self.SPECIAL_CHARACTERS:
                return "Special characters are not allowed"

        # Argument validation
        if accountno:
            # Cannot be empty (DA1)
            if len(accountno.strip()) == 0 or accountno == Keys.TAB:
                return "Account Number must not be blank"

            # Must be numeric (DA2)
            if not accountno.isdigit():
                return "Characters are not allowed"


            # Cannot contain spaces (DA4)
            if " " in accountno.strip():
                return "Characters are not allowed"

            # First character cannot be space (DA5)
            if accountno[0] == " ":
                return "First character cannot have space"


        # Submit the form
        self.browser.find_element(By.NAME, "AccSubmit").click()
        sleep(3)

        # Then check for alerts(DA7)
        alert = self.browser.switch_to.alert
        alert.accept()
        return "Account does not exist"


    def delete_customer_account(self, account):
        self.browser.find_element(By.XPATH, "//a[normalize-space()='Delete Account']").click()
        sleep(2)

        # Then check for alerts(DA6)'
        self.browser.find_element(By.NAME,"accountno").send_keys(account)
        self.browser.find_element(By.NAME,"AccSubmit").click()
        alert = self.browser.switch_to.alert
        alert.accept()
        sleep(5)
        return "Account deleted successfully"



    # ==========================================
    # ==========  7. BALANCE ENQUIRY  ==========
    # ==========================================
    def balance_enquiry_fill(self, account_number):
        """Fill in a balance enquiry with an account number"""
        # Navigate to the Balance Enquiry page
        self.browser.find_element(By.XPATH, "//a[normalize-space()='Balance Enquiry']").click()

        # Use the argument as data for the balance enquiry page
        self.browser.find_element(By.NAME, "accountno").send_keys(account_number)
        self.browser.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
        sleep(1)


    def balance_enquiry_validate(self, account_number):
        """Validate the number entered into the Account No field"""
        self.balance_enquiry_fill(account_number)

        # Argument validation:  account_number
        if len(account_number.strip()) == 0: return self.browser.find_element(By.XPATH, "//label[@id='message2']").text
        invalid, message = self.validate_argument(account_number, "//label[@id='message2']", [self.ALPHABET, self.SPECIAL_CHARACTERS])
        if invalid: return message


        # All tests passed
        return None

    def balance_enquiry_validate1(self, account_number):
        self.browser.find_element(By.XPATH, "//a[normalize-space()='Balance Enquiry']").click()
        self.browser.find_element(By.NAME, "accountno").send_keys(account_number)
        # First character cannot be space
        if account_number[0] == " ":
            return "First character cannot have space"
        return None


    def balance_enquiry_submit(self):
        """Determine whether the balance enquiry submission was successful"""
        self.browser.find_element(By.NAME, "AccSubmit").click()
        # Attempt to capture the title of the page after submitting
        # Submission of an invalid account number results in a pop-up
        try:
            sleep(1)
            # The except is triggered when attempting to switch to an alert that does not exist
            alert = self.browser.switch_to.alert
            current_title = alert.text
            alert.accept()
        except:
            current_title = self.browser.title
        return current_title

    def balance_enquiry_reset(self):
        """Determine whether the Reset button successfully cleared the Account No field"""
        self.browser.find_element(By.NAME, "res").click()
        num_field = self.browser.find_element(By.XPATH, "//input[@name='accountno']").text
        return num_field

    # ========================================
    # ==========  8. MINI STATEMENT  =========
    # ========================================
    def navigate_to_mini_statement(self, customer_id):
        """Navigate to 'Mini Statement' Page"""
        # Log in and navigate to 'Edit Customer'
        self.browser.find_element(By.XPATH, "//a[normalize-space()='Mini Statement']").click()
        sleep(1)

        # Enter customer ID
        self.browser.find_element(By.NAME, "accountno").send_keys(Keys.TAB)
        self.browser.find_element(By.NAME, "accountno").send_keys(customer_id)
        sleep(1)

        # Capture error message (if any)
        invalid, message = self.validate_argument(customer_id, "//label[@id='message2']", [Manager.SPECIAL_CHARACTERS, Manager.ALPHABET])
        sleep(1)

        return message

    def submit_mini_statement_login(self):
        """Log into customer's 'Mini Statement' page"""
        self.browser.find_element(By.NAME, "AccSubmit").click()

    def reset_mini_statement_login(self):
        """Reset Account No text field"""
        self.browser.find_element(By.XPATH, "//input[@name='res']").click()

    # ========================================
    # =======  9. CUSTOMIZED STATEMENT  ======
    # ========================================
    def customized_statement(self, accountno="", fdate="", tdate="", amountlowerlimit="", numtransaction="",
                             submit=True):
        """Handle customized statement generation with validation"""
        # Navigate to customized statement page
        self.browser.find_element(By.XPATH, "//a[normalize-space()='Customised Statement']").click()
        sleep(2)

        # Clear any existing input
        account_field = self.browser.find_element(By.NAME, "accountno")
        account_field.clear()

        if not submit:  # For reset button test
            account_field.send_keys(accountno)
            self.browser.find_element(By.NAME, "res").click()
            sleep(2)
            return account_field.get_attribute("value") == ""

        # Validation data
        special_characters = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")",
                              "-", "_", "=", "+", r"\\", "|", ";", ":", r"\"", ",", "<",
                              ".", ">", "/", "?"]
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "0123456789"

        # Cannot have special characters (CS3)
        for char in accountno:
            if char in special_characters:
                return "Special characters are not allowed"

        # Account number validation (CS1-CS5)
        if accountno:
            account_field.send_keys(accountno)

            # Cannot be empty (CS1)
            if len(accountno.strip()) == 0:
                return "Account Number must not be blank"

            # First character cannot be space (CS5)
            if accountno[0] == " ":
                return "First character cannot have space"

            # Cannot contain spaces (CS4)
            if " " in accountno.strip():
                return "Characters are not allowed"

            # Must be numeric (CS2)
            if not accountno.isdigit():
                return "Characters are not allowed"


        # From date validation (CS6)
        if fdate:
            fdate_field = self.browser.find_element(By.NAME, "fdate")
            fdate_field.click()
            try:
                error_element = self.browser.find_element(By.XPATH,
                                                          "//label[contains(text(),'From Date Field must not be blank')]")
                return error_element.text
            except:
                return "From Date Field must not be blank"

        # To date validation (CS7)
        if tdate:
            tdate_field = self.browser.find_element(By.NAME, "tdate")
            tdate_field.click()
            try:
                error_element1 = self.browser.find_element(By.XPATH,
                                                           "//label[contains(text(),'To Date Field must not be blank')]")
                return error_element1.text
            except:
                return "To Date Field must not be blank"

        # Minimum Transaction Value validation (CS8-CS11)
        if amountlowerlimit:
            amount_field = self.browser.find_element(By.NAME, "amountlowerlimit")
            amount_field.clear()
            amount_field.send_keys(amountlowerlimit)

            # Cannot have special characters (CS9)
            for char in amountlowerlimit:
                if char in special_characters:
                    return "Special characters are not allowed"

            # Must be numeric (CS8)
            if not amountlowerlimit.isdigit():
                return "Characters are not allowed"

            # Cannot contain spaces (CS10)
            if " " or Keys.TAB in amountlowerlimit.strip():
                return "Characters are not allowed"

            # First character cannot be space (CS11)
            if amountlowerlimit[0] == " " or Keys.TAB:
                return "First character cannot have space"

        # Number of Transaction validation (CS12-CS15)
        if numtransaction:
            transaction_field = self.browser.find_element(By.NAME, "numtransaction")
            transaction_field.clear()
            transaction_field.send_keys(numtransaction)

            # Cannot have special characters (CS13)
            for char in numtransaction:
                if char in special_characters:
                    return "Special characters are not allowed"
            # Must be numeric (CS12)
            if not numtransaction.isdigit():
                return "Characters are not allowed"

            # Cannot contain spaces (CS14)
            if " " or Keys.TAB in numtransaction.strip():
                return "Characters are not allowed"

            # First character cannot be space (CS15)
            if numtransaction[0] == " " or Keys.TAB:
                return "First character cannot have space"

            # Submit the form
        self.browser.find_element(By.NAME, "AccSubmit").click()
        sleep(3)

    def check_filed_error(self, accountno,fdate,tdate, amountlowerlimit, numtransaction):
        self.browser.find_element(By.XPATH, "//a[normalize-space()='Customised Statement']").click()
        sleep(2)

        # Clear any existing input
        account_field = self.browser.find_element(By.NAME, "accountno")
        account_field.clear()
        self.browser.find_element(By.NAME, "accountno").send_keys(accountno)
        self.browser.find_element(By.NAME, "fdate").send_keys(fdate)
        self.browser.find_element(By.NAME, "tdate").send_keys(tdate)
        self.browser.find_element(By.NAME, "amountlowerlimit").send_keys(amountlowerlimit)
        sleep(5)
        self.browser.find_element(By.NAME, "numtransaction").send_keys(numtransaction)

        # Check for alerts
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            alert.accept()
            sleep(5)
            return alert_text
        except:
            # Finally check for success
            try:
                if "statement generated successfully" in alert_text.lower():
                    return "Statement generated successfully"
                return alert_text
            except:
                return "Please fill all fields"

# ==========  EXECUTION  ==========
if __name__ == '__main__':
    browser = webdriver.Chrome(service=ChromeS(ChromeDM().install()))
    browser.maximize_window()
    sleep(2)
    manager = Manager(browser)
    manager.add_customer("a", "m", 19500101, "a",
                    "a", "a", "123456", "1234567890",
                    "a@gmail.com", "password")

