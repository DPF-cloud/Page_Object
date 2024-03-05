from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_URL = "https://selenium1py.pythonanywhere.com/ru/accounts/login"
    LOGIN_INCORRECT_URL = "http://selenium1py.pythonanywhere"
    LOGIN_BUTTON = (By.ID, "login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    USER_ICON = (By.CSS_SELECTOR, "#top_page > div.navbar-collapse.account-collapse.collapse > div > ul > li:nth-child(1) > a > i")

class MainPageLocators():
    MAIN_URL = "https://selenium1py.pythonanywhere.com/ru/"

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#content_inner > div > div.col-sm-6.login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#content_inner > div > div.col-sm-6.register_form")
    EMAIL_REGISTER_FORM= (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_REGISTER_FORM = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_REGISTER_FORM_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_SUBMIT_BUTTON = (By.CSS_SELECTOR, "#register_form > button")

class ProductPageLocators():
    PRODUCT_URL = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    ADD_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    PRICE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    NAME = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    ALERT_PRICE = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    ALERT_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")

class BasketPageLocators():
    ITEMS = (By.CSS_SELECTOR, "#basket_formset > div")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner > p")