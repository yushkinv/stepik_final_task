from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group :nth-child(1).btn")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BASKET_FORM = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRODUCT_ADD_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, "#messages :nth-child(1) :nth-child(2) strong")
    PRICE_ADD_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, "#messages :nth-child(3) :nth-child(2) strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#content_inner h1")
    PRICE = (By.CSS_SELECTOR, "#content_inner .col-sm-6 .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages :nth-child(1).alert")

class BasketPageLocators():
    EMPTY_BASKET_FORM = (By.CSS_SELECTOR, "#content_inner>p")
    BASKET_TITLE = (By.CSS_SELECTOR, "#content_inner .basket-title")

