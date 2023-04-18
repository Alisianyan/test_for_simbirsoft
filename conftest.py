import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

def pytest_addoption(parser):
    ##добавляем возможность запускать тесты с параметрами вроде pytest --language=en
    parser.addoption('--language', action='store', default="ru", help="Enter language like en/ru/es")

@pytest.fixture(scope="function")
def language(request):
    ##добавляем значеие параметра language как переменную
    language=request.config.getoption("language")
    return language

@pytest.fixture(scope="function")
def browser():
    ##фикстура "браузер", которая запускает и закрываем браузер для каждого теста.
    browser=webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    yield browser
    browser.quit()