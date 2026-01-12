from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AddUserPage(BasePage):
    # locators
    LINK_ADMIN_MENU = (By.XPATH, "//a[.//span[normalize-space()='Admin']]") # 'normalize-space' to avoid space issues
    BUTTON_ADD_USER = (By.XPATH, "//button[normalize-space()='Add']")
    DROPDOWN_USER_ROLE = (By.XPATH, "//label[text()='User Role']/following::div[contains(@class,'oxd-select-text')][1]")
    ITEM_USER_ROLE_ADMIN = (By.XPATH, "//div[@role='option']//span[contains(text(),'Admin')]")
    ITEM_USER_ROLE_ESS = (By.XPATH, "//div[@role='option']//span[contains(text(),'ESS')]")
    INPUT_EMPLOYEE_NAME = (By.XPATH, "//label[contains(text(),'Employee Name')]/ancestor::div[contains(@class,'oxd-input')]//input")
    LIST_EMPLOYEE_NAME = (By.XPATH, "(//div[@class='oxd-autocomplete-option']//span)[1]")
    LIST_EMPLOYEE_NAME_NO_RESULT = (By.XPATH, "//div[@role='option' and text()='No Records Found']")
    DROPDOWN_STATUS = (By.XPATH, "//label[contains(text(),'Status')]/following::div[contains(@class,'oxd-select-text')][1]")
    ITEM_STATUS_ENABLED = (By.XPATH, "//div[@role='option']//span[contains(text(),'Enabled')]")
    ITEM_STATUS_DISABLED = (By.XPATH, "//div[@role='option']//span[contains(text(),'Disabled')]")
    INPUT_USERNAME = (By.XPATH, "//label[contains(text(),'Username')]/following::input[contains(@class,'oxd-input')][1]")
    INPUT_PASSWORD = (By.XPATH, "(//input[@type='password'])[1]")
    INPUT_CONFIRM_PASSWORD = (By.XPATH, "(//input[@type='password'])[2]")
    BUTTON_SAVE = (By.XPATH, "//button[@type='submit']")
    TOAST_SUCCESS_MESSAGE = (By.XPATH, "//p[contains(@class, 'oxd-text--toast-message')]")

    # constructor
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    # actions (methods)
    # select user role as admin or ess
    def select_item_user_role(self, role):
        self.do_click(self.DROPDOWN_USER_ROLE)
        if role == "Admin":
            self.do_click(self.ITEM_USER_ROLE_ADMIN)
        else:
            self.do_click(self.ITEM_USER_ROLE_ESS)

        # alternative way:
        # item_role = (By.XPATH, f"//div[@role='option']//span[contains(text(),'{role}')]")
        # self.do_click(item_role)

    # select employee name from the auto-suggest list
    def select_employee_name(self, emp_name):
        self.do_send_keys(self.INPUT_EMPLOYEE_NAME, emp_name)
        self.do_click(self.LIST_EMPLOYEE_NAME)

    # select status as enabled or disabled
    def select_item_status(self, status):
        self.do_click(self.DROPDOWN_STATUS)
        if status == "Enabled":
            self.do_click(self.ITEM_STATUS_ENABLED)
        else:
            self.do_click(self.ITEM_STATUS_DISABLED)

        # alternative way:
        # item_status = (By.XPATH, f"//div[@role='option']//span[contains(text(),'{status}')]")
        # self.do_click(item_status)

    # add new user - include multiple steps
    def add_new_user(self, role, emp_name, status, username, password):
        self.do_click(self.LINK_ADMIN_MENU)
        self.do_click(self.BUTTON_ADD_USER)
        self.select_item_user_role(role)
        self.select_employee_name(emp_name)
        self.select_item_status(status)
        self.do_send_keys(self.INPUT_USERNAME, username)
        self.do_send_keys(self.INPUT_PASSWORD, password)
        self.do_send_keys(self.INPUT_CONFIRM_PASSWORD, password)
        self.do_click(self.BUTTON_SAVE)

    # get toast success message text
    def get_toast_success_message_text(self):
        msg_text = self.get_text(self.TOAST_SUCCESS_MESSAGE) # get the toast message text
        self.wait_until_invisible(self.TOAST_SUCCESS_MESSAGE) # wait until the toast message disappears
        return msg_text