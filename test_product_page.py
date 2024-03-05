import pytest
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators, BasePageLocators


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_should_see_login_link_on_product_page(self, browser):
        url = ProductPageLocators.PRODUCT_URL
        page = ProductPage(browser, url)
        page.open()
        page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page(browser):
    url = ProductPageLocators.PRODUCT_URL
    page = ProductPage(browser, url)
    page.open()
    page.go_to_login_page()


@pytest.mark.user_add_to_basket
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):  # Сделано не так, как предложено в задании, но раз мы применяем ООП, то так лучше
        self.login_page = LoginPage(browser, BasePageLocators.LOGIN_URL)
        self.login_page.open()
        self.login_page.register_new_user()
        self.login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        url = ProductPageLocators.PRODUCT_URL
        page = ProductPage(browser, url)
        page.open()
        page.should_not_be_success_message()

    def test_user_cant_see_product_in_basket_opened_from_product_page(self, browser):
        url = ProductPageLocators.PRODUCT_URL
        page = ProductPage(browser, url)
        page.open()
        page.go_to_basket_page()
        page = BasketPage(browser, url)
        page.should_not_see_items_in_basket()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        url = ProductPageLocators.PRODUCT_URL
        page = ProductPage(browser, url)
        page.open()
        page.add_to_cart()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    url = ProductPageLocators.PRODUCT_URL
    page = ProductPage(browser, url)
    page.open()
    page.add_to_cart()


def test_add_product_name_correct(browser):
    url = ProductPageLocators.PRODUCT_URL
    page = ProductPage(browser, url)
    page.open()
    page.name_of_product_correct()


def test_add_product_price_correct(browser):
    url = ProductPageLocators.PRODUCT_URL
    page = ProductPage(browser, url)
    page.open()
    page.price_of_product_correct()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    url = ProductPageLocators.PRODUCT_URL
    page = ProductPage(browser, url)
    page.open()
    page.go_to_basket_page()
    page = BasketPage(browser, url)
    page.should_not_see_items_in_basket()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    url = ProductPageLocators.PRODUCT_URL
    page = ProductPage(browser, url)
    page.open()
    page.add_to_cart()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    url = ProductPageLocators.PRODUCT_URL
    page = ProductPage(browser, url)
    page.open()
    page.add_to_cart()
    page.success_message_should_disappear()
