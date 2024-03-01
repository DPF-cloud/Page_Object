import pytest
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
'''
@pytest.mark.parametrize('link',ProductPageLocators.TEST_DATA)
def test_guest_can_add_product_to_basket(browser, link):
    url = link
    page = ProductPage(browser, url)
    page.open()
    page.should_be_able_to_add()
    page.solve_quiz_and_get_code()
'''
@pytest.mark.parametrize('link',ProductPageLocators.TEST_DATA)
def test_add_product_name_correct(browser, link):
    url = link
    page = ProductPage(browser, url)
    page.open()
    page.name_of_product_correct()
'''
@pytest.mark.parametrize('link',ProductPageLocators.TEST_DATA)
def test_add_product_price_correct(browser, link):
    url = link
    page = ProductPage(browser, url)
    page.open()
    page.price_of_product_correct()
'''