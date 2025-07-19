from locators import PersonalAccountLocators
from pages.base_page import BasePage

class AccountPage(BasePage):
    def open_account(self):
        self.click(PersonalAccountLocators.PROFILE_LINK)

    def go_to_history(self):
        self.click(PersonalAccountLocators.ORDER_HISTORY_TAB)

    def logout(self):
        self.wait_page_loaded(PersonalAccountLocators.LOGOUT_BUTTON)
        self.click_with_wait(PersonalAccountLocators.LOGOUT_BUTTON)

