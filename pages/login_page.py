from locators import LoginPageLocators
from data.data import URLs
from pages.base_page import BasePage


class LoginPage(BasePage):

    def open(self, url=URLs.LOGIN_URL):
        super().open(url)

    def new_registration(self):
        self.click(LoginPageLocators.RESET_REGISTRATION_LINK)

    def login(self, email, password):
        self.input_text(LoginPageLocators.EMAIL_INPUT, email)
        self.input_text(LoginPageLocators.PASSWORD_INPUT, password)
        self.click_with_wait(LoginPageLocators.LOGIN_BUTTON)

    def click_reset_password(self):
        self.click(LoginPageLocators.RESET_PASSWORD_LINK)

    def wait_url(self, url):
        self.wait_for_url(url, 10)
