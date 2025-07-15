from locators import ResetPasswordPageLocators
from pages.base_page import BasePage

class ResetPasswordPage(BasePage):
    def input_email(self, email):
        self.input_text(ResetPasswordPageLocators.EMAIL_INPUT, email)

    def input_pass_restore(self, password):
        self.input_text(ResetPasswordPageLocators.PASS_RESTORE_INPUT, password)

    def click_restore(self):
        self.click(ResetPasswordPageLocators.RESTORE_BUTTON)

    def click_show_password(self):
        # self.wait_for_element(ResetPasswordPageLocators.SHOW_PASSWORD)
        self.click_with_wait(ResetPasswordPageLocators.SHOW_PASSWORD)

    def get_password_input(self):
        return self.element(ResetPasswordPageLocators.EMAIL_INPUT)

    def get_password_container_class(self):
        container = self.element(ResetPasswordPageLocators.PASSWORD_INPUT_CONTAINER)
        return container.get_attribute("type")

    def get_password_input_type(self):
        elem = self.element(ResetPasswordPageLocators.PASSWORD_INPUT_CONTAINER)
        return elem.get_attribute("type")


