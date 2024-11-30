import time

import  pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver

from pageObjects.LoginPage import LoginPage


class Test_01_Admin_Login:
    baseURL = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    userName = "admin@yourstore.com"
    password = "admin"
    invalidUserName = "siva@gmail.com"


    def test_title_verification(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            # self.loggerValue.info("***************** Home Page Title is Passed ***********************")

        else:
            self.driver.close()
            assert False
            # self.driver.save_screenshot("C:\\python-selenium\\nopcommerceApp\\Screenshots\\test_homepageTitle.png")
            # self.driver.save_screenshot(".\\Screenshots\\" + "test_homepageTitle.png")

            # self.loggerValue.error("***************** Home Page Title is Failed ***********************")

    def test_valid_admin_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.admin_lp=LoginPage(self.driver)
        self.admin_lp.setUserName(self.userName)
        self.admin_lp.setPassword(self.password)
        self.admin_lp.clickLogin()

        loginPageTitle=self.driver.title
        print("The Logged in page title is ",loginPageTitle)
        time.sleep(15)

        # if loginPageTitle == "Dashboard / nopCommerce administration":
        #     assert True
        #     self.driver.close()
        # else:
        #     self.driver.close()
        #     assert False

    def test_invalid_admin_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.admin_lp = LoginPage(self.driver)
        self.admin_lp.setUserName(self.invalidUserName)
        self.admin_lp.setPassword(self.password)
        self.admin_lp.clickLogin()
        time.sleep(3)
        errorText = self.admin_lp.invalidLogin_textElement_xpath()
        print(errorText)
        if errorText == "Login was unsuccessful. Please correct the errors and try again.No customer account found":
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False














