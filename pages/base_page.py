import csv
import time
from pages.locators import MainPageLocators

class BasePage():
    login = ""
    password = ""
    with open("pages/creds.csv", "r") as file:
        reader = csv.reader(file)
        creds = next(reader)
        login = creds[0]
        password = creds[1]
        print(login, password)

    def __init__(self, browser, url, timeout=10):  ##конструктор
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def test_authorizate(self):

        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        time.sleep(9)
        login_button_yandex_id = self.browser.find_element(*MainPageLocators.LOGIN_LINK_BY_YANDEX_ID)
        login_button_yandex_id.click()
        time.sleep(7)

        login_field_yandex_id = self.browser.find_element(*MainPageLocators.LOGIN_FIELD_BY_YANDEX_ID)
        login_field_yandex_id.send_keys(self.login)
        login_button = self.browser.find_element(*MainPageLocators.PASSWORD_BUTTON_BY_YANDEX_ID)
        login_button.click()
        time.sleep(7)
        passwd_field_yandex_id = self.browser.find_element(*MainPageLocators.PASSWORD_FIELD_BY_YANDEX_ID)
        passwd_field_yandex_id.send_keys(self.password)
        login_button = self.browser.find_element(*MainPageLocators.PASSWORD_BUTTON_BY_YANDEX_ID)
        time.sleep(15)
        login_button.click()
