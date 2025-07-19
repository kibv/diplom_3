import time

from locators import MainPageLocators, ConstructorPageLocators, FeedPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):

    def go_to_personal_account(self):
        self.click(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    def login_for_order(self):
        self.click_with_wait(MainPageLocators.LOGIN_BUTTON)
    def create_order(self):
        self.click_with_wait(MainPageLocators.CREATE_ORDER_BUTTON)

    def go_to_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)

    def go_to_feed(self):
        self.click_with_wait(MainPageLocators.FEED_BUTTON)

    def click_ingredient(self):
        self.click(ConstructorPageLocators.INGREDIENT)

    def close_modal(self):
        self.click(ConstructorPageLocators.CLOSE_MODAL_BUTTON)

    def get_counter_text_total(self):
        return self.get_text(FeedPageLocators.TOTAL_DONE)

    def get_counter_text_today(self):
        return self.get_text(FeedPageLocators.TOTAL_TODAY)

    def get_order_number(self):
        self.wait_page_loaded(MainPageLocators.LOADING_ANIMATION)
        element = self.wait.until(EC.presence_of_element_located(MainPageLocators.ORDER_NUMBER))
        self.wait.until(lambda driver: element.text.strip() != "" and element.text != "9999")
        return element.text

    def drag_ingredient_to_constructor(self):
        self.drag_and_drop_js(ConstructorPageLocators.INGREDIENT, ConstructorPageLocators.CONSTRUCTOR_AREA)
        self.drag_and_drop_js(ConstructorPageLocators.INGREDIENT_1, ConstructorPageLocators.CONSTRUCTOR_AREA)

    def get_ingredient_counter(self):
        text = self.get_text_or_default(ConstructorPageLocators.INGREDIENT_COUNTER, default="0")
        return int(text)
