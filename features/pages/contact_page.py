from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


class ContactPage(BasePage):
    URL = "contact.html"

    def __init__(self, context):
        super(ContactPage, self).__init__(context.base_url + ContactPage.URL)


class ContactPageLocators(object):
    HEADER = (By.CLASS_NAME, "section-heading-lower")
    PHONE_NUMBER = (By.CLASS_NAME, "phoneNumber")
    FAX_NUMBER = (By.CLASS_NAME, "fuxNumber")
