import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen() #Logger

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info('******** Test_003_AddCustomer *********')
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info('******** Login succesful ********')

        self.logger.info('******** Starting Add Customer Test *******')

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.addcust.clickOnAddnew()

        self.logger.info('******** Providing customer info ********')

        self.email = random_generator() + '@gmail.com'
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManageOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Luis")
        self.addcust.setLastName("Cardeña")
        self.addcust.setDob("10/21/1985") # Format DD/MM/YYYY
        self.addcust.setCompanyName("QA Learning")
        self.addcust.setAdminContent("This is a test user")
        self.addcust.clickOnSave()

        self.logger.info("****** Saving customer info ******")

        self.logger.info("****** Add customer validation started ******")

        self.msg = self.driver.find_element_by_tag_name("body").text
        if "The new customer has been added successfully." in self.msg:
            assert True == True
            self.logger.info("******* Add customer Test Passed ******")
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_addCustomer_scr.png") #Screenshot
            self.logger.error("******* Add customer Test Failed ******")
            assert True == False

        self.driver.close()
        self.logger.info("******** Ending Home Page Title Test *******")

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))