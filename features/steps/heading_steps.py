from behave import given, then
from pages.start_page import StartPage

@given('I am on the homepage')
def I_am_on_the_homepage(context):
    context.page = StartPage(context.driver).open()

@then('I should see the heading "{expected_heading}"')
def I_should_see_the_heading(context, expected_heading):
    actual_heading = context.page.get_heading_text()
    assert actual_heading == expected_heading, f"Expected heading '{expected_heading}', but got '{actual_heading}'"