import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import  Select




class searchCustomer():

    #Add Customer Page
    txtEmail_id = "SearchEmail"
    txtFirstName_id = "SearchFirstName"
    txtLastName_id = "SearchLastName"
    btnSearch_id ="search-customers"
    tblSearchResults_xpath = "//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath = "//table[@id='customers-grid']//tbody/tr/td"


    def __init__(self,driver):
        self.driver = driver

    def setEmail(self,email):
        self.driver.find_element(By.ID, self.txtEmail_id).clear()
        self.driver.find_element(By.ID,self.txtEmail_id).send_keys(email)
        time.sleep(3)
    def setFirstName(self,fname):
        self.driver.find_element(By.ID, self.txtFirstName_id).clear()
        self.driver.find_element(By.ID, self.txtFirstName_id).send_keys(fname)
    def setLastName(self, lname):
        self.driver.find_element(By.ID, self.txtLastName_id).clear()
        self.driver.find_element(By.ID, self.txtLastName_id).send_keys(lname)
    def clickSearch(self):
        self.driver.find_element(By.ID,self.btnSearch_id).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH, self.tableRows_xpath))
    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH, self.tableColumns_xpath))


    def SearchByEmail(self,email):
        flag = False
        for r in range(1,self.getNoOfRows()+1):
            emailID=self.driver.find_element(By.XPATH,"//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[2]").text
            print(emailID)
            if emailID == email:
                flag = True
                break
        return  flag

    def SearchByName(self,fullname):
        flag = False
        for r in range(1,self.getNoOfColumns()+1):
            name=self.driver.find_element(By.XPATH,"//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[3]").text
            if name == fullname:
                flag = True
                break
        return flag




















































































