import os, time, sys


from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from model.names import names_log, info_user
from model.elements import wait


#path = os.getcwd()
#sys.path.append("{0}\Page".format(path))

class base(object):
    def __init__(self, driver):
        self.driver = driver


class regHelperPersonal(base):
    home_url = "http://doctors.secondok.com"
    title = "Login"
    registration_xpath = "//a[@ui-sref='registration']"
    english_xpath = "//div/span[contains(text(), 'EN')]"
    submit_email_password_element_xpath = "//a[@class='btn btn_green btn_reg_first ng-binding']"
    submit_contract_element_xpath = "//div[@class='btn btn_green btn_conf_rules ng-binding']"
    submit_pers_info_element_xpath = "//div[@class='btn btn_green ng-binding']"
    email_id = "reg_email"
    password_id = "reg_pwd"
    password_confirm_id = "reg_pwd_conf"
    firstname_id = "reg_name"
    lastname_id = "reg_surname"
    gender = "ref_male"
    country_select = "//div[@data-def='Country and city']"
    country_select_field = "html/body/div[2]/section[1]/div[2]/div[2]/div[3]/input"
    country_select_field_name = "//div[@ng-repeat='country in allCountries | filter:vm.filter']/span[@class='name ng-binding' and contains(text(), 'Ukraine')]"
    city_select_field_name = "html/body/div[2]/section[1]/div[2]/div[2]/div[3]/input"
    city_name = "html/body/div[2]/section[1]/div[2]/div[3]/div/div[2]/div/section/section/ng-include/div/div[3]/span"
    phone_id = "reg_tel"
    personal_details_submit = "//div[@class='btn btn_green ng-binding' and contains(text(), 'Go to education')]"
    submit_avatar = "//div[@class='btn btn_blue btn_save_avatar ng-binding']"
    avatar_photo_upload = "//div[@data-file='avatar']"
    script_chrome_photo_avatar = "C:\\Users\\John\\PycharmProjects\\SeconDOK\Files\\script_chrome_photo_avatar.exe"
    script_ff = "C:\\Users\\John\\PycharmProjects\\SeconDOK\Files\\script_ff_photo_avatar_diplom.exe"
    xpath_avatar_photo_left = "//img[@id='main_avatar']"
    xpath_avatar_photo_right = "//div[@id='reg_done_avatar']"
    xpath_first_name = "//span[@data-name='reg_name']"
    xpath_last_name = "//span[@data-name='reg_surname']"
    xpath_country = "//span[@data-name='reg_place_country']"
    xpath_city = "//span[@data-name='reg_place_city']"
    xpath_phone_number = "//span[@data-name='reg_tel']"


    def setup_registration(self):
        driver = self.driver
        driver.get(regHelperPersonal.home_url)
        wait.wait_title(driver, regHelperPersonal.title)
        time.sleep(2)

    def switch_to_english(self):
        english = self.driver.find_element_by_xpath(regHelperPersonal.english_xpath)
        wait.element_xpath_clickable(self.driver, regHelperPersonal.english_xpath)
        english.click()
        time.sleep(2)

    def go_registration(self):
        driver = self.driver
        element_to_hover_over = driver.find_element_by_xpath(regHelperPersonal.registration_xpath)
        hover = ActionChains(driver).move_to_element(element_to_hover_over)
        hover.perform()
        element = driver.find_element_by_xpath(regHelperPersonal.registration_xpath)
        element.click()

    def email_name_login(self):
        driver = self.driver
        email = driver.find_element_by_id(regHelperPersonal.email_id)
        time.sleep(2)
        wait.wait_el_id(driver, regHelperPersonal.email_id)
        email.clear()
        email.send_keys(names_log.email)

    def password_name_login(self):
        driver = self.driver
        wait.wait_el_id(driver, regHelperPersonal.password_id)
        password = driver.find_element_by_id(regHelperPersonal.password_id)
        password.clear()
        password.send_keys(names_log.password1)
        password.send_keys(Keys.TAB)
        wait.wait_el_id(driver, regHelperPersonal.password_confirm_id)
        password_conf = driver.find_element_by_id(regHelperPersonal.password_confirm_id)
        password.send_keys(Keys.TAB)
        password_conf.clear()
        password_conf.send_keys(names_log.password2)
        password.send_keys(Keys.TAB)

    def submit_email_password(self):
        driver = self.driver
        wait.element_xpath_active(driver, regHelperPersonal.submit_email_password_element_xpath)
        driver.find_element_by_xpath(regHelperPersonal.submit_email_password_element_xpath).click()

    def submit_registration_contract(self):
        driver = self.driver
        wait.element_xpath_active(driver, regHelperPersonal.submit_contract_element_xpath)
        driver.find_element_by_xpath(regHelperPersonal.submit_contract_element_xpath).click()

    def firstname(self):
        driver = self.driver
        first_name = driver.find_element_by_id(regHelperPersonal.firstname_id)
        wait.wait_el_id(driver, regHelperPersonal.firstname_id)
        time.sleep(2)
        first_name.clear ()
        first_name.send_keys(info_user.firstname)
        first_name.send_keys(Keys.TAB)

    def lastname(self):
        driver = self.driver
        wait.wait_el_id(driver, regHelperPersonal.lastname_id)
        last_name = driver.find_element_by_id(regHelperPersonal.lastname_id)
        last_name.clear()
        last_name.send_keys(info_user.lastname)
        time.sleep(1)

    def gender_select(self):
        driver = self.driver
        driver.find_element_by_id(regHelperPersonal.gender).click()
        #time.sleep(1)

    def country(self):
        driver = self.driver
        wait.element_xpath_active(driver, regHelperPersonal.country_select)
        driver.find_element_by_xpath(regHelperPersonal.country_select).click()
        time.sleep(1)

    def country_field(self):
        driver = self.driver
        wait.element_xpath_active(driver, regHelperPersonal.country_select_field)
        driver.find_element_by_xpath(regHelperPersonal.country_select_field).clear()
        driver.find_element_by_xpath(regHelperPersonal.country_select_field).send_keys(info_user.country)
        time.sleep(2)

    def country_field_name(self):
        driver = self.driver
        wait.element_xpath_clickable(driver, regHelperPersonal.country_select_field_name)
        time.sleep(2)
        driver.find_element_by_xpath(regHelperPersonal.country_select_field_name).click()
        time.sleep(2)

    def city_field_name(self):
        driver = self.driver
        driver.find_element_by_xpath(regHelperPersonal.city_select_field_name).clear()
        wait.element_xpath(driver, regHelperPersonal.city_name)
        driver.find_element_by_xpath(regHelperPersonal.city_name).click()
        time.sleep(2)

    def phone_id_select(self):
        driver = self.driver
        wait.wait_el_id(driver, regHelperPersonal.phone_id)
        driver.find_element_by_id(regHelperPersonal.phone_id).clear()
        driver.find_element_by_id(regHelperPersonal.phone_id).send_keys(info_user.phone)

    def details_avatar(self):
        driver = self.driver
        upload = driver.find_element_by_xpath(regHelperPersonal.avatar_photo_upload)
        wait.element_xpath(driver, regHelperPersonal.avatar_photo_upload)
        upload.click()
        time.sleep ( 2 )
        os.system(regHelperPersonal.script_chrome_photo_avatar)
        wait.element_xpath_active(driver, regHelperPersonal.submit_avatar)
        driver.find_element_by_xpath(regHelperPersonal.submit_avatar).click()
        time.sleep(2)

    def details_submit(self):
        driver = self.driver
        wait.element_xpath_active(driver, regHelperPersonal.personal_details_submit)
        driver.find_element_by_xpath(regHelperPersonal.personal_details_submit).click()
        time.sleep(2)


    def check_personal_data(self):
        driver = self.driver
        #check avatar photo
        assert driver.find_element_by_xpath(regHelperPersonal.xpath_avatar_photo_left), "failed, No avatar photo"
        assert driver.find_element_by_xpath(regHelperPersonal.xpath_avatar_photo_right), "failed, No avatar photo"

        #check name
        element = driver.find_element_by_xpath(regHelperPersonal.xpath_first_name)
        assert element.text == "Testerq", "failed, wrong first name"

        #check last name
        element = driver.find_element_by_xpath(regHelperPersonal.xpath_last_name)
        assert element.text == "Qtester", print("failed, wrong last name")

        #check country
        element = driver.find_element_by_xpath(regHelperPersonal.xpath_country)
        assert element.text == "Ukraine", "country does not exist"

        #check city
        element = driver.find_element_by_xpath(regHelperPersonal.xpath_city)
        assert element.text == "Kharkov", "city does not exist"

        #check phone number
        element = driver.find_element_by_xpath(regHelperPersonal.xpath_phone_number)
        assert element.text == "+38 (012) 345-67-89"









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


    #def personal_details_details_avatar(self):
     #   driver = self.driver

      #  icon = driver.find_element_by_css_selector ( "input" )
       # driver.execute_script("arguments[0].style.visibility = 'visible'; arguments[0].style.height = '1px'; arguments[0].style.width = '1px'; arguments[0].style.opacity = 1",  icon )

        #element = driver.find_element_by_xpath("//input[@type = 'file']")

        #element.send_keys(os.getcwd() + info_user.avatar_file)
        #time.sleep(5)
        #driver.find_element_by_xpath("//div[@class='btn btn_blue btn_save_avatar ng-binding']").click()
            # upload.click()

            # Runtime.getRuntime ().exec ( "Secondok_file.exe" );

            #from conftest import file_path


            # upload.send_keys ( Keys.ENTER )

            # upload.send_keys(path_to_image)
            # upload.send_keys ( Keys.TAB )
            # upload.send_keys(os.getcwd() + info_user.avatar_file)

            # base_dir = "C:\\Users\\John\\PycharmProjects\\SeconDOK\\Files\\"
            # path_to_image = os.path.join(base_dir, "konur_01.jpg")

#import os, sys
            # os.path.abspath("C:/Users/John/PycharmProjects/SeconDOK/Files/konur.jpg")
            # Imagepath = os.path.abspath('.\\Files\konur.jpg')