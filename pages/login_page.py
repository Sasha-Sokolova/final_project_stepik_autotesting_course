from .base_page import BasePage
from .locators import *
import time # в начале файла

email = str(time.time()) + "@fakemail.org"

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_form()
        self.should_be_register_form()


    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.login_form), "Login form is not presented"


    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.register_form), "Register form is not presented"

    def register_new_user(self, email):
        self.browser.find_element(*RegisterPageLocators.email_id).send_keys(email)
        self.browser.find_element(*RegisterPageLocators.password_id).send_keys("something2021")
        self.browser.find_element(*RegisterPageLocators.password_confirm).send_keys("something2021")
        self.browser.find_element(*RegisterPageLocators.button_confirm).click()

