import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


@given('a user navigates to the SauceLabs demo site')
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get("https://www.saucedemo.com/")


@when('the user logs in with username "{username}" and password "{password}"')
def step_impl(context, username, password):
    username_input = context.browser.find_element(By.ID, "user-name")
    username_input.send_keys(username)
    time.sleep(1)
    password_input = context.browser.find_element(By.ID, "password")
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)  # Simulating pressing the Enter key
    time.sleep(1)


@then('the user should be redirected to the inventory page')
def step_impl(context):
    assert "inventory.html" in context.browser.current_url


@then('an error message "{error_message}" should be displayed')
def step_impl(context, error_message):
    time.sleep(1)
    error = context.browser.find_element(
        By.CSS_SELECTOR, "h3[data-test='error']")
    assert error_message in error.text


@given('a user is logged in the SauceLabs demo site')
def step_impl(context):
    context.execute_steps('''
        given a user navigates to the SauceLabs demo site
        when the user logs in with username "standard_user" and password "secret_sauce"
        then the user should be redirected to the inventory page
    ''')


time.sleep(1)


@when('the user clicks the logout button')
def step_impl(context):
    menu_button = context.browser.find_element(By.ID, "react-burger-menu-btn")
    menu_button.click()
    time.sleep(1)
    logout_button = context.browser.find_element(By.ID, "logout_sidebar_link")
    logout_button.click()
    time.sleep(1)


@then('the user should be logged out and redirected to the home page')
def step_impl(context):
    assert "https://www.saucedemo.com/" in context.browser.current_url

# Add a finalizer to close the browser


def after_scenario(context, scenario):
    context.browser.quit()
