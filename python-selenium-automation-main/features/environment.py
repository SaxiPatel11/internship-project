# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# from selenium.webdriver.firefox.options import Options as FirefoxOptions
# from selenium.webdriver.firefox.service import Service as FirefoxService
#
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# import os
#
# # def browser_init(context):
# #     """
# #     :param context: Behave context
# #     """
# #     driver_path = ChromeDriverManager().install()
# #     service = Service(driver_path)
# #     context.driver = webdriver.Chrome(service=service)
# #
# #     context.driver.maximize_window()
# #     context.driver.implicitly_wait(4)
#
#
# def browser_init(context):
#     browser = os.getenv("BROWSER", "chrome")
#
#     if browser.lower() == "firefox":
#         firefox_options = FirefoxOptions()
#         firefox_options.add_argument("--headless")
#
#         service = FirefoxService(GeckoDriverManager().install())
#         context.driver = webdriver.Firefox(
#             service=service,
#             options=firefox_options
#         )
#
#     else:
#         chrome_options = ChromeOptions()
#         chrome_options.add_argument("--headless=new")
#         chrome_options.add_argument("--window-size=1920,1080")
#
#         service = Service(ChromeDriverManager().install())
#         context.driver = webdriver.Chrome(
#             service=service,
#             options=chrome_options
#         )
#
#     context.driver.implicitly_wait(4)
#
# def before_scenario(context, scenario):
#     print('\nStarted scenario: ', scenario.name)
#     browser_init(context)
#
#
# def before_step(context, step):
#     print('\nStarted step: ', step)
#
#
# def after_step(context, step):
#     if step.status == 'failed':
#         print('\nStep failed: ', step)
#
#
# def after_scenario(context, feature):
#     context.driver.quit()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import os


def browser_init(context):
    browser = os.getenv("BROWSER", "chrome")
    use_cloud = os.getenv("USE_CLOUD", "false").lower() == "true"

    # =========================
    # CLOUD EXECUTION (BrowserStack)
    # =========================
    if use_cloud:
        USERNAME = os.getenv("CLOUD_USER")
        ACCESS_KEY = os.getenv("CLOUD_KEY")

        hub_url = f"https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"

        capabilities = {
            "browserName": browser,
            "browserVersion": "latest",
            "os": "Windows",
            "osVersion": "11",
            "name": context.scenario.name
        }

        context.driver = webdriver.Remote(
            command_executor=hub_url,
            desired_capabilities=capabilities
        )

    # =========================
    # LOCAL EXECUTION
    # =========================
    else:
        if browser.lower() == "firefox":
            firefox_options = FirefoxOptions()
            firefox_options.add_argument("--headless")

            service = FirefoxService(GeckoDriverManager().install())
            context.driver = webdriver.Firefox(
                service=service,
                options=firefox_options
            )

        else:
            chrome_options = ChromeOptions()
            chrome_options.add_argument("--headless=new")
            chrome_options.add_argument("--window-size=1920,1080")

            service = Service(ChromeDriverManager().install())
            context.driver = webdriver.Chrome(
                service=service,
                options=chrome_options
            )

    context.driver.implicitly_wait(4)


# =========================
# BEHAVE HOOKS
# =========================

def before_scenario(context, scenario):
    print("\nStarted scenario:", scenario.name)
    browser_init(context)


def before_step(context, step):
    print("\nStarted step:", step.name)


def after_step(context, step):
    if step.status == "failed":
        print("\nStep failed:", step.name)


def after_scenario(context, scenario):
    print("\nFinished scenario:", scenario.name)
    context.driver.quit()