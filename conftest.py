import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


supported_browsers = {
    'chrome': webdriver.Chrome,
    'firefox': webdriver.Firefox
}

supported_languages = {
    'العربيّة': 'ar',
    'català': 'ca',
    'česky': 'cs',
    'dansk': 'da',
    'Deutsch': 'de',
    'British English': 'en-gb',
    'Ελληνικά': 'el',
    'español': 'es',
    'suomi': 'fi',
    'français': 'fr',
    'italiano': 'it',
    '한국어': 'ko',
    'Nederlands': 'nl',
    'polski': 'pl',
    'Português': 'pt',
    'Português Brasileiro': 'pt-br',
    'Română': 'ro',
    'Русский': 'ru',
    'Slovensky': 'sk',
    'Українська': 'uk',
    '简体中文': 'zh-hans'
}

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='ru',
                     help=f"""Choose language: {', '.join(supported_languages.keys())}""")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")

    if browser_name not in supported_browsers:
        joined_browsers = ', '.join(supported_browsers.keys())
        raise pytest.UsageError(f"--browser_name is invalid, supported browsers: {joined_browsers}")

    if language in supported_languages.values():
        if browser_name == 'chrome':
            options = Options()
            options.add_experimental_option('prefs', {'intl.accept_languages': language})
            browser = webdriver.Chrome(options=options)
        elif browser_name == 'firefox':
            fp = webdriver.FirefoxProfile()
            fp.set_preference("intl.accept_languages", language)
            browser = webdriver.Firefox(firefox_profile=fp)
    else:
        joined_languages = ', '.join(supported_languages.keys())
        raise pytest.UsageError(f"--language is invalid, supported languages: {joined_languages}")

    yield browser
    print("\nquit browser..")
    browser.quit()