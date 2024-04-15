import selenium
import time
import pytest
from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomer import addCustomer
from pageObjects.searchCustomerPage import searchCustomer
from utilities.customLogger import LogGen

class Test_SearchCustomerByEmail_005:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.logger.info("**** Test_SearchCustomerByEmail_005 ******* ")

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("**** Navigating to Add Customer Page ******* ")

        self.addcust=addCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.logger.info("**** In  Search  Customer Landing  Page ******* ")

        self.searchCust=searchCustomer(self.driver)
        self.searchCust.setFirstName("raj")
        self.searchCust.clickSearch()

        time.sleep(4)

        self.logger.info("**** Searched Customer By Fname ******* ")


        result = self.searchCust.SearchByName("raj awale")
        print(result)
        assert True == result
        self.logger.info("**** Test_SearchCustomerByEmail_005 ******* ")













