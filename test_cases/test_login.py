# This test case module verifies the login functionality of the OrangeHRM application.
from selenium.webdriver.common.by import By
from pages.Login_Page import LoginPage
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
        self.logger.info("TestLogin01:")
        self.logger.info("test_title_verification started")
        self.driver = setup
        self.driver.get(self.base_URL)
        self.driver = setup
        self.driver.get(self.base_URL)
        act_title = self.driver.title
        exp_title = "OrangeHRM"     # expected title

        # try:
        #     assert act_title == exp_title, f"Expected title: '{exp_title}', but got: '{act_title}'"
        # finally:
        #     self.driver.close()

        if act_title == exp_title:
            self.logger.info("test_title_verification PASSED (title matched)")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".//screenshots//test_title_verification.png")
            self.logger.info("test_title_verification FAILED (title not matched)")
            self.driver.close()
            assert False

    # Test case to verify login with valid credentials
    def test_valid_login(self, setup):
        self.logger.info("test_valid_login started")
        self.driver = setup
        self.driver.get(self.base_URL)
        self.lp = LoginPage(self.driver)
        self.lp.enter_username(self.username)
        self.lp.enter_password(self.password)
        self.lp.click_login()
        act_dashboard = self.driver.find_element(By.XPATH, "//span[contains(@class,'oxd-topbar-header-breadcrumb')]/h6").text
        exp_dashboard = "Dashboard"

        # try:
        #     assert act_dashboard == exp_dashboard, f"Expected dashboard text: '{exp_dashboard}, but got: '{act_dashboard}'"
        # finally:
        #     self.driver.close()

        if act_dashboard == exp_dashboard:
            self.logger.info("test_valid_login PASSED (login successful)")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".//screenshots//test_valid_login.png")
            self.logger.info("test_valid_login FAILED (login failed)")
            self.driver.close()
            assert False

    # Test case to verify login with invalid credentials
    def test_invalid_login(self, setup):
        self.logger.info("test_invalid_login started")
        self.driver = setup
        self.driver.get(self.base_URL)
        self.lp = LoginPage(self.driver)
        self.lp.enter_username(self.invalid_username)
        self.lp.enter_password(self.password)
        self.lp.click_login()
        act_err_msg = self.driver.find_element(By.XPATH, "//div[contains(@class,'oxd-alert')]/p").text
        exp_err_msg = "Invalid credentials"

        # try:
        #     assert act_err_msg == exp_err_msg, f"Expected error message: '{exp_err_msg}', but got: '{exp_err_msg}'"
        # finally:
        #     self.driver.close()

        if act_err_msg == exp_err_msg:
            self.logger.info("test_invalid_login PASSED (error message matched)")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".//screenshots//test_invalid_login.png")
            self.logger.info("test_invalid_login FAILED (error message not matched)")
            self.driver.close()
            assert False