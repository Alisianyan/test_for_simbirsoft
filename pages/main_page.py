from .base_page import BasePage ##импортируем конструктор(browser, url) и метод open
from selenium.webdriver.common.by import By
from pages.locators import MainPageLocators
import sys

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)