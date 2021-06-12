from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    login_form = (By.CSS_SELECTOR, "#login_form")
    register_form = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    actual_book = (By.CSS_SELECTOR, '.product_main > h1')
    actual_price = (By.CSS_SELECTOR, '.product_main .price_color')
    name_book = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    price_of_book = (By.CSS_SELECTOR, '#messages > div:nth-child(3) > div > p > strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alertinner strong')