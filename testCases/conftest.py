from selenium import webdriver
import pytest
import pytest_html
from _pytest.config import Config
from pytest_metadata.plugin import metadata_key

def pytest_addoption(parser):  # This will get the value of CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will retrun the Browser value to set up method
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome Browser........")
        return driver
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox Browser........")
        return driver
    elif browser == 'edge':
        driver = webdriver.Edge()
        print("Launching Edge Browser...........")
        return driver
    else:
        driver = webdriver.Chrome()
        print("Launching Chrome Browser........")
        return driver


# def pytest_addoption(parser):  # This will get the value of CLI /hooks
#     parser.addoption("--browser")
#
# @pytest.fixture()
# def browser(request):  # This will retrun the Browser value to set up method
#     return request.config.getoption("--browser")


######################PyTest HTML reports#####################

###It is hook for adding environment info to HTML reports
def pytest_configure(config):
    config.stash[metadata_key] ['Project Name'] = 'nop commerce'
    config.stash[metadata_key]['Module Name'] = 'Customers'
    config.stash[metadata_key]['Tester Name'] = 'Anand'
    # config.metadata['Project Name'] = 'nop commerce'
    # config.metadata['Module Name'] = 'Customers'
    # config.metadata['Tester'] = 'Anand'

###It is hook for Delete/Modify environment info to HTML reports
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)















