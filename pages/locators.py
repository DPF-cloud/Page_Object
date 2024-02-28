from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")

class LoginPageLocators():
    LOGIN_URL = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#content_inner > div > div.col-sm-6.login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#content_inner > div > div.col-sm-6.register_form")