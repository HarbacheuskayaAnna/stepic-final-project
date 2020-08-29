from pages.base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def guest_can_add_product_to_basket(self):

        basket = self.browser.find_element(*ProductPageLocators.BASKET)
        basket.click()

    def should_be_the_same_product(self):
        product = self.browser.find_element(*ProductPageLocators.PRODUCT_TO_BASKET).text
        message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert product == message, f"The {product} should be instead of {message}"

    def should_be_the_same_price(self):
        prod_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        message_price = self.browser.find_element(*ProductPageLocators.INFO_PRICE).text
        assert prod_price == message_price, f"The price - {prod_price} is not equal {message_price}"

