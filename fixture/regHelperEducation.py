import os, time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from model.names import info_education
from model.elements import wait
#from fixture.application import Application



class base(object):

    def __init__(self, driver):
        self.driver = driver

class regHelperEducation(base):

    education_select_school_field = "//div[@data-arr='educations']//div[@data-def='Choose your school / college / academy / university']"
    school_country = "html/body/div[2]/section[1]/div[3]/div[3]/div/div[1]/div/section/section/ng-include/div/div[207]/span[2]"
    school_city_field = "//input[@placeholder='Enter city']"
    school_city_select = "html/body/div[2]/section[1]/div[3]/div[3]/div/div[2]/div/section/section/ng-include/div/div[2]/span"
    year_field = "html/body/div[2]/section[1]/div[3]/div[2]/div[3]/input"
    year_start = "//section[1]/div[3]/div[3]/div/div[3]/div/section/section/div/div[11]/span"
    year_end = "//section[1]/div[3]/div[3]/div/div[4]/div/section/section/div/div[10]/span"
    university_name = "html/body/div[2]/section[1]/div[3]/div[3]/div/div[5]/div/section/section/ng-include/div/div/span[contains(text(), 'Karazin')]"
    specialization_name = "//section[1]/div[3]/div[3]/div/div[6]/div/section/section/div/div/span[contains(text(), 'Toxicology')]"
    upload_diplom = "//div[@class='load_pic active']/div"
    upload_page_1 = "html/body/div[2]/div[2]/div/div[3]/div[1]/div[2]/div/div[1]"
    upload_page_2 = "html/body/div[2]/div[2]/div/div[3]/div[2]/div[2]/div/div[1]"
    script_chrome_photo_diplom_1 = "C:\\Users\\John\\PycharmProjects\\SeconDOK\Files\\script_chrome_diplom_1.exe"
    script_chrome_photo_diplom_2 = "C:\\Users\\John\\PycharmProjects\\SeconDOK\Files\\script_chrome_diplom_2.exe"
    submit_diplom = "//div[@class='btn btn_blue btn_save_educ ng-binding']"
    qual_categor = "//div[@class='title ng-binding' and contains(text(), 'Choose qualification category')]"
    qualification = "//span[contains(text(), 'MD (Medicinae Doctor')]"
    academic_degree = "//div[@class='title ng-binding' and contains(text(), 'Choose academic degree')]"
    degree_select = "html/body/div[2]/section[1]/div[5]/div[3]/div/div/div/section/section/ng-include/div/div[3]/span"
    education = "//div[@class='btn btn_green ng-binding' and contains(text(), 'Go to professional skills')]"
    xpath_diplom_editor = "//div[@data-arr='educations']//div[@class='circ edit btn_upload']"
    xpath_university = "//span[@data-name='reg_educ_name' and contains(text(), 'Kharkiv national university of V. Karazin (KNU)')]"
    xpath_start_year = "//span[@data-name='reg_educ_dataFrom' and contains(text(), '1970')]"
    xpath_finish_year = "//span[@data-name='reg_educ_dataTo' and contains(text(), '1978')]"
    xpath_specialization = "//span[@data-name='reg_educ_prof' and contains(text(), 'Toxicology')]"
    xpath_qualification = "//span[@data-name='reg_cval' and contains(text(), 'MD (Medicinae Doctor)')]"
    xpath_academic_degree = "//span[@data-name='reg_degree' and contains(text(), 'Professor')]"

    def select_school(self):
        driver = self.driver
        wait.element_xpath_active(driver, regHelperEducation.education_select_school_field)
        time.sleep(2)
        driver.find_element_by_xpath(regHelperEducation.education_select_school_field).click()

    def select_school_country(self):
        driver = self.driver
        wait.element_xpath_active(driver, regHelperEducation.school_country)
        time.sleep(1)
        driver.find_element_by_xpath(regHelperEducation.school_country).click()

    def city_field(self):
        driver = self.driver
        wait.element_xpath_clickable( driver, regHelperEducation.school_city_field )
        element = driver.find_element_by_xpath( regHelperEducation.school_city_field )
        element.click()
        element.clear()
        element.send_keys(info_education.city)
        time.sleep(3)

    def city_select(self):
        driver = self.driver
        wait.element_xpath_clickable(driver, regHelperEducation.school_city_select )
        driver.find_element_by_xpath(regHelperEducation.school_city_select).click()

    def year_select(self):
        driver = self.driver
        driver.find_element_by_xpath(regHelperEducation.year_field).clear()
        wait.element_xpath_clickable(driver, regHelperEducation.year_start)
        driver.find_element_by_xpath(regHelperEducation.year_start).click()
        time.sleep(1)
        wait.element_xpath_clickable(driver, regHelperEducation.year_end)
        driver.find_element_by_xpath(regHelperEducation.year_end).click()
        time.sleep(1)

    def university_select(self):
        driver = self.driver
        wait.element_xpath_active(driver, regHelperEducation.university_name)
        driver.find_element_by_xpath(regHelperEducation.university_name).click()
        time.sleep(1)

    def specialization_select(self):
        driver = self.driver
        wait.element_xpath_active(driver, regHelperEducation.specialization_name)
        driver.find_element_by_xpath(regHelperEducation.specialization_name).click ()
        #time.sleep(1)

    def diplom_select(self):
        driver = self.driver
        upload = driver.find_element_by_xpath(regHelperEducation.upload_diplom)
        wait.element_xpath_active(driver, regHelperEducation.upload_diplom)
        upload.click()
        load_page_1 = driver.find_element_by_xpath(regHelperEducation.upload_page_1)
        wait.element_xpath_clickable(driver, regHelperEducation.upload_page_1)
        load_page_1.click()
        os.system(regHelperEducation.script_chrome_photo_diplom_1)
        time.sleep(3)
        load_page_2 = driver.find_element_by_xpath(regHelperEducation.upload_page_2)
        wait.element_xpath_clickable(driver, regHelperEducation.upload_page_2)
        load_page_2.click()
        os.system(regHelperEducation.script_chrome_photo_diplom_2)
        wait.element_xpath_active(driver, regHelperEducation.submit_diplom)
        driver.find_element_by_xpath(regHelperEducation.submit_diplom).click()

    def select_qual_categor(self):
        driver = self.driver
        wait.element_xpath_clickable(driver, regHelperEducation.qual_categor)
        driver.find_element_by_xpath(regHelperEducation.qual_categor).click()

    def select_qualification(self):
        driver = self.driver
        wait.element_xpath_clickable(driver, regHelperEducation.qualification)
        driver.find_element_by_xpath(regHelperEducation.qualification).click()

    def select_academic_degree(self):
        driver = self.driver
        wait.element_xpath_clickable(driver, regHelperEducation.academic_degree)
        driver.find_element_by_xpath(regHelperEducation.academic_degree).click()
        time.sleep(1)

    def select_academdegree(self):
        driver = self.driver
        wait.element_xpath_clickable(driver, regHelperEducation.degree_select)
        driver.find_element_by_xpath(regHelperEducation.degree_select).click()

    def education_submit(self):
        driver = self.driver
        wait.element_xpath_clickable(driver, regHelperEducation.education)
        driver.find_element_by_xpath(regHelperEducation.education).click()
        time.sleep(2)

    def check_education_data(self):
        driver = self.driver

        # check diplom photo
        assert driver.find_element_by_xpath(regHelperEducation.xpath_diplom_editor), "No diplom photo"
        assert driver.find_element_by_xpath(regHelperEducation.xpath_diplom_editor), "No diplom photo"

        # check university name
        element = driver.find_element_by_xpath(regHelperEducation.xpath_university)
        assert element.text == "Kharkiv national university of V. Karazin (KNU)", "Not your university name"

        # check start year
        element = driver.find_element_by_xpath(regHelperEducation.xpath_start_year)
        assert element.text == "1970", "wrong start year"

        # check finished year
        element = driver.find_element_by_xpath(regHelperEducation.xpath_finish_year)
        assert element.text == "1978", "wrong finished year"

        # check specialization
        element = driver.find_element_by_xpath(regHelperEducation.xpath_specialization)
        assert element.text == "Toxicology", "specialization is wrong"

        # check digree qualification
        element = driver.find_element_by_xpath(regHelperEducation.xpath_qualification)
        assert element.text == "MD (Medicinae Doctor)", "qualification is wrong"

        # check academic degree
        element = driver.find_element_by_xpath(regHelperEducation.xpath_academic_degree)
        assert element.text == "Professor", "academic degree is wrong"



    def is_element_present(self, how, what):

        try:
            self.driver.find_element ( by=how, value=what )
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert ()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert ()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept ()
            else:
                alert.dismiss ()
            return alert_text
        finally:
            self.accept_next_alert = True


