from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_TITLE), \
        "Basket is not empty"


    def should_empty_basket_text_is_present(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_FORM), \
        "Text about empty basket is not presented"

