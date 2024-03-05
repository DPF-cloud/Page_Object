import pytest
import time
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.locators import MainPageLocators
from .pages.locators import BasePageLocators


@pytest.mark.parametrize('link', MainPageLocators.MAIN_URL)
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser, link):
    url = link
    page = MainPage(browser, url)
    page.open()
    page.go_to_basket_page()
    page = BasketPage(browser, url)
    page.should_not_see_items_in_basket()

@pytest.mark.parametrize('link', MainPageLocators.MAIN_URL)
def test_guest_should_see_login_link(browser, link):
    url = link
    page = MainPage(browser, url)
    page.open()
    page.should_be_login_link()
  
@pytest.mark.parametrize('link', MainPageLocators.MAIN_URL)
def test_guest_can_go_to_login_page(browser, link):
    url = link
    page = MainPage(browser, url)
    page.open()
    page.go_to_login_page()



@pytest.mark.parametrize('link', BasePageLocators.LOGIN_URL)
def test_should_be_login_page(browser, link):
    url = link
    page = LoginPage(browser, url)
    page.open()
    time.sleep(2)
    page.should_be_login_page()
    time.sleep(2)