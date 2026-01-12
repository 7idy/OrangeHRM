import time
from utils.logger import LoggerMaker
from pages.add_user_page import AddUserPage
from pages.login_page import LoginPage
from utils.read_properties import ReadConfig

class TestAddUser:
    logger = LoggerMaker.log_generator()
    base_URL = ReadConfig.get_base_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    emp_name = f"baotest{int(time.time())}" # unique employee name using timestamp

    def test_add_user(self, setup):
        self.logger.info("----- test_add_user started -----")
        self.driver = setup
        self.driver.get(self.base_URL)

        self.lp = LoginPage(self.driver)
        self.lp.enter_username(self.username)
        self.lp.enter_password(self.password)
        self.lp.click_login()
        self.logger.info("login successful")

        self.au = AddUserPage(self.driver)
        self.au.add_new_user("ESS", "b", "Enabled", self.emp_name, "bao12345")

        act_toast_msg = self.au.get_toast_success_message_text()
        exp_toast_msg = "Successfully Saved"
        if act_toast_msg != exp_toast_msg:
            self.driver.save_screenshot(".//screenshots//test_add_user.png")
            self.logger.info("test_add_user FAILED (toast message not matched)")
        # if act_toast_msg != exp_toast_msg, show Expected toast message... but got...
        assert act_toast_msg == exp_toast_msg, f"Expected toast message: '{exp_toast_msg}, but got: '{act_toast_msg}'"
        self.logger.info("add new user successfully")