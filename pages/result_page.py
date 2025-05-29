from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import allure
from random import randint

class ResultPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        with allure.step('Click to results tab'):
            self.driver.implicitly_wait(5)
            link = self.driver.find_element(By.XPATH, '//a[text()=" Результаты "]')
            link.click()

    def switch_dropbar_category(self, category):
        with allure.step('Click on sports dropbar'):
            dropbar = self.driver.find_element(By.NAME, 'sport')
            dropbar.click()
        with allure.step('Switch category'):
            category_to_switch = self.driver.find_element(By.XPATH, f'//option[text()="{category}"]')
            category_to_switch.is_displayed()
            category_to_switch.click()

    def switch_dropbar_championship(self):
        with allure.step('Click championship dropbar'):
            dropbar = self.driver.find_element(By.NAME, 'championships')
            dropbar.click()
        with allure.step('Switch championship to random one'):
            self.driver.implicitly_wait(3)
            champoinships = dropbar.find_elements(By.XPATH, './/option[contains(@class,"ng-star-inserted")]')
            champoinship_to_switch = champoinships[randint(0, len(champoinships) - 1)]
            champoinship_to_switch.is_displayed()
            champoinship_to_switch.click()

    def is_results_visible(self):
        with allure.step('Check results date, time, members and score is visible'):
            self.driver.implicitly_wait(5)
            result_date = self.driver.find_element(By.XPATH, '//div[@class="result-item__date"]')
            result_date.is_displayed()
            result_time = self.driver.find_element(By.XPATH, '//div[@class="result-item__time"]')
            result_time.is_displayed()
            result_members = self.driver.find_element(By.XPATH, '//div[@class="result-item__members"]')
            result_members.is_displayed()
            result_score = self.driver.find_element(By.XPATH, '//div[@class="result-item__score"]')
            result_score.is_displayed()