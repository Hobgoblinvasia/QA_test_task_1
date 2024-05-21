import requests

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://www.baaqmd.gov/sitemap"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Unable to find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Unable to find elements by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def click_button(self, locator):
        return self.find_element(locator, time=10).click()

    def get_present_url(self):
        return self.driver.current_url

    def get_status_code(self):
        return requests.get(self.get_present_url()).status_code
