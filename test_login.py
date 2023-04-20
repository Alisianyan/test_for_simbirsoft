import pytest
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.drive_page import DrivePage
from pages.locators import MainPageLocators
import time

def test_login(browser):
    ##login = 'abc1636@yandex.ru'
    ##password = 'PurPur86'
    link = "http://yandex.ru/"
    foldername = "testtest"
    filename = "testtest"
    page = DrivePage(browser, link)
    page.open()
    time.sleep(15)
    page.test_authorizate()
    time.sleep(20)
    page.createfolder(foldername)
    time.sleep(5)
    page.openfolder(foldername)
    time.sleep(5)
    page.createfile(filename)
    time.sleep(5)
    page.close_file_tab()
    time.sleep(5)
    page.file_should_exist(filename)
