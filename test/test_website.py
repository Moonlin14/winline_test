from pages.home_page import HomePage
from pages.cybersport_page import CybersportPage
from pages.result_page import ResultPage
from pages.abot_as_page import AboutAsPage
import pytest

def test_color_of_mainpage(driver):

    home_page = HomePage(driver)
    cybersportpage = CybersportPage(driver)
    
    home_page.check_body_color()

    cybersportpage.open()
    cybersportpage.check_body_color()

@pytest.mark.xfail()
def test_coupon_modal(driver):

    home_page = HomePage(driver)

    home_page.click_category(num=1)

    home_page.fill_coupon()
    home_page.check_coupon_coef()

    home_page.fill_bet_input(777)
    home_page.is_payment_check_correct_visible(777)

    home_page.click_coupon()
    home_page.click_coupon()
    home_page.is_coupon_open()

    home_page.clear_coefs()

CATEGORY = ['Баскетбол', 'Крикет' ,'Теннис', 'Волейбол']

@pytest.mark.parametrize('category', CATEGORY)

def test_match_result_visible(driver, category):
    result_page = ResultPage(driver)

    result_page.open()

    result_page.switch_dropbar_category(category)
    result_page.switch_dropbar_championship()
        
    result_page.is_results_visible()

def test_support_chat_modal(driver):
    about_as_page = AboutAsPage(driver)

    about_as_page.open()

    about_as_page.is_support_h1_visible()
    about_as_page.support_button_click()
    about_as_page.is_support_chat_modal_visible(bool=True)
    
    about_as_page.close_support_chat_modal()
    about_as_page.is_support_chat_modal_visible(bool=False)

@pytest.mark.xfail()
def test_check_footer_docs(driver):
    home_page = HomePage(driver)

    home_page.open_docs()
    home_page.click_doc(0)
    home_page.download_doc()
    home_page.check_pdf_strings()