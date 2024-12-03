import time

import  pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_01_Admin_Login:

    baseURL = ReadConfig.getApplicationURL()
    userName = ReadConfig.getUserEmail()
    password = ReadConfig.getpassword()
    invalidUserName = ReadConfig.invalidemail()
    loggerValue=LogGen.loggen()

    @pytest.mark.sanity
    def test_title_verification(self,setup):
        self.loggerValue.info("***************** Test_01_Admin_Login ***********************")
        self.loggerValue.info("***************** Verification of test_title_verification Started ***********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.loggerValue.info("***************** Home Page Title is Passed ***********************")

        else:
            self.driver.save_screenshot("C:\\python-selenium\\nopcommerceApp\\Screenshots\\test_homepageTitle.png")
            # self.driver.save_screenshot(".\\Screenshots\\" + "test_homepageTitle.png")
            self.loggerValue.error("***************** Home Page Title is Failed ***********************")
            self.driver.close()
            assert False

    def test_valid_admin_login(self,setup):
        self.loggerValue.info("***************** Verification of test_valid_admin_login Started ***********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.admin_lp=LoginPage(self.driver)
        self.admin_lp.setUserName(self.userName)
        self.admin_lp.setPassword(self.password)
        self.admin_lp.clickLogin()
        time.sleep(7)
        loginPageTitle=self.driver.title
        print("The Logged in page title is ",loginPageTitle)

        if loginPageTitle == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.loggerValue.info(
                "***************** Verification of loginPageTitle is Passed ***********************")


        else:
            self.driver.save_screenshot("C:\\python-selenium\\nopcommerceApp\\Screenshots\\test_valid_admin_login.png")
            self.loggerValue.error(
                "***************** Verification of loginPageTitle is Failed ***********************")
            # self.driver.save_screenshot(".\\Screenshots\\" + "test_valid_admin_login.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    def test_invalid_admin_login(self,setup):
        self.loggerValue.info("***************** Verification of test_invalid_admin_login Started ***********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.admin_lp = LoginPage(self.driver)
        self.admin_lp.setUserName(self.invalidUserName)
        self.admin_lp.setPassword(self.password)
        self.admin_lp.clickLogin()
        time.sleep(5)
        errorText = self.admin_lp.invalidLogin_textElement_xpath()
        print("The error Text is ",errorText)
        self.driver.close()
        # if errorText == "Login was unsuccessful. Please correct the errors and try again.No customer account found":
        #     assert True
        #     self.driver.close()
        # else:
        #     print("********The message is not as Expected*********")
        #     self.driver.close()
        #     assert False














