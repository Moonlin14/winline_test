from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pdfbox import PDFBox
import random

class HomePage:
    
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def check_body_color(self):
        self.driver.implicitly_wait(5)
        body = self.driver.find_element(By.TAG_NAME, 'body')
        bg_color = body.value_of_css_property('background-color')
        hex = Color.from_string(bg_color).hex
        
        assert hex == '#e2e6ee'

    def click_category(self, num):
        self.driver.implicitly_wait(5)
        category = self.driver.find_elements(By.XPATH, '//a[contains(@class, "topbar-button")]')
        category[num].click()

    def fill_coupon(self):
        #дописать комент про функционал
        lines_of_bet = self.driver.find_elements(By.XPATH, '//div[@class="card__central-part"]')

        for i in range(2):
            WebDriverWait(self.driver, 3).until(EC.visibility_of_all_elements_located((By.XPATH, '//div[contains(@class, "coefficient-button") and not(contains(@class, "empty"))]')))
            buttons = lines_of_bet[i].find_elements(By.XPATH, './/div[contains(@class, "coefficient-button") and not(contains(@class, "empty"))]')
            buttons[random.randint(0, len(buttons) - 1)].click()

    def click_coupon(self):   
        coupon = self.driver.find_element(By.XPATH, '//div[contains(@class, "ww-coupon-header__controls")]')
        coupon.click()

    def multiplication_coefs_in_coupon(self):
        coefs = self.driver.find_elements(By.XPATH, '//div[@class="ww-bets-item__coeff"]')
        result = 1
        for i in range(0, len(coefs)):
            result *= float(coefs[i].text)
        
        return round(result, 2)

    def check_coupon_coef(self):
        multiplication_coefs = self.multiplication_coefs_in_coupon()
        coef_to_check = self.driver.find_element(By.XPATH, '//*[@id="coupon"]/div[2]/div/div[2]/div[2]/div[1]/span').text
        print(multiplication_coefs, coef_to_check)
        assert coef_to_check == f'{multiplication_coefs}0'

    def fill_bet_input(self, value):
        input = self.driver.find_element(By.XPATH, '//input[@id="number-input"]')
        input.send_keys(value)

    def is_payment_check_correct_visible(self, value):
        coef = self.driver.find_element(By.XPATH, '//*[@id="coupon"]/div[2]/div/div[2]/div[2]/div[1]/span').text
        payment = self.driver.find_element(By.XPATH, '//div[contains(@class, "ww-coupon-total__label")]')
        payment_value = payment.text.replace(' ', '').split(':')
        multiply = value * float(coef)
        split = str(multiply).split('.')
        assert payment.is_displayed() and payment_value[1][:2] == split[0][:2]

    def is_coupon_visible(self):
        assert self.driver.find_element(By.XPATH, '//div[contains(@class, "ww-coupon--show")]')

    def clear_coefs(self):
        clear_button = self.driver.find_element(By.XPATH, '//div[contains(@class, "ww-coupon__btn-clear")]')
        clear_button.click()
        assert self.driver.find_element(By.XPATH, '//div[@class="ww-coupon-empty__text"]')

    def open_docs(self):
        #WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//a[text()="Основные документы"]')))
        self.driver.implicitly_wait(5)
        link = self.driver.find_element(By.XPATH, '//a[text()="Основные документы"]')
        self.driver.execute_script("arguments[0].scrollIntoView(true);", link)
        link.click()

    def click_doc(self, num):
        docs = self.driver.find_elements(By.XPATH, '//a[@class="doc"]')
        docs[num].click()
    
    def download_doc(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        link = self.driver.find_element(By.XPATH, '//*[@id="download"]')
        link.click()

    def check_pdf_strings(self):
        pdf = PDFBox()
        text = pdf.extract_text('./pdf/pravila-priema-stavok-i-vyplaty-vyigryshey.pdf')
        print(text[:30])