from pages.base_page import BasePage
from pages.locators import BasePageLocators

class BasketPage(BasePage):
    def should_be_empty_basket(self):
        message = self.browser.find_element(*BasePageLocators.EMPTY_BASKET_MESSAGE).text
        assert "empty" in message, f"The basket is not empty"