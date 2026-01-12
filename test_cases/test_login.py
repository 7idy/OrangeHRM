# This test case module verifies the login functionality of the OrangeHRM application.
from pages.login_page import LoginPage
from utils.read_properties import ReadConfig
from utils.logger import LoggerMaker

class TestLogin01:
    base_URL = ReadConfig.get_base_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    invalid_username = ReadConfig.get_invalid_username()
    logger = LoggerMaker.log_generator()

    # Test case to verify the title of the login page
    def test_title_verification(self, setup):
        self.logger.info("----- test_title_verification started -----")
        self.driver = setup
        self.driver.get(self.base_URL)

        act_title = self.driver.title   # actual title
        exp_title = "OrangeHRM"     # expected title
        # if act_title != exp_title, show Expected title... but got...
        assert act_title == exp_title, f"Expected title: '{exp_title}', but got: '{act_title}'"
        self.logger.info("test_title_verification PASSED (title matched)")

    # Test case to verify login with valid credentials
    def test_valid_login(self, setup):
        self.logger.info("----- test_valid_login started -----")
        self.driver = setup
        self.driver.get(self.base_URL)

        self.lp = LoginPage(self.driver)
        self.lp.enter_username(self.username)
        self.lp.enter_password(self.password)
        self.lp.click_login()

        act_dashboard = self.lp.get_dashboard_header_text()
        exp_dashboard = "Dashboard"
        if act_dashboard != exp_dashboard:
            self.driver.save_screenshot(".//screenshots//test_valid_login.png")
            self.logger.info("test_valid_login FAILED (dashboard not matched)")
        # if act_dashboard != exp_dashboard, show Expected dashboard text... but got...
        assert act_dashboard == exp_dashboard, f"Expected dashboard text: '{exp_dashboard}, but got: '{act_dashboard}'"
        self.logger.info("test_valid_login PASSED (dashboard text matched)")

    # Test case to verify login with invalid credentials
    def test_invalid_login(self, setup):
        self.logger.info("----- test_invalid_login started -----")
        self.driver = setup
        self.driver.get(self.base_URL)

        self.lp = LoginPage(self.driver)
        self.lp.enter_username(self.invalid_username)
        self.lp.enter_password(self.password)
        self.lp.click_login()

        act_err_msg = self.lp.get_error_message_text()
        exp_err_msg = "Invalid credentials"
        if act_err_msg != exp_err_msg:
            self.driver.save_screenshot(".//screenshots//test_invalid_login.png")
            self.logger.info("test_invalid_login FAILED (error message not matched)")
        # if act_err_msg != exp_err_msg, show Expected error message... but got...
        assert act_err_msg == exp_err_msg, f"Expected error message: '{exp_err_msg}', but got: '{exp_err_msg}'"
        self.logger.info("test_invalid_login PASSED (error message matched)")