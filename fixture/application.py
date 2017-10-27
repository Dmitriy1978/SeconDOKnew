from selenium import webdriver

from fixture.regHelperPersonal import regHelperPersonal
from fixture.regHelperEducation import regHelperEducation
from fixture.regHelperProfession import regHelperProfession
from fixture.regHelperAddInformation import regHelperAddinform
from fixture.regHelperMail_verify import regHelperMail
from fixture.regHelperBillInfo import regHelperBillInfo
from fixture.session import sessionHelper
from model.elements import wait

class Application:

    def __init__(self):
        #self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(60)
        self.session = sessionHelper(self)
        self.regHelperPersonal = regHelperPersonal(self)
        self.regHelperEducation = regHelperEducation(self)
        self.regHelperProfession = regHelperProfession(self)
        self.regHelperAddinform = regHelperAddinform(self)
        self.regHelperBillInfo = regHelperBillInfo(self)
        self.regHelperMail = regHelperMail(self)
        self.wait = wait(self)


        #self.base_url = "http://doctors.secondok.com/#/registration"
        #self.verificationErrors = []
        #self.accept_next_alert = True


    def is_valid(self):
        try:
            self.driver.current_url()
            return True
        except:
            return False


    def Open_home_page(self):
        driver = self.driver
        driver.get("http://doctors.secondok.com")


    def destroy(self):
        #driver = self.driver
        self.driver.delete_all_cookies()
        self.driver.quit()

    def delete_all_cookies(self):
        pass
