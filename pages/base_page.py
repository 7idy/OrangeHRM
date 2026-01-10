from selenium.common import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    # constructor
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10) # wait max 10 seconds

    # actions (methods)
    # send keys to an element
    def do_send_keys(self, locator, text):
        elm = self.wait.until(EC.visibility_of_element_located(locator))
        elm.clear()
        elm.send_keys(text)

    # click an element
    def do_click(self, locator):
        elm = self.wait.until(EC.element_to_be_clickable(locator))
        elm.click()

    # get text of an element
    def get_text(self, locator):
        elm = self.wait.until(EC.visibility_of_element_located(locator))
        return elm.text

    # check if an element is visible
    def is_element_visible(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            return False