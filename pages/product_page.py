from .base_page import BasePage
import time
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.browser.find_element_by_xpath("//button[@class='btn btn-lg btn-primary btn-add-to-basket']").click()
        self.solve_quiz_and_get_code()
        self.check_that_book_was_added()
        self.check_the_price()



    def check_that_book_was_added(self):
        time.sleep(2)
        book = self.browser.find_element(*ProductPageLocators.actual_book).text
        check = self.browser.find_element(*ProductPageLocators.name_book).text
        assert check == book


    def check_the_price(self):
        sum = self.browser.find_element(*ProductPageLocators.actual_price).text
        price = self.browser.find_element(*ProductPageLocators.price_of_book).text
        print(sum, price)
        assert price == sum

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is disappeared"




