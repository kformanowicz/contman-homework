import re

from behave import then
from hamcrest import assert_that

from features.pages.contact_page import ContactPageLocators


@then("{item_name} number is displayed")
def step_impl(context, item_name):
    locator = ContactPageLocators.PHONE_NUMBER if item_name == "Phone" else ContactPageLocators.FAX_NUMBER
    assert_that(context.contact_page.driver.find_element(*locator).is_displayed(),
                "Expected phone number to be visible")


@then("{item_name} number is correct")
def step_impl(context, item_name):
    if item_name == "Phone":
        number = context.contact_page.driver.find_element(*ContactPageLocators.PHONE_NUMBER).text.split(": ")[1]
        pattern = re.compile("^(\+48)?[- ]?500[- ]?600[- ]?700$")
    else:
        number = context.contact_page.driver.find_element(*ContactPageLocators.FAX_NUMBER).text.split(": ")[1]
        pattern = re.compile("^(\+48)?[- ]?22[- ]123[- ]45[- ]67$")

    assert_that(bool(re.match(pattern, number)),
                "Expected {} number to be \"+48 500 600 700\", and it is {}".format(item_name, number))
