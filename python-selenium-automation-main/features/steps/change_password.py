from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('User opens Reelly login page')
def open_login_page(context):
    context.driver.get('https://soft.reelly.io')


@when('User logs in')
def login(context):
    wait = WebDriverWait(context.driver, 10)

    email = wait.until(
        EC.presence_of_element_located((By.ID, 'email-2'))
    )
    password = wait.until(
        EC.presence_of_element_located((By.ID, 'field'))
    )

    email.send_keys('YOUR_EMAIL')
    password.send_keys('YOUR_PASSWORD')

    login_btn = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@type='submit']")
        )
    )
    login_btn.click()


@when('User clicks Settings option')
def click_settings(context):
    wait = WebDriverWait(context.driver, 10)

    settings_btn = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(text(),'Settings')]")
        )
    )
    settings_btn.click()


@when('User clicks Change Password option')
def click_change_password(context):
    wait = WebDriverWait(context.driver, 10)

    change_password_btn = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(text(),'Change password')]")
        )
    )
    change_password_btn.click()


@then('Verify Change Password page opens')
def verify_page(context):
    wait = WebDriverWait(context.driver, 10)

    page_title = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(text(),'Change password')]")
        )
    )

    assert page_title.is_displayed()


@then('User enters test passwords')
def enter_passwords(context):
    wait = WebDriverWait(context.driver, 10)

    wait.until(
        EC.presence_of_element_located(
            (By.NAME, 'currentPassword')
        )
    ).send_keys('Test123!')

    context.driver.find_element(
        By.NAME, 'newPassword'
    ).send_keys('NewPass123!')

    context.driver.find_element(
        By.NAME, 'confirmPassword'
    ).send_keys('NewPass123!')


@then('Verify Change Password button is displayed')
def verify_button(context):
    wait = WebDriverWait(context.driver, 10)

    button = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//button[contains(text(),'Change password')]")
        )
    )

    assert button.is_displayed()