from .base_page import BasePage
from .locators import BasketPageLocators
import time

class BasketPage(BasePage):
    def check_basket(self):
        self.go_to_basket()
        time.sleep(5)
        self.should_be_empty()

    def should_be_empty(self):
        empty = self.browser.find_element(*BasketPageLocators.empty_basket).text
        assert "empty" in empty
        "Basket is not empty but should be"


