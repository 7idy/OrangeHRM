# Description: This module contains the LoginPage class which encapsulates
# the elements and actions related to the login page of a web application.
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

class LoginPage:
    # locators
    TEXTBOX_USERNAME_NAME = "username"
    TEXTBOX_PASSWORD_NAME = "password"
    BUTTON_LOGIN_XPATH = "//button[@type='submit']"
    USER_DROPDOWN_NAME = "oxd-userdropdown-name"
    LOGOUT_LINK_XPATH = "//a[text()='Logout']"
    DASHBOARD_HEADER_XPATH = "//span[contains(@class,'oxd-topbar-header-breadcrumb')]/h6"

    # constructor
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # actions (methods)
    # enter username
    def enter_username(self, username):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.NAME, self.TEXTBOX_USERNAME_NAME).clear()
        self.driver.find_element(By.NAME, self.TEXTBOX_USERNAME_NAME).send_keys(username)

    # enter password
    def enter_password(self, password):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.NAME, self.TEXTBOX_PASSWORD_NAME).clear()
        self.driver.find_element(By.NAME, self.TEXTBOX_PASSWORD_NAME).send_keys(password)

    # click login button
    def click_login(self):
        self.driver.find_element(By.XPATH, self.BUTTON_LOGIN_XPATH).click()

    # logout
    def logout(self):
        self.driver.find_element(By.CLASS_NAME, self.USER_DROPDOWN_NAME).click()
        self.driver.find_element(By.XPATH, self.LOGOUT_LINK_XPATH).click()

    # check if dashboard is displayed
    def is_dashboard_displayed(self):
        # True if dashboard header element is found, else False
        try:
            return self.driver.find_element(By.XPATH, self.DASHBOARD_HEADER_XPATH).is_displayed()
        except NoSuchElementException:
            return False