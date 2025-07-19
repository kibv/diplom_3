from locators import LoginPageLocators, MainPageLocators
from data.data import URLs

from locators import RegistrationPageLocators
from pages.base_page import BasePage

class RegisterPage(BasePage):
    def register(self, name, email, password):
        self.wait_for_overlay(RegistrationPageLocators.NAME_FIELD)
        self.input_text(RegistrationPageLocators.NAME_FIELD, name)
        self.input_text(RegistrationPageLocators.EMAIL_FIELD, email)
        self.input_text(RegistrationPageLocators.PASSWORD_FIELD, password)
        self.click_with_wait(RegistrationPageLocators.REGISTER_BUTTON)

class LoginPage(BasePage):
    def open(self, url=URLs.LOGIN_URL):
        super().open(url)

    def new_registrathion(self):
        self.click(LoginPageLocators.RESET_REGISTRATION_LINK)

    def wait_el(self):
        self.wait_page_loaded(MainPageLocators.CONSTRUCTOR_BUTTON)

    def login(self, email, password):
        self.input_text(LoginPageLocators.EMAIL_INPUT, email)
        self.input_text(LoginPageLocators.PASSWORD_INPUT, password)
        self.click_with_wait(LoginPageLocators.LOGIN_BUTTON)

    def click_reset_password(self):
        self.click(LoginPageLocators.RESET_PASSWORD_LINK)

    def wait_url(self, url):
        self.wait_for_url(url, 10)
