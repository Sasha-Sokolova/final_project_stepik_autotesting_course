from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import *

class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/"
        self.page = MainPage(browser, self.link)
        self.page.open()
        self.page.go_to_login_page()
        self.login_page = LoginPage(browser, browser.current_url)
        self.login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/"
        self.page = MainPage(browser, self.link)
        self.page.open()
        self.page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.check_basket()







