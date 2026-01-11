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