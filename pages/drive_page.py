##наследуются все остальные классы. Тут вспомогательные методы для работы с браузером
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time
from pages.base_page import BasePage
from pages.locators import DrivePageLocators as DPL
import requests
from selenium.webdriver.common.by import By

class DrivePage(BasePage):
    def createfolder(self, foldername):
        self.browser.get("https://disk.yandex.ru/client/disk")
        self.browser.find_element(*DPL.BUTTON_CREATE_RESOURCE).click()
        time.sleep(9)
        self.browser.find_element(*DPL.BUTTON_CREATE_FOLDER).click()
        time.sleep(9)
        self.browser.find_element(*DPL.FOLDER_NAME_FIELD).send_keys(foldername)
        time.sleep(5)
        self.browser.find_element(*DPL.SAVE_FOLDER_NAME_BUTTON).click()

    def openfolder(self, foldername):
        url = str("https://disk.yandex.ru/client/disk" + foldername)
        self.browser.get(url)

    def createfile(self, filename):
        self.browser.find_element(*DPL.BUTTON_CREATE_RESOURCE).click()
        time.sleep(3)
        self.browser.find_element(*DPL.BUTTON_CREATE_TEXT_FILE).click()
        time.sleep(3)
        self.browser.find_element(*DPL.TEXT_FILE_NAME_FIELD).send_keys(filename)
        time.sleep(3)
        self.browser.find_element(*DPL.SAVE_TEXT_FILE_BUTTON).click()

    def close_file_tab(self):
        file_tab = self.browser.window_handles[1]
        self.browser.switch_to.window(file_tab)
        self.browser.close()

    def file_should_exist(self, filename):
        xpath_string = '//div[contains(@aria-label,{})]'.format(filename)
        try:
            self.browser.find_element(By.XPATH, xpath_string)
        except NoSuchElementException:
            return False
        return True






