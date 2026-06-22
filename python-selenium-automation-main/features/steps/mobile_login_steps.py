from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('User opens Reelly login page on mobile')
def open_login(context):
    context.driver.get("https://soft.reelly.io/sign-in")


@when('User enters email and password')
def enter_credentials(context):
    wait = WebDriverWait(context.driver, 10)

    email_input = wait.until(
        EC.presence_of_element_located((By.NAME, "email"))
    )
    password_input = wait.until(
        EC.presence_of_element_located((By.NAME, "password"))
    )

    email_input.send_keys("your_email_here")
    password_input.send_keys("your_password_here")


@when('User clicks Login button')
def click_login(context):
    wait = WebDriverWait(context.driver, 10)

    login_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[text()='Continue']")
        )
    )
    login_button.click()


@then('User should be logged in successfully')
def verify_login(context):
    wait = WebDriverWait(context.driver, 10)

    wait.until(
        EC.url_contains("dashboard")
    )

    assert "dashboard" in context.driver.current_url