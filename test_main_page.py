import pytest
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.locators import MainPageLocators
from .pages.locators import BasePageLocators

@pytest.mark.main_page_via_guest
class TestMainPageAsGuest:
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        url = MainPageLocators.MAIN_URL
        page = MainPage(browser, url)
        page.open()
        page.go_to_basket_page()
        page = BasketPage(browser, url)
        page.should_not_see_items_in_basket()


    def test_guest_should_see_login_link(self, browser):
        url = MainPageLocators.MAIN_URL
        page = MainPage(browser, url)
        page.open()
        page.should_be_login_link()


    def test_guest_can_go_to_login_page(self, browser):
        url = MainPageLocators.MAIN_URL
        page = MainPage(browser, url)
        page.open()
        page.go_to_login_page()


    def test_should_be_login_page(self, browser):
        url = BasePageLocators.LOGIN_URL
        page = LoginPage(browser, url)
        page.open()
        page.should_be_login_page()
