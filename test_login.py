import sys
sys.path.append("./pages")
sys.path.append(".")

import pytest
from pages.drive_page import DrivePage
import time



def test_login(browser):

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
