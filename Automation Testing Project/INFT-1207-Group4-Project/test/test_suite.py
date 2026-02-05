# File:     test_suite.py
# Type:     Python (.py) file
# Authors:  Kyle Angeles, Mathuran Chandramohan, Pratig Thapa,  Maxximillion Thomas
# Date:     Aug 7, 2025
# Desc.:    Perform tests on a dummy banking website to simulate Manager privileges

# ==========  IMPORTS  ==========
import unittest
from test_manager import TestManager

# ==========  CONSTANTS  ==========
MANAGER_TESTS = {
    '1': [
        "test_NC1", "test_NC2", "test_NC3", "test_NC4", "test_NC5",
        "test_NC6", "test_NC7", "test_NC8", "test_NC9", "test_NC10",
        "test_NC11", "test_NC12", "test_NC13", "test_NC14", "test_NC15",
        "test_NC16", "test_NC17", "test_NC18", "test_NC19", "test_NC20",
        "test_NC21", "test_NC22", "test_NC23", "test_NC24", "test_NC25",
        "test_NC26", "test_NC27"
    ],
    '2': [
        "test_EC1", "test_EC2", "test_EC3", "test_EC4", "test_EC5",
        "test_EC6", "test_EC7", "test_EC8", "test_EC9", "test_EC10",
        "test_EC11", "test_EC12", "test_EC13", "test_EC14", "test_EC15",
        "test_EC16", "test_EC17", "test_EC18", "test_EC19", "test_EC20"
    ],
    '3': [
        "test_DC1", "test_DC2", "test_DC3", "test_DC4", "test_DC5",
        "test_DC6", "test_DC7", "test_DC8"
    ],
    '4': [
        "test_NA1", "test_NA2", "test_NA3", "test_NA4", "test_NA5",
        "test_NA6", "test_NA7", "test_NA8", "test_NA9", "test_NA10",
        "test_NA11", "test_NA12", "test_NA13", "test_NA14", "test_NA15",
        "test_NA16"
    ],
    '5': [
        "test_EA1", "test_EA2", "test_EA3", "test_EA4", "test_EA5",
        "test_EA6", "test_EA7", "test_EA8"
    ],
    '6': [
        "test_DA1", "test_DA2", "test_DA3", "test_DA4", "test_DA5",
        "test_DA6", "test_DA7", "test_DA8"
    ],
    '7': [
        "test_BE1", "test_BE2", "test_BE3", "test_BE4", "test_BE5",
        "test_BE6", "test_BE7"
    ],
    '8': [
        "test_MS1", "test_MS2", "test_MS3", "test_MS4", "test_MS5",
        "test_MS6", "test_MS7", "test_MS8"
    ],
    '9': [
        "test_CS1", "test_CS2", "test_CS3", "test_CS4", "test_CS5",
        "test_CS6", "test_CS7", "test_CS8", "test_CS9", "test_CS10",
        "test_CS11", "test_CS12", "test_CS13", "test_CS14", "test_CS15",
        "test_CS16", "test_CS17"
    ]
}

MENU = '''Please select one of the following testing options:
    - '1' for New Customer
    - '2' for Edit Customer
    - '3' for Delete Customer
    - '4' for New Account
    - '5' for Edit Account
    - '6' for Delete Account
    - '7' for Balance Enquiry
    - '8' for Mini Statement
    - '9' for Customized Statement
    - 'X' to quit
'''

# ==========  FUNCTION DEFINITION  ==========
def my_suite():
    """Run the selected test suite based on user input"""
    while True:
        print(MENU)
        option = input("Your selection: ").strip().upper()

        # Execute user's option
        if option == 'X':
            input("Press <Enter> to exit the program.")
            break
        elif option in MANAGER_TESTS:
            # Create new test suite
            suite = unittest.TestSuite()

            # Add chosen module's test cases to suite
            for test_case in MANAGER_TESTS[option]:
                suite.addTest(TestManager(test_case))

            # Execute test suite
            runner = unittest.TextTestRunner()
            print(runner.run(suite))
        else:
            print("Invalid input. Please try again.")

# ==========  EXECUTION  ==========
if __name__ == "__main__":
    my_suite()
    exit()