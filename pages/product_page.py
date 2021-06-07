from .base_page import BasePage
import time
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.browser.find_element_by_xpath("//button[@value='Добавить в корзину']").click()
        self.solve_quiz_and_get_code()
        self.check_that_book_was_added()
        self.check_the_price()

    def check_that_book_was_added(self):
        time.sleep(2)
        check = self.browser.find_element(*ProductPageLocators.name_book).text
        assert check == "The shellcoder's handbook"


    def check_the_price(self):
        price = self.browser.find_element(*ProductPageLocators.price_of_book).text
        assert "9,99" in price

