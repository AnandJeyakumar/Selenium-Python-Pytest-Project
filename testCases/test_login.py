from selenium import webdriver
from pageObjects.LoginPage import LoginPage
import pytest
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_login:
    base_url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getpassword()
    loggerValue = LogGen.loggen()
    @pytest.mark.regression
    def test_homepageTitle(self, setup):
        self.loggerValue.info("Inside Test login homepage title")

        self.loggerValue.info("*********** Test_001_login **************")
        self.loggerValue.info("******************Verifying Home Page Title***********************")

        self.driver = setup
        self.driver.get(self.base_url)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.loggerValue.info("***************** Home Page Title is Passed ***********************")

        else:
            self.driver.save_screenshot("C:\\python-selenium\\nopcommerceApp\\Screenshots\\test_homepageTitle.png")
            # self.driver.save_screenshot(".\\Screenshots\\" + "test_homepageTitle.png")
            self.driver.close()
            self.loggerValue.error("***************** Home Page Title is Failed ***********************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):

        self.loggerValue.info("****************** Verifying Login Test ***********************")

        self.driver = setup
        self.driver.get(self.base_url)
        self.loginObj = LoginPage(self.driver)
        self.loginObj.setUserName(self.username)
        self.loginObj.setPassword(self.password)
        self.loginObj.clickLogin()
        dash_title = self.driver.title
        if dash_title == "Dashboard / nopCommerce administration":
            assert True
            self.loggerValue.info("******************  Login Test Passed ***********************")
            self.driver.close()
        else:
            self.driver.save_screenshot("C:\\python-selenium\\nopcommerceApp\\Screenshots\\test_login.png")
            # self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.loggerValue.error("******************  Login Test Failed ***********************")
            assert False
