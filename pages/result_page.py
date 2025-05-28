from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class ResultPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        self.driver.implicitly_wait(5)
        link = self.driver.find_element(By.XPATH, '//a[text()=" Результаты "]')
        link.click()

    def switch_dropbar_category(self, category):
        dropbar = self.driver.find_element(By.NAME, 'sport')
        dropbar.click()
        category_to_switch = self.driver.find_element(By.XPATH, f'//option[text()="{category}"]')
        category_to_switch.is_displayed()
        category_to_switch.click()

    def switch_dropbar_championship(self):
        dropbar = self.driver.find_element(By.NAME, 'championships')
        dropbar.click()
        champoinship_to_switch = self.driver.find_element(By.XPATH, '//*[@id="main"]/div[1]/div[1]/ww-feature-results-gen/div/div[1]/form/div[2]/select/option[2]')
        champoinship_to_switch.is_displayed()
        champoinship_to_switch.click()

    def is_results_visible(self):
        result_date = self.driver.find_element(By.XPATH, '//div[@class="result-item__date"]')
        result_date.is_displayed()
        result_time = self.driver.find_element(By.XPATH, '//div[@class="result-item__time"]')
        result_time.is_displayed()
        result_members = self.driver.find_element(By.XPATH, '//div[@class="result-item__members"]')
        result_members.is_displayed()
        result_score = self.driver.find_element(By.XPATH, '//div[@class="result-item__score"]')
        result_score.is_displayed()