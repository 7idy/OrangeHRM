# This test case verifies the login functionality data-driven execution using data from an Excel file.
from pages.Login_Page import LoginPage
from utils.read_properties import ReadConfig
from utils.logger import LoggerMaker
from utils import excel_utils

class TestLogin02:
    base_URL = ReadConfig.get_base_url()
    logger = LoggerMaker.log_generator()
    excel_path = ".//test_data//login_data.xlsx"
    status_list = [] # to store pass/fail status of each test iteration

    # Test case to verify login with valid credentials using data-driven
    def test_valid_login_data_driven(self, setup):
        self.logger.info("test_valid_login_data_driven started")
        self.driver = setup
        self.driver.get(self.base_URL)
        self.lp = LoginPage(self.driver)

        self.rows = excel_utils.get_row_count(self.excel_path, "Sheet1")
        print("Number of rows in Excel: ", self.rows)
        self.status_list = [] # reset status list for this test case
        for r in range(2, self.rows + 1): # start from row 2 to skip header
            self.username = excel_utils.read_data(self.excel_path, "Sheet1", r, 1) # read username
            self.password = excel_utils.read_data(self.excel_path, "Sheet1", r, 2) # read password
            self.exp_result = excel_utils.read_data(self.excel_path, "Sheet1", r, 3) # read exp result

            self.lp.enter_username(self.username)
            self.lp.enter_password(self.password)
            self.lp.click_login()

            self.login_status = self.lp.is_dashboard_displayed() # check if dashboard is displayed
            if self.login_status: # if self.login_status is True
                if self.exp_result == "Yes":
                    self.logger.info("Test data driven login PASSED")
                    self.status_list.append("Pass")
                    self.lp.logout()
                else: # if self.exp_result is "No"
                    self.logger.info("Test data driven login FAILED")
                    self.status_list.append("Fail")
            else: # if self.login_status is False
                if self.exp_result == "Yes":
                    self.logger.info("Test data driven login FAILED")
                    self.status_list.append("Fail")
                else: # if self.exp_result is "No"
                    self.logger.info("Test data driven login PASSED")
                    self.status_list.append("Pass")

        print("Status List: ", self.status_list)
        if "Fail" in self.status_list:
            self.logger.info("Test data driven login overall FAILED")
            self.driver.close()
            assert False
        else:
            self.logger.info("Test data driven login overall PASSED")
            assert True
            self.driver.close()