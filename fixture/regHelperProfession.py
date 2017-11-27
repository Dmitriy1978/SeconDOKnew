import os, time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from model.names import info_profession
from model.elements import wait
#from fixture.application import Application



class base(object):

    def __init__(self, driver):
        self.driver = driver

class regHelperProfession(base):
    select_institution_field = "//div[@data-arr='experience']//div[@data-def='Choose a Medical Institution']"
    institution_country = "html/body/div[2]/section[1]/div[6]/div[3]/div/div[1]/div/section/section/div/div[207]/span[2]"
    institution_city_field = "//input[@placeholder='Enter city']"
    institution_city_select = "html/body/div[2]/section[1]/div[6]/div[3]/div/div[2]/div/section/section/div/div[2]/span"
    year_field = "html/body/div[2]/section[1]/div[6]/div[2]/div[3]/input"
    year_start = "html/body/div[2]/section[1]/div[6]/div[3]/div/div[3]/div/section/section/div/div[36]/span"
    year_end = "html/body/div[2]/section[1]/div[6]/div[3]/div/div[4]/div/section/section/div/div[8]/span"
    institution_name = "//span[@data-id='62' and contains(text(), 'Branch of polyclinic №1 of Solomensky district of Kyiv')]"
    speciality_name = "html/body/div[2]/section[1]/div[6]/div[3]/div/div[6]/div/section/section/div/div[72]/span"
    specialization_field = "//input[@ng-model='filter.specializations']"
    specialization_name = "//span[@data-id='64' and contains(text(), 'Triholog')]"
    position = "//input[@placeholder='Choose position']"
    position_name = "//div[@ng-click='selectPosition(position.title, position.id)' and contains(text(), 'Doctor')]"
    profession = "//div[@class='btn btn_green ng-binding' and contains(text(), 'Go to additional information')]"
    xpath_institution = "//span[@data-name='reg_exper_name' and contains(text(), 'Branch of polyclinic №1 of Solomensky district of Kyiv')]"
    xpath_start_year = "//span[@data-name='reg_exper_dataFrom' and contains(text(), '1995')]"
    xpath_finish_year = "//span[@data-name='reg_exper_dataTo' and contains(text(), '2001')]"
    xpath_specialization = "//span[@data-name='reg_exper_prof' and contains(text(), 'Triholog')]"
    xpath_position = "//span[@data-name='reg_position' and contains(text(), 'Doctor')]"


    def select_institution(self):
        driver = self.driver
        wait.element_xpath_active(driver, regHelperProfession.select_institution_field)
        time.sleep(4)
        driver.find_element_by_xpath(regHelperProfession.select_institution_field).click()

    def select_country(self):
        driver = self.driver
        wait.element_xpath_clickable(driver, regHelperProfession.institution_country)
        driver.find_element_by_xpath(regHelperProfession.institution_country).click()
        time.sleep(1)

    def city_field(self):
        driver = self.driver
        wait.element_xpath_clickable(driver, regHelperProfession.institution_city_field)
        element = driver.find_element_by_xpath(regHelperProfession.institution_city_field)
        element.click()
        element.clear()
        element.send_keys(info_profession.city)
        time.sleep(3)

    def city_select(self):
        driver = self.driver
        wait.element_xpath_clickable(driver, regHelperProfession.institution_city_select)
        driver.find_element_by_xpath(regHelperProfession.institution_city_select).click()
        time.sleep ( 2 )

    def year_select(self):
        driver = self.driver
        driver.find_element_by_xpath(regHelperProfession.year_field).clear()
        wait.element_xpath_clickable(driver, regHelperProfession.year_start)
        driver.find_element_by_xpath(regHelperProfession.year_start).click()
        time.sleep(1)
        wait.element_xpath_clickable(driver, regHelperProfession.year_end)
        driver.find_element_by_xpath(regHelperProfession.year_end).click()
        time.sleep(1)

    def institution_select(self):
        driver = self.driver
        wait.element_xpath_active(driver, regHelperProfession.institution_name)
        driver.find_element_by_xpath(regHelperProfession.institution_name).click()
        time.sleep(1)

    def speciality_select(self):
        driver = self.driver
        wait.element_xpath_active(driver, regHelperProfession.speciality_name)
        driver.find_element_by_xpath(regHelperProfession.speciality_name).click()
        time.sleep(1)

    def select_specialization(self):
        driver = self.driver
        wait.element_xpath_clickable(driver, regHelperProfession.specialization_field)
        element = driver.find_element_by_xpath(regHelperProfession.specialization_field)
        element.click()
        time.sleep(1)
        driver.find_element_by_xpath(regHelperProfession.specialization_name).click()

    def select_position(self):
        driver = self.driver
        wait.element_xpath_clickable(driver, regHelperProfession.position)
        element = driver.find_element_by_xpath(regHelperProfession.position)
        time.sleep(1)
        element.click()
        time.sleep(1)
        driver.find_element_by_xpath(regHelperProfession.position_name).click()

    def profession_submit(self):
        driver = self.driver
        wait.element_xpath_clickable(driver, regHelperProfession.profession)
        driver.find_element_by_xpath(regHelperProfession.profession).click()
        time.sleep(2)

    def check_profession_data(self):
        driver = self.driver

       # check university name
        element = driver.find_element_by_xpath(regHelperProfession.xpath_institution)
        assert element.text == "Branch of polyclinic №1 of Solomensky district of Kyiv", "Not your institution name"

        # check start year
        element = driver.find_element_by_xpath(regHelperProfession.xpath_start_year)
        assert element.text == "1995", "wrong start year"

        # check finished year
        element = driver.find_element_by_xpath(regHelperProfession.xpath_finish_year)
        assert element.text == "2001", "wrong finished year"

        # check specialization
        try:
            driver.find_element_by_xpath(regHelperProfession.xpath_specialization)
            error = 'false'
        except:
            error = 'True'
        assert error == 'false', "wrong specialization"

        # check position
        try:
            driver.find_element_by_xpath(regHelperProfession.xpath_position)
            error = 'false'
        except:
            error = 'True'
        assert error == "false", "wrong position"


