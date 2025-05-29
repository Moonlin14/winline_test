from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class CybersportPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        with allure.step('Click to cybersport tab'):
            link = self.driver.find_element(By.XPATH, '//a[text()=" Киберспорт "]')
            link.click()

    def check_body_color(self):
        with allure.step('Check body color hex = #181637'):
            WebDriverWait(self.driver, 7).until(EC.visibility_of_element_located((By.XPATH, '//div[text()="Киберспорт"]')))
            body = self.driver.find_element(By.TAG_NAME, 'body')
            bg_color = body.value_of_css_property('background-color')
            hex = Color.from_string(bg_color).hex

            assert hex == '#181637', 'Ожидаемый цвет - #181637'