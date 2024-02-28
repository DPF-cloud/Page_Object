from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer "
    browser.get(url)
    login_link = browser.find_element(By.CSS_SELECTOR, "#registration_link")
    login_link.click()

def test_guest_should_see_login_link(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer "
    page = MainPage(browser, url)
    page.open()
    page.should_be_login_link()

def test_should_be_login_page(browser):
    url = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, url)
    page.open()
    page.should_be_login_page()
