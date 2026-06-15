from behave import given, when, then
from selenium.webdriver.common.by import By
import time


@given('User opens Reelly login page')
def open_login_page(context):
    context.driver.get('https://soft.reelly.io')


@when('User logs in')
def login(context):
    context.driver.find_element(By.ID, 'email-2').send_keys('YOUR_EMAIL')
    context.driver.find_element(By.ID, 'field').send_keys('YOUR_PASSWORD')

    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    time.sleep(3)


@when('User clicks Settings option')
def click_settings(context):
    context.driver.find_element(
        By.XPATH,
        "//a[contains(text(),'Settings')]"
    ).click()

    time.sleep(2)


@when('User clicks Change Password option')
def click_change_password(context):
    context.driver.find_element(
        By.XPATH,
        "//a[contains(text(),'Change password')]"
    ).click()

    time.sleep(2)


@then('Verify Change Password page opens')
def verify_page(context):
    page_title = context.driver.find_element(
        By.XPATH,
        "//*[contains(text(),'Change password')]"
    )

    assert page_title.is_displayed(), \
        "Change Password page did not open"


@then('User enters test passwords')
def enter_passwords(context):
    context.driver.find_element(
        By.NAME,
        'currentPassword'
    ).send_keys('Test123!')

    context.driver.find_element(
        By.NAME,
        'newPassword'
    ).send_keys('NewPass123!')

    context.driver.find_element(
        By.NAME,
        'confirmPassword'
    ).send_keys('NewPass123!')


@then('Verify Change Password button is displayed')
def verify_button(context):
    button = context.driver.find_element(
        By.XPATH,
        "//button[contains(text(),'Change password')]"
    )

    assert button.is_displayed(), \
        "Change Password button is not displayed"