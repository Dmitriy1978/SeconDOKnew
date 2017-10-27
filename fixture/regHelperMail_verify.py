import sys, unittest, time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

from model.names import info_mail
from model.elements import wait


class base(object):
    def __init__(self, driver):
        self.driver = driver


class regHelperMail(base):
    mail_url = "http://www.i.ua/"
    submit = "p > input[type=\"submit\"]"
    email = "//span[contains(text(), 'Регистрация нового пользователя (SeconDOK)')]"
    message = "//div[@class = 'message_body']/iframe"
    mes_reg = "//strong[contains(text(), 'Вы заполнили регистрационные данные на сайте ')]"
    mes_del = "//body//div[@class='message_container clear']/div/div[1]//a[@class='button l_r del']"
    logout = "//span[@class='icon-ho ho_settings ho_i_settings']"

    def test_setup(self):
        driver = self.driver
        driver.get(regHelperMail.mail_url)

    def login_mail(self):
        driver = self.driver
        driver.find_element_by_name("login").clear()
        driver.find_element_by_name("login").send_keys(info_mail.mail)
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(info_mail.password)
        driver.find_element_by_css_selector(regHelperMail.submit).click()

    def select_email(self):
        driver = self.driver
        driver.find_element_by_xpath(regHelperMail.email).click()
        time.sleep(2)
        mail = driver.find_element_by_xpath(regHelperMail.message)
        driver.switch_to_frame(mail)

    def check_email(self):
        driver = self.driver
        try:
            driver.find_element_by_xpath(regHelperMail.mes_reg)
            error = 'false'
        except:
            error = 'True'
        assert error == 'false', "wrong email"

    def mail_delete(self):
        driver = self.driver
        driver.switch_to_default_content()
        driver.find_element_by_xpath(regHelperMail.mes_del).click()
        time.sleep(4)
        alert = driver.switch_to_alert()
        alert.accept()
        time.sleep(2)

    def logout_email(self):
        driver = self.driver
        driver.find_element_by_xpath(regHelperMail.logout).click()

