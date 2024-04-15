import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import  Select

#Selecting the Customers Tab and seleting customers sub menu and clicking on ADD


class addCustomer():
    #Till clicking on  the Add Button
    link_customers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    link_customers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    buttonAddnew_xpath = "//a[normalize-space()='Add new']"

    #The below are the elements in the Add customer Landing Page

    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFristName_xpath="//input[@id='FirstName']"
    txtLastName_xpath="//input[@id='LastName']"
    rdMaleGender_id="Gender_Male"
    rdFemaleGender_id="Gender_Female"
    txtDob_xpath ="//input[@id='DateOfBirth']"
    txtComapanyName_xpath="//input[@id='Company']"
    txtcustomerRole_xpath = "(//div[@class='k-widget k-multiselect k-multiselect-clearable'])[2]"
    lstRegistered_xpath = "//li[normalize-space()='Registered']"
    lstAdministrators_xpath="//li[normalize-space()='Administrators']"
    lstForumModerators_xpath="//li[normalize-space()='Forum Moderators']"
    lstGuests_xpath = "//li[normalize-space()='Guests']"
    lstVendors_xpath = "//li[contains(text(),'Vendors')]"
    drdwnmgrOfVendor_xpath = "//*[@id='VendorId']"
    txtAdminComment_xpath = "//select[@id='VendorId']"
    btnSave_xpath = "//button[@name='save']"


    def __init__(self,driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH,self.link_customers_menu_xpath ).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element(By.XPATH, self.link_customers_menuitem_xpath).click()

    def clickOnAddCustomer(self):
        self.driver.find_element(By.XPATH,self.buttonAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txtEmail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.txtPassword_xpath).send_keys(password)

    def setCustomerRole(self,role):
        self.driver.find_element(By.XPATH,self.txtcustomerRole_xpath).click()
        time.sleep(3)
        if role == "Registered":
            self.driver.find_element(By.XPATH,"//*[@id='SelectedCustomerRoleIds_taglist']/li//span[@title='delete']").click()
            self.listItem = self.driver.find_element(By.XPATH,self.lstRegistered_xpath)
        elif role == "Administrators":
            self.listItem = self.driver.find_element(By.XPATH, self.lstAdministrators_xpath)
        elif role == "Forum Moderators":
            self.listItem = self.driver.find_element(By.XPATH, self.lstForumModerators_xpath)
        elif role == "Guests":
            time.sleep(2)
            self.driver.find_element(By.XPATH,"//*[@id='SelectedCustomerRoleIds_taglist']/li//span[@title='delete']").click()
            # self.driver.find_element(By.XPATH, self.txtcustomerRole_xpath).click()
            self.listItem = self.driver.find_element(By.XPATH, self.lstGuests_xpath)
        elif role == "Vendors":
            self.listItem = self.driver.find_element(By.XPATH, self.lstVendors_xpath)
        else:
            self.listItem = self.driver.find_element(By.XPATH, self.lstVendors_xpath)

        time.sleep(2)
        self.driver.execute_script("arguments[0].click();",self.listItem)

    def setManagerOfVendor(self,value):
        drp = Select(self.driver.find_element(By.XPATH,self.drdwnmgrOfVendor_xpath))
        drp.select_by_visible_text(value)


    def setGender(self,gender):
        if gender == "Male":
            self.driver.find_element(By.ID,self.rdMaleGender_id).click()
        elif gender == "Female":
            self.driver.find_element(By.ID, self.rdFemaleGender_id).click()
        else:
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH,self.txtFristName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH,self.txtLastName_xpath).send_keys(lname)

    def setDob(self,dob):
        self.driver.find_element(By.XPATH,self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self,comname):
        self.driver.find_element(By.XPATH,self.txtComapanyName_xpath).send_keys(comname)

    def setAdminContent(self,content):
        self.driver.find_element(By.XPATH,self.txtAdminComment_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH,self.btnSave_xpath).click()






















































































































































