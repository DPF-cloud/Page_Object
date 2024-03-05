import time

from .base_page import BasePage
from .locators import BasePageLocators
from .locators import LoginPageLocators



class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        password = "Qwe123rty"
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_REGISTER_FORM)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTER_FORM)
        password_input.send_keys(password)
        password_input2 = self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTER_FORM_2)
        password_input2.send_keys(password)
        submit_button = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT_BUTTON )
        submit_button.click()

    def should_be_login_url(self):
        assert BasePageLocators.LOGIN_URL[0] in self.browser.current_url, f"Login url is not presented {BasePageLocators.LOGIN_URL} in {self.browser.current_url}"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
