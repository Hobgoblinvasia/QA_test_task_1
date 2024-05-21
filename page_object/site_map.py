from page_object.base_page import BasePage
from selenium.webdriver.common.by import By


class SiteMapLocators:
    @staticmethod
    def get_text_locator(text):
        return f'//*[contains(@aria-label,"{text}")]'

    LOCATOR_HEADER = (By.CLASS_NAME, 'middle-nav-wrapper')
    LOCATOR_SUBLIST = (By.CLASS_NAME, 'tab-label')
    LOCATOR_ALERT_STATUS = (By.XPATH, get_text_locator('Alert Status'))
    LOCATOR_ABOUT_THE_AIR_DISTRICT = (By.XPATH, get_text_locator('About the Air District'))
    LOCATOR_PUBLIC_DATA_CENTER = (By.XPATH, get_text_locator('Public Data Center'))
    LOCATOR_ONLINE_SERVICES = (By.XPATH, get_text_locator('Online Services'))
    LOCATOR_PUBLICATIONS = (By.XPATH, get_text_locator('Publications'))


class SiteMap(BasePage):

    def go_to_home(self):
        return self.click_button(SiteMapLocators.LOCATOR_HOME)

    def go_to_alert_status(self):
        return self.click_button(SiteMapLocators.LOCATOR_ALERT_STATUS)

    def go_to_about_the_air_district(self):
        return self.click_button(SiteMapLocators.LOCATOR_ABOUT_THE_AIR_DISTRICT)

    def go_to_public_data_center(self):
        return self.click_button(SiteMapLocators.LOCATOR_PUBLIC_DATA_CENTER)

    def go_to_online_services(self):
        return self.click_button(SiteMapLocators.LOCATOR_ONLINE_SERVICES)

    def go_to_publications(self):
        return self.click_button(SiteMapLocators.LOCATOR_PUBLICATIONS)

    def check_header(self):
        return self.find_element(SiteMapLocators.LOCATOR_HEADER)
