import random
import string
import time

import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomer import addCustomer
from selenium.webdriver.common.by import By



class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username= ReadConfig.getUserEmail()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()
    @pytest.mark.regression
    def test_addCustomer(self,setup):
        self.logger.info("********* Test_003_AddCustomer ******** ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("******** Login Successfull*****")

        self.logger.info("******** Started Add Customer Flow *****")

        self.addCust = addCustomer(self.driver)
        self.addCust.clickOnCustomerMenu()
        self.addCust.clickOnCustomerMenuItem()
        self.addCust.clickOnAddCustomer()

        self.logger.info("******** Providing Customer Info******")


        self.email= random_generator()+ "@gmail.com"
        self.addCust.setEmail(self.email)
        self.addCust.setPassword("test123")
        time.sleep(2)
        self.addCust.setCustomerRole("Guests")
        self.addCust.setManagerOfVendor("Vendor 2")
        time.sleep(2)
        print("line 48")
        self.addCust.setGender("Male")
        self.addCust.setFirstName("Anand")
        self.addCust.setLastName("Jeyakumar")
        self.addCust.setDob("7/03/1998")
        self.addCust.setCompanyName("Automation")
        self.addCust.setAdminContent("This is Automation Tester")
        self.addCust.clickOnSave()


        self.logger.info("*****SAVING CUSTOMER DETAILS********")

        self.logger.info("******** Add Customer Validation started******")

        self.msg = self.driver.find_element(By.TAG_NAME,"body").text

        print(self.msg)

        if "customer has been added successfully." in self.msg:
            assert True == True
            self.logger.info("******* Add Customer Test Passed *******")

        else:
            self.driver.save_screenshot(".\\Screenshots\\"+ "test_addCustomer.png") #Screenshot
            self.logger.info("******* Add Customer Test Failed *******")
            assert True == False

        self.driver.close()
        self.logger.info("*******Ending Test_003_AddCustomer *********")




def random_generator(size=8 , chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))






































































































































