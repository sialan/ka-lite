from behave import *
from selenium.common.exceptions import NoSuchElementException

from django.core.urlresolvers import reverse

from kalite.testing.behave_helpers import *

TIMEOUT = 3

@given("I am on the homepage")
def step_impl(context):
    go_to_homepage(context)

@when("I search for 'Math'")
def step_impl(context):
    search_for(context, "Math")

@when("I search for Basic Addition")
def step_impl(context):
    search_for(context, "Basic Addition")

@when("I click on the first option")
def step_impl(context):
    menu_item = find_css_class_with_wait(context, "ui-menu-item")
    assert menu_item, "No menu item on page."
    click_and_wait_for_page_load(context, menu_item)

@then("I should see a list of options")
def step_impl(context):
    auto_complete_list = find_css_class_with_wait(context, "ui-menu-item")
    assert auto_complete_list, "Auto complete list not found on page."

@then("I should navigate to Basic Addition")
def step_impl(context):
    expected_url = build_url(context, "/learn/khan/math/arithmetic/addition-subtraction/basic_addition/basic-addition/")
    assert context.browser.current_url == expected_url, "Assertion failed. context.browser.current_url: %s\nbuild_url: %s" % (context.browser.current_url, expected_url)

def search_for(context, text):
    search_field = find_id_with_wait(context, "search")
    search_field.send_keys(text)