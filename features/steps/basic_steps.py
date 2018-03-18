from behave import given, when, then
from nose.tools import assert_equals

from features.pages.contact_page import ContactPageLocators


@given("I am on home page")
def step_impl(context):
    context.home_page.navigate_to()
    assert_equals(context.home_page.get_page_title(), "Test me!", "Expected page title to be \"Test me!\"")


@when("I click on \"{tab_name}\" tab")
def step_impl(context, tab_name):
    if tab_name == "Contact":
        context.home_page.go_to_contact()
    elif tab_name == "About":
        pass


@then("\"{page_name}\" page is opened")
def step_impl(context, page_name):
    if page_name == "Contact":
        assert_equals(context.contact_page.get_element_text(*ContactPageLocators.HEADER), "ABOUT OUR COMPANY",
                      "Expected page header to equal \"ABOUT OUR COMPANY\"")
    elif page_name == "About":
        pass
