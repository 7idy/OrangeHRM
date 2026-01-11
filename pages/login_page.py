# Description: This module contains the LoginPage class which encapsulates
# the elements and actions related to the login page of a web application.
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage): # LoginPage inherits from BasePage
    # locators
    TEXTBOX_USERNAME = (By.NAME, "username")
    TEXTBOX_PASSWORD = (By.NAME, "password")
    BUTTON_LOGIN = (By.XPATH, "//button[@type='submit']")
    USER_DROPDOWN = (By.CLASS_NAME, "oxd-userdropdown-name")
    LOGOUT_LINK = (By.XPATH, "//a[text()='Logout']")
    DASHBOARD_HEADER = (By.XPATH, "//span[contains(@class,'oxd-topbar-header-breadcrumb')]/h6")
    ERROR_MESSAGE = (By.XPATH, "//div[contains(@class,'oxd-alert')]/p")

    # constructor
    def __init__(self, driver: WebDriver):
        super().__init__(driver) # call the constructor of BasePage

    # actions (methods)
    # enter username
    def enter_username(self, username):
        self.do_send_keys(self.TEXTBOX_USERNAME, username)

    # enter password
    def enter_password(self, password):
        self.do_send_keys(self.TEXTBOX_PASSWORD, password)

    # click login button
    def click_login(self):
        self.do_click(self.BUTTON_LOGIN)

    # logout
    def logout(self):
        self.do_click(self.USER_DROPDOWN)
        self.do_click(self.LOGOUT_LINK)

    # get dashboard header text
    def get_dashboard_header_text(self):
        return self.get_text(self.DASHBOARD_HEADER)

    # get error message text
    def get_error_message_text(self):
        return self.get_text(self.ERROR_MESSAGE)

    # check if dashboard is displayed
    def is_dashboard_displayed(self):
        return self.is_element_visible(self.DASHBOARD_HEADER) # return the WebElement if visible, else False