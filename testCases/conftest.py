from selenium import webdriver
import pytest
import pytest_html
from _pytest.config import Config



@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        return driver
        print("Launching Chrome Browser........")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        return driver
        print("Launching Firefox Browser........")
    elif browser == 'edge':
        driver = webdriver.Edge()
        return driver
        print("Launching Edge Browser...........")
    else:
        driver = webdriver.Chrome()
        return driver
        print("Launching Chrome Browser........")


def pytest_addoption(parser):  # This will get the value of CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will retrun the Browser value to set up method
    return request.config.getoption("--browser")


######################PyTest HTML Report#####################

###It is hook for adding environment info to HTML Report
# def pytest_configure(config):
#     config.metadata['Project Name'] = 'nop commerce'
#     config.metadata['Module Name'] = 'Customers'
#     config.metadata['Tester'] = 'Anand'

###It is hook for Delete/Modify environment info to HTML Report

# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)















