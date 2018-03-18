from behave import then
from nose.tools import assert_true
import re

from features.pages.contact_page import ContactPageLocators


@then("Phone number is displayed")
def step_impl(context):
    assert_true(context.contact_page.driver.find_element(*ContactPageLocators.PHONE_NUMBER).is_displayed(),
                "Expected phone number to be visible")


@then("Phone number is correct")
def step_impl(context):
    phone_number = context.contact_page.driver.find_element(*ContactPageLocators.PHONE_NUMBER).text.split(": ")[1]
    assert_true(re.match("^(\+48 )?500[- ]?600[- ]?700$", phone_number),
                "Expected phone number to be \"+48 500 600 700\"")
