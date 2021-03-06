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

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    basket_link = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs > span > a")
    empty_basket = (By.CSS_SELECTOR, "div#content_inner > p")

class RegisterPageLocators():
    email_id = (By.CSS_SELECTOR, '#id_registration-email')
    password_id = (By.CSS_SELECTOR, '#id_registration-password1')
    password_confirm = (By.CSS_SELECTOR, '#id_registration-password2')
    button_confirm = (By.CSS_SELECTOR, 'form#register_form > button.btn.btn-lg.btn-primary')

