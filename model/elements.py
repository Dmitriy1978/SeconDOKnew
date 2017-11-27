

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException




class base(object):
    def __init__(self, app):
         self.app = app


class wait(base):




    def element_xpath_clickable(self, xpath):
        WebDriverWait (self, 5).until(EC.element_to_be_clickable((By.XPATH, xpath)))

    def wait_el_name(self, element_name):
        element_name = str(element_name)
        WebDriverWait(self, 5).until(EC.element_located_to_be_selected((By.NAME, element_name)))

    def wait_el_id(self, element_id):
        element_id = str(element_id)
        #try:
         #   WebDriverWait(self, 60).until(EC.presence_of_element_located((By.ID, element_id)))
          #  print("Page is ready!")
        #except TimeoutException:
         #   print("Loading took too much time!")
        WebDriverWait(self, 5).until(EC.element_to_be_clickable((By.ID, element_id)))

    def wait_title(self, title):
        WebDriverWait(self, 5).until(EC.title_contains(title))

    def spinner_hide(self):
        WebDriverWait(self, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@class='b-spinner'][@style='display: none;']")))

    def page_name(self, name):
        WebDriverWait(self, 5).until(EC.presence_of_element_located((By.XPATH, "//h3[@class='b-form__header'][contains(text(), '"+name+"')]")))

    def element_xpath(self, xpath):
        WebDriverWait(self, 5).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))

    def element_xpath_hide(self, xpath):
        WebDriverWait(self, 5).until(EC.invisibility_of_element_located((By.XPATH, xpath)))

    def element_xpath_active(self, xpath):
        WebDriverWait(self, 5).until(EC.element_to_be_clickable((By.XPATH, xpath)))

    def element_xpath_visible(self, xpath):
        WebDriverWait(self, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))

    def page_load(self):
        WebDriverWait(self, 5).until(EC.presence_of_all_elements_located)



