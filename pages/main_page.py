from locators import MainPageLocators
from pages.base_page import BasePage


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
        self.click(MainPageLocators.INGREDIENT)

    def close_modal(self):
        self.click(MainPageLocators.CLOSE_MODAL_BUTTON)

    def is_visible_container(self):
        return self.is_visible(MainPageLocators.MODAL_CONTAINER)

    def get_order_number(self):
        self.wait_page_loaded(MainPageLocators.LOADING_ANIMATION)
        element = self.wait_el(MainPageLocators.ORDER_NUMBER)
        self.wait.until(lambda driver: element.text.strip() != "" and element.text != "9999")
        return element.text

    def drag_ingredient_to_constructor(self):
        self.drag_and_drop_js(MainPageLocators.INGREDIENT, MainPageLocators.CONSTRUCTOR_AREA)
        self.drag_and_drop_js(MainPageLocators.INGREDIENT_1, MainPageLocators.CONSTRUCTOR_AREA)

    def get_ingredient_counter(self):
        text = self.get_text_or_default(MainPageLocators.INGREDIENT_COUNTER, default="0")
        return int(text)
