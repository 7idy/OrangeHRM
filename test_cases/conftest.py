# This file contains shared fixtures for Selenium WebDriver tests using pytest.
import  pytest
from  selenium import webdriver
from  selenium.webdriver.chrome.options import Options
from  pytest_metadata.plugin import metadata_key

# Fixture to set up the WebDriver
# @pytest.fixture()
# def setup():
#     driver = webdriver.Chrome()
#     return driver

# add a command line option to specify the browser
# hook function to add command line options
def pytest_addoption(parser: pytest.Parser):
    parser.addoption(
        "--browser",
        action="store", # store the value
        default="chrome",
        help="Specified the browser: chrome, edge or firefox"    # pytest --help
    )

# fixture to get the browser choice from command line
@pytest.fixture()
def browser(request: pytest.FixtureRequest):
    return request.config.getoption("--browser")

# fixture to set up the WebDriver based on the browser choice
@pytest.fixture()
def setup(browser):
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-notifications")
    options.add_argument("--guest")
    options.add_experimental_option("prefs",{
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
        })

    if browser == "chrome":
        driver = webdriver.Chrome(options=options)
    elif browser == "edge":
        driver = webdriver.Edge()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    yield driver # return the driver to the test and wait for the test to complete
    driver.quit()

# hook to add metadata to the test report (environment info)
def pytest_configure(config: pytest.Config):
    config.stash[metadata_key] ["Project Name"] = "OrangeHRM"
    config.stash[metadata_key] ["Test Module Name"] = "Login"
    config.stash[metadata_key] ["Tester"] = "Bao"

# hook to modify metadata in the test report (remove unwanted fields)
@pytest.hookimpl(optionalhook=True) # 'optionalhook' to avoid errors if pytest-metadata is not installed
def pytest_metadata(metadata: dict):
    metadata.pop("Plugins", None) # remove Plugins field, 'None' to avoid KeyError if field not present

# hook to set the title of the HTML report
def pytest_html_report_title(report):
    report.title = "OrangeHRM Test Automation Report"