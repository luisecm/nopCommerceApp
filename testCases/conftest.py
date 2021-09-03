import pytest
from selenium import webdriver

@pytest.fixture
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path="/Users/luisecm/Documents/Selenium/Drivers/chromedriver")
        print("Launching Chrome browser.....")
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path="/Users/luisecm/Documents/Selenium/Drivers/geckodriver")
        print("Launching Firefox browser.....")
    else:
        driver = webdriver.Chrome(executable_path="/Users/luisecm/Documents/Selenium/Drivers/chromedriver")
        print("Not a valid browser... Opening in default browser (Chrome)")
    return driver

def pytest_addoption(parser): #This will get the value from CLI/ Hooks
    parser.addoption("--browser")

@pytest.fixture
def browser(request): #This will return the Browser value to setup method
    return request.config.getoption("--browser")

"""
    Generate PyTest HTML Report 
"""

#Hook for adding environment info to HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Luis Cardeña'

#Hook for delete/modify environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)