from .pages.product_page import *
import pytest
from .pages.basket_page import BasketPage
from .pages.login_page import *

# команда для запуска тестов в финальной проверке: pytest -v --tb=line --language=en -m need_review


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.check_basket()


@pytest.mark.need_review
@pytest.mark.parametrize('promo_offer', ["0","1", "3", "4", "5", "6",
                                         pytest.param("7", marks=pytest.mark.xfail),
                                         "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()

@pytest.mark.xfail(reason="it fails because there is a success message")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    time.sleep(5)
    page.is_not_element_present()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="it fails because there is a success message and it wont disappear")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.is_disappeared()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.page = LoginPage(browser, 'http://selenium1py.pythonanywhere.com/')
        self.page.open()
        self.page.go_to_login_page()
        self.page.register_new_user(email)
        time.sleep(5)
        self.page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        self.link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
        self.page = ProductPage(browser, self.link)
        self.page.open()
        self.page.add_product_to_basket()


    @pytest.mark.xfail(reason='Тест упадет, потому что имейл уже занят')
    def test_user_cant_see_success_message(self, browser):
        self.link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/'
        self.page = ProductPage(browser, self.link)
        self.page.open()
        self.page.should_not_be_success_message()






