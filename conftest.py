# from distutils.command.config import config
from requests import request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pytest


# путь до chromedriver
path_to_driver = 'chromedriver'

driver_service = Service(executable_path=path_to_driver)
options = Options()

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose lang: ru or fr or es or en. For example --language=es", choices=("ru", "fr" , "es", "en",))


@pytest.fixture
def browser(request):
    print('\nbrowser start')
    language = request.config.getoption('language')
    options.add_experimental_option('prefs',{'intl.accept_languages': language})
    browser = webdriver.Chrome(service=driver_service, options=options)
    yield browser
    print('\nbrowser quit')
    browser.quit()
