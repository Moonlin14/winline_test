from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AboutAsPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        self.driver.implicitly_wait(5)
        link = self.driver.find_element(By.XPATH, '//a[text()=" О нас "]')
        link.click()

    def is_support_h1_visible(self):
        assert self.driver.find_element(By.CSS_SELECTOR, 'h1').is_displayed()

    def support_button_click(self):
        button = self.driver.find_element(By.XPATH, '//div[contains(@class, "webim-html-button-element")]')
        button.click()

    def is_support_chat_modal_visible(self, bool):
        if bool == True:
            WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//div[text()="Для начала диалога введите, пожалуйста, свою контактную информацию и вопрос."]')))

        assert self.driver.find_element(By.XPATH, '//div[text()="Для начала диалога введите, пожалуйста, свою контактную информацию и вопрос."]').is_displayed() == bool

    def close_support_chat_modal(self):
        button = self.driver.find_element(By.XPATH, '//div[contains(@class, "webim-action-close")]')
        button.click()