from selenium.webdriver.common.by import By


class SettingsPage:

    SETTINGS_BTN = (By.XPATH, "//a[contains(text(),'Settings')]")
    CHANGE_PASSWORD_LINK = (By.XPATH, "//a[contains(text(),'Change password')]")

    def __init__(self, driver):
        self.driver = driver

    def open_settings(self):
        self.driver.find_element(*self.SETTINGS_BTN).click()

    def open_change_password(self):
        self.driver.find_element(*self.CHANGE_PASSWORD_LINK).click()