import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='session')
def driver():

    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_experimental_option('prefs', {
        'download.default_directory': './winline_test/pdf',
        'download.prompt_for_download': False,
        'plugins.always_open_pdf_externally': True
    })

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get('https://winline.ru')
    
    yield driver
    driver.quit()