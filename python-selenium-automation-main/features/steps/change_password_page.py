from selenium.webdriver.common.by import By


class ChangePasswordPage:

    PAGE_TITLE = (By.XPATH, "//div[contains(text(),'Change password')]")
    CURRENT_PASSWORD = (By.NAME, "currentPassword")
    NEW_PASSWORD = (By.NAME, "newPassword")
    CONFIRM_PASSWORD = (By.NAME, "confirmPassword")
    CHANGE_PASSWORD_BTN = (By.XPATH, "//button[contains(text(),'Change password')]")

    def __init__(self, driver):
        self.driver = driver

    def verify_page_opened(self):
        return self.driver.find_element(*self.PAGE_TITLE).is_displayed()

    def fill_passwords(self):
        self.driver.find_element(*self.CURRENT_PASSWORD).send_keys("Test123!")
        self.driver.find_element(*self.NEW_PASSWORD).send_keys("NewPass123!")
        self.driver.find_element(*self.CONFIRM_PASSWORD).send_keys("NewPass123!")

    def is_change_password_button_displayed(self):
        return self.driver.find_element(*self.CHANGE_PASSWORD_BTN).is_displayed()