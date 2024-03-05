from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_see_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS),"Items in basket are presented, but should not be"
        basket_message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text
        assert basket_message == "Ваша корзина пуста Продолжить покупки", f"Received text:{basket_message} is not matching refference 'Ваша корзина пуста Продолжить покупки'"