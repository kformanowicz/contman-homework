from features.browser import Browser
from features.pages.home_page import HomePage
from features.pages.contact_page import ContactPage


def before_all(context):
    context.base_url = 'https://contman.github.io/testing_pages/'
    context.browser = Browser()
    context.home_page = HomePage(context)
    context.contact_page = ContactPage(context)


def after_all(context):
    context.browser.close()
