from abc import ABC

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from features.browser import Browser


class BasePage(ABC, Browser):

    def __init__(self, url):
        super(BasePage, self).__init__()
        self.url = url

    def navigate_to(self):
        self.driver.get(self.url)

    def click_element(self, by, value):
        self.driver.find_element(by, value).click()
        return self

    def get_page_title(self):
        return self.driver.title

    def get_element_text(self, by, value):
        return self.driver.find_element(by, value).text

    def wait_for_element_visibility(self, by, value):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((by, value)),
                                            "Timeout when waiting for element to be visible")
        return self
