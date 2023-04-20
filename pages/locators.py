from selenium.webdriver.common.by import By


class MainPageLocators():
    #LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK = (By.XPATH, "//button[contains(@aria-label, 'Войти')]")
    LOGIN_LINK_BY_YANDEX_ID = (By.XPATH, "//a[contains(@aria-label, 'Войти через Яндекс ID')]")
    LOGIN_FIELD_BY_YANDEX_ID = (By.ID, "passp-field-login")
    PASSWORD_BUTTON_BY_YANDEX_ID = (By.ID, "passp:sign-in")
    PASSWORD_FIELD_BY_YANDEX_ID = (By.ID, "passp-field-passwd")

class DrivePageLocators():
    BUTTON_CREATE_RESOURCE = (By.XPATH, "/html/body/div[1]/div/div/div[3]/div[1]/div[1]/div/div/span[2]/button")

    BUTTON_CREATE_FOLDER = (By.XPATH,"/html/body/div[3]/div/button[1]")
    FOLDER_NAME_FIELD = (By.XPATH,"/html/body/div[4]/div[2]/div/div/div/div/div/div[1]/div/form/span/input")
    SAVE_FOLDER_NAME_BUTTON = (By.XPATH, "/html/body/div[4]/div[2]/div/div/div/div/div/div[2]/button")

    BUTTON_CREATE_TEXT_FILE = (By.XPATH,"/html/body/div[3]/div/button[2]")
    TEXT_FILE_NAME_FIELD = (By.XPATH, "/html/body/div[4]/div[2]/div/div/div/div/div/div[1]/div/form/span/input")
    SAVE_TEXT_FILE_BUTTON = (By.XPATH, "/html/body/div[4]/div[2]/div/div/div/div/div/div[2]/button")

