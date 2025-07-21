from locators import FeedPageLocators
from pages.base_page import BasePage


class FeedPage(BasePage):
    def open_order_details(self):
        self.click(FeedPageLocators.FEED_ORDERS)

    def wait_feed_order(self):
        self.wait_for_overlay(FeedPageLocators.FEED_ORDERS)

    def get_total(self):
        self.wait_for_overlay(FeedPageLocators.TOTAL_DONE)
        return self.get_text(FeedPageLocators.TOTAL_DONE)

    def get_today(self):
        self.wait_for_overlay(FeedPageLocators.TOTAL_TODAY)
        return self.get_text(FeedPageLocators.TOTAL_TODAY)

    def get_counter_text_total(self):
        return self.get_text(FeedPageLocators.TOTAL_DONE)

    def get_counter_text_today(self):
        return self.get_text(FeedPageLocators.TOTAL_TODAY)

    def check_order_in_feed(self, order_number, param):
        locator = getattr(FeedPageLocators, f'{param}_FEED_NUMBERS')
        self.wait_for_overlay(locator)
        self.wait.until(lambda driver: any(
            el.text.strip() != "" and el.text.strip() != "Все текущие заказы готовы!"
            for el in driver.find_elements(*locator)))

        order_elements = self.driver.find_elements(*locator)
        order_numbers = [elem.text.strip() for elem in order_elements]

        for feed_number in order_numbers:
            normalized_feed_number = feed_number.lstrip('#0')
            if order_number == normalized_feed_number:
                print(f"Found order number {order_number} in feed as {feed_number}")
                return True
        return False
