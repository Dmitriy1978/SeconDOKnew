from model.names import info_bill
from model.elements import wait
import time


class base(object):
    def __init__(self, driver):
        self.driver = driver


class regHelperBillInfo(base):
    inform_xpath = "//input[@id='reg_card']"
    submit_add_xpath = "//div[@class='btn btn_green ng-binding']"
    xpath_add = "//span[@data-name='reg_card' and contains(text(), '1234 5678 1234 5678')]"
    submit_reg_xpath = "//div[@class='btn btn_green btn_reg_complet ng-binding']"

    def bill_information(self):
        driver = self.driver
        wait.element_xpath_active(driver, regHelperBillInfo.inform_xpath)
        element = driver.find_element_by_xpath(regHelperBillInfo.inform_xpath)
        element.click()
        element.clear()
        element.send_keys(info_bill.bill)

    def submit_bill(self):
        driver = self.driver
        wait.element_xpath_active(driver, regHelperBillInfo.submit_add_xpath)
        driver.find_element_by_xpath(regHelperBillInfo.submit_add_xpath).click()

    # check additional data
    def check_bill(self):
        driver = self.driver
        element = driver.find_element_by_xpath(regHelperBillInfo.xpath_add)
        element = str(element.text)
        assert element == "1234 5678 1234 5678", "wrong Billing information"

    # final registration submit
    def submit_registration(self):
        driver = self.driver
        wait.element_xpath_active(driver, regHelperBillInfo.submit_reg_xpath)
        driver.find_element_by_xpath(regHelperBillInfo.submit_reg_xpath).click()
        time.sleep(6)
