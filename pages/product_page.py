from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.BASKET_FORM)
        link.click()

    def should_be_product_name(self):
        product_basket_text = self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_TO_BASKET_MESSAGE).text
        product_text = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert product_basket_text == product_text, "Product name in basket is not equal to current product name"

    def should_be_product_price(self):
        basket_price_text = self.browser.find_element(*ProductPageLocators.PRICE_ADD_TO_BASKET_MESSAGE).text
        price_text = self.browser.find_element(*ProductPageLocators.PRICE).text
        assert basket_price_text == price_text, "Price in basket is not equal to current price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is disappeared, but should not be"
