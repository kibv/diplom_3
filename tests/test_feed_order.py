import allure
from pages.feed_page import FeedPage
from pages.main_page import MainPage
from data.data import URLs

@allure.title("Лента заказов")
class TestFeed:
    @allure.story("Открытие деталей заказа")
    def test_order_modal_opens(self, browser, registered_user):
        main = MainPage(browser)
        feed_order = FeedPage(browser)
        main.open(URLs.BASE_URL)
        assert registered_user["status_code"] == 200

        with allure.step("Открываем страницу ленты заказов"):
            main.go_to_feed()

        with allure.step("Ожидаем список заказов и кликаем первый"):
            feed_order.wait_feed_order()
            feed_order.open_order_details()

        with allure.step("Проверяем, что открылось всплывающее окно с деталями"):
            assert main.is_visible_container(), "Модальное окно не появилось"


    @allure.story("Оформление заказа с авторизацией")
    def test_create_oder(self, browser, get_numbers_in_feed, authorized_order):
        order_number = authorized_order["order_number"]
        main_page = authorized_order["main_page"]
        number_all_before = get_numbers_in_feed['total']
        number_day_before = get_numbers_in_feed['today']
        feed_page = FeedPage(browser)

        with allure.step("Проверка заказа в ленте"):
            main_page.open(URLs.BASE_URL)
            main_page.go_to_feed()
            assert feed_page.check_order_in_feed(order_number, 'ORDER'), f'Заказ № {order_number} не найден'

        with allure.step("Проверка заказа в работе"):
            assert feed_page.check_order_in_feed(order_number, 'IN_PROGRESS'), f'Заказ № {order_number} в работе не найден'

        with allure.step("Проверка общего счетчика в ленте"):
            after = feed_page.get_total()
            assert int(after) == int(number_all_before) + 1, f"Счетчик не увеличился: было {number_all_before}, стало {after}"

        with allure.step("Проверка счетчика за сегодня в ленте"):
            after = feed_page.get_today()
            assert int(after) == int(number_day_before) + 1, f"Счетчик не увеличился: было {number_day_before}, стало {after}"
