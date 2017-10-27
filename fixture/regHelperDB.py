from model.names import info_db
from model.elements import wait
from selenium.webdriver.common.keys import Keys
from model.names import names_log
import time


class base(object):
    def __init__(self, driver):
        self.driver = driver


class regHelperDB(base):
    admin_url = "https://doctors.secondok.com/admin/doctors"
    title = "Админ Панель SeconDOK"
    admin_login = "//button[@type='submit']"
    email_name = "//input[@name='email']"
    password_name = "//input[@name='password']"
    title_panel = "Врачи | SeconDOK Admin Panel"
    section_doctor = "//li[@class='showAdmin active']//span[contains(text(), 'Врачи')]"
    delete_doctor = "//tbody//tr[td[contains(text(), 'Testerq ')]]//button[@class='btn btn-danger btn-xs btn-delete btn-flat']"
    accept_button = "//button[@class='btn btn-primary']"
    approve_delete = "//tbody//tr[td[contains(text(), 'Testerq ')]]//i[@class='fa fa-trash']"
    search_admin = "//input[@type = 'search']"
    exit_admin = "//span[contains(text(), 'Выход')]"



    def setup_for_delete_doctor_in_db(self):
        driver = self.driver
        driver.get(regHelperDB.admin_url)
        wait.wait_title(driver, regHelperDB.title)

    def email_db_login(self):
        driver = self.driver
        email = driver.find_element_by_xpath(regHelperDB.email_name)
        time.sleep(2)
        wait.element_xpath_clickable(driver, regHelperDB.email_name)
        email.clear()
        email.send_keys(info_db.email)
        email.send_keys(Keys.TAB)

    def password_name_login(self):
        driver = self.driver
        wait.element_xpath_clickable(driver, regHelperDB.password_name)
        password = driver.find_element_by_xpath(regHelperDB.password_name)
        password.clear()
        password.send_keys(info_db.password)

    def submit_db_login(self):
        driver = self.driver
        wait.element_xpath_clickable(driver, regHelperDB.admin_login)
        driver.find_element_by_xpath(regHelperDB.admin_login).click()

    def select_doctor_section(self):
        driver = self.driver
        #wait.wait_title(driver, regHelperDB.title_panel)
        wait.element_xpath_clickable(driver, regHelperDB.section_doctor)
        driver.find_element_by_xpath(regHelperDB.section_doctor).click()


    def delete_doctor_button(self):
        driver = self.driver
        wait.element_xpath_clickable(driver, regHelperDB.delete_doctor)
        driver.find_element_by_xpath(regHelperDB.delete_doctor).click()
        wait.element_xpath_clickable(driver, regHelperDB.accept_button)
        driver.find_element_by_xpath(regHelperDB.accept_button).click()
        time.sleep(2)
        wait.element_xpath_clickable(driver, regHelperDB.approve_delete)
        driver.find_element_by_xpath(regHelperDB.approve_delete).click()

    def verifying_delete_exit(self):
        driver = self.driver
        wait.element_xpath_clickable(driver, regHelperDB.search_admin)
        element = driver.find_element_by_xpath(regHelperDB.search_admin)
        element.clear()
        element.send_keys(names_log.email)
        assert len(driver.find_elements_by_xpath(regHelperDB.delete_doctor)) == 0
        try:
            driver.find_element_by_xpath(regHelperDB.delete_doctor)
            error = 'True'
        except:
            error = 'False'
        assert error == 'False', "doctor still exist"
        wait.element_xpath_clickable(driver, regHelperDB.exit_admin)
        driver.find_element_by_xpath(regHelperDB.exit_admin).click()




