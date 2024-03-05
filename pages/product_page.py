from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math
import time


class ProductPage(BasePage):
    def add_to_cart(self):
        self.browser.find_element(*ProductPageLocators.ADD_BUTTON).click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        time.sleep(1)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def name_of_product_correct(self):
        name = self.browser.find_element(*ProductPageLocators.NAME).text
        self.add_to_cart()
        alert_name = self.browser.find_element(*ProductPageLocators.ALERT_NAME).text
        assert name == alert_name, "Name incorrect, mismatch between name and alert name"

    def price_of_product_correct(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        self.add_to_cart()
        alert_price = self.browser.find_element(*ProductPageLocators.ALERT_PRICE).text
        assert price == alert_price, "Price incorrect, mismatch between price and alert_price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
