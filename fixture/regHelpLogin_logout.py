import os, time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from model.names import names_log, info_login
from model.elements import wait


class base(object):
    def __init__(self, driver):
        self.driver = driver


class regHelpLogin_out(base):
    home_url = "http://doctors.secondok.com"
    title = "//title[@ng-bind='$root.page.title' and contains(text(), 'Login')]"
    english_xpath = "//div/span[contains(text(), 'EN')]"
    email_id = "log_email"
    password_id = "log_pwd"
    submit_xpath = "//div[@class='btn btn_green btn_enter ng-binding']"
    login_name = "//div[@class='b-user__name acc_name ng-binding' and contains(text(), 'Testerq Qtester')]"
    logout = "//a[@class='h_logout ']"


    def setup_login(self):
        driver = self.driver
        if driver.find_element_by_xpath(regHelpLogin_out.title):
            pass
        else:
            driver.get(regHelpLogin_out.home_url)

    def switch_to_english(self):
        english = self.driver.find_element_by_xpath(regHelpLogin_out.english_xpath)
        wait.element_xpath_clickable(self.driver, regHelpLogin_out.english_xpath)
        english.click()

    def email_name_login(self):
        driver = self.driver
        email = driver.find_element_by_id(regHelpLogin_out.email_id)
        time.sleep(2)
        wait.wait_el_id(driver, regHelpLogin_out.email_id)
        email.clear()
        email.send_keys(info_login.email)

    def password_name_login(self):
        driver = self.driver
        wait.wait_el_id(driver, regHelpLogin_out.password_id)
        password = driver.find_element_by_id(regHelpLogin_out.password_id)
        password.clear()
        password.send_keys(info_login.password)

    def submit_login(self):
        driver = self.driver
        wait.element_xpath_clickable(driver, regHelpLogin_out.submit_xpath)
        driver.find_element_by_xpath(regHelpLogin_out.submit_xpath).click()

    def check_login(self):
        driver = self.driver
        element = driver.find_element_by_xpath(regHelpLogin_out.login_name)
        assert element.text == "Testerq Qtester", "wrong name"

    def check_logout(self):
        driver = self.driver
        driver.find_element_by_xpath(regHelpLogin_out.logout).click()
        try:
            driver.find_element_by_xpath(regHelpLogin_out.title)
            error = 'false'
        except:
            error = 'True'
        assert error == 'false', "wrong logout"

