from locators import RegistrationPageLocators
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def register(self, name, email, password):
        self.wait_for_overlay(RegistrationPageLocators.NAME_FIELD)
        self.input_text(RegistrationPageLocators.NAME_FIELD, name)
        self.input_text(RegistrationPageLocators.EMAIL_FIELD, email)
        self.input_text(RegistrationPageLocators.PASSWORD_FIELD, password)
        self.click_with_wait(RegistrationPageLocators.REGISTER_BUTTON)
