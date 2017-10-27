import os, time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from model.names import info_add
from model.elements import wait


class base(object):
    def __init__(self, driver):
        self.driver = driver


class regHelperAddinform(base):
    inform_xpath = "//textarea[@id='reg_add_info']"
    submit_add_xpath = "//div[@class='btn btn_green ng-binding']"
    xpath_add = "//span[@data-name='reg_add_info' and contains(text(), '— «Нимфа», туды её в качель, разве товар даёт? — смутно молвил гробовой мастер. — Разве ж она может покупателя удовлетворить? Гроб — он одного лесу сколько требует…')]"


    def add_information(self):
        driver = self.driver
        wait.element_xpath_active(driver, regHelperAddinform.inform_xpath)
        element = driver.find_element_by_xpath(regHelperAddinform.inform_xpath)
        element.click()
        element.clear()
        element.send_keys(info_add.add)

    def submit_add(self):
        driver = self.driver
        wait.element_xpath_active(driver, regHelperAddinform.submit_add_xpath)
        driver.find_element_by_xpath(regHelperAddinform.submit_add_xpath).click()

    # check additional data
    def check_additional_data(self):
        driver = self.driver
        element = driver.find_element_by_xpath(regHelperAddinform.xpath_add)
        assert element.text == "— «Нимфа», туды её в качель, разве товар даёт? — смутно молвил гробовой мастер. — Разве ж она может покупателя удовлетворить? Гроб — он одного лесу сколько требует…"