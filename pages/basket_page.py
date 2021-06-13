from .base_page import BasePage
from .locators import BasketPageLocators
import time

class BasketPage(BasePage):
    def check_basket(self):
        self.go_to_basket()
        time.sleep(5)
        self.should_be_empty()
        #self.should_not_be_items_in_basket()

    def should_be_empty(self):
        empty = self.browser.find_element(*BasketPageLocators.empty_basket).text
        assert "empty" in empty
        "Basket is not empty but should be"



    #def should_not_be_items_in_basket(self):
     #   assert self.is_not_element_present(*BasketPageLocators.empty_basket), \
      #      "Basket form present, but should not be"
