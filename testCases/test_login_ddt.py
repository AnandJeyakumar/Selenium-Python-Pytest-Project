import time

from selenium import webdriver
from pageObjects.LoginPage import LoginPage
import pytest
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test_002_DDT_login:
    base_url = ReadConfig.getApplicationURL()
    path="C:\\python-selenium\\nopcommerceApp\\testData\\LoginData.xlsx"
    path = ".//testData/LoginData.xlsx"
    loggerValue = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):

        self.loggerValue.info("****************** Test_002_DDT_login ***********************")
        self.loggerValue.info("****************** Verifying Login DDT Test ***********************")

        self.driver = setup
        self.driver.get(self.base_url)
        self.loginObj = LoginPage(self.driver)


        self.rows= XLUtils.getrowcount(self.path,"Sheet1")
        print("Number of Rows in a Excel :",self.rows)

        list_status =[]


        for r in range(2,self.rows+1):
            self.user = XLUtils.readData(self.path,"Sheet1",r,1)
            self.password= XLUtils.readData(self.path,"Sheet1",r,2)
            self.exp = XLUtils.readData(self.path,"Sheet1",r,3)

            self.loginObj.setUserName(self.user)
            self.loginObj.setPassword(self.password)
            self.loginObj.clickLogin()
            time.sleep(5)


            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp =="Pass":
                    self.loggerValue.info("****Passed******")
                    self.loginObj.clickLogout()
                    list_status.append("Pass")
                elif self.exp =="Fail":
                    self.loggerValue.info("**** Failed ******")
                    self.loginObj.clickLogout()
                    list_status.append("Fail")

            elif act_title!=exp_title:
                if self.exp=="Pass":
                    self.loggerValue.info("****Failed*****")
                    list_status.append("Fail")
                elif self.exp=="Fail":
                    self.loggerValue.info("****Passed*****")
                    list_status.append("Pass")

        if "fail" not in list_status:

            self.loggerValue.info("****Login DDT Test  Passed *****")
            self.driver.close()
            assert True
        else:
            self.loggerValue.info("****Login DDT Test is Failed*****")
            self.driver.close()
            assert False

        self.loggerValue.info("***END of Login DDT Test*******")
        self.loggerValue.info("**********Completed Test_002_DDT_login Test*******")













