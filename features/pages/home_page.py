from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, context):
        super(HomePage, self).__init__(context.base_url)

    def go_to_contact(self):
        if self.driver.find_element(*HomePageLocators.HAMBURGER_MENU).is_displayed():
            self.click_element(*HomePageLocators.HAMBURGER_MENU)\
                .wait_for_element_visibility(*HomePageLocators.CONTACT_LINK)
        self.click_element(*HomePageLocators.CONTACT_LINK)
        return self


class HomePageLocators(object):
    CONTACT_LINK = (By.CSS_SELECTOR, '[href="contact.html"]')
    HAMBURGER_MENU = (By.CLASS_NAME, 'navbar-toggler')
