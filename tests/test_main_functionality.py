import allure
from pages.feed_page import FeedPage
from pages.main_page import MainPage
from data.data import URLs
@allure.story("Проверка основного функционала")
class TestMain:
    @allure.feature("Переход в конструктор")
    def test_go_to_constructor(self, browser):
        main_page = MainPage(browser)

        with allure.step("Открываем страницу заказов"):
            browser.get(URLs.FEED_URL)

        with allure.step("Кликаем на кнопку 'Конструктор'"):
            main_page.go_to_constructor()

        with allure.step("Проверяем, что URL изменился на конструктор"):
            assert browser.current_url == URLs.BASE_URL, "Не открылась страница конструктора"

    @allure.feature("Переход в лента заказов")
    def test_go_to_feed(self, browser):
        main_page = MainPage(browser)

        with allure.step("Открываем главную страницу"):
            main_page.open(URLs.BASE_URL)

        with allure.step("Кликаем на кнопку 'Лента заказов'"):
            main_page.go_to_feed()

        with allure.step("Проверяем, что URL изменился на Ленту заказов"):
            assert browser.current_url == URLs.FEED_URL, "Не открылась Лента заказов"

    @allure.feature("Модальное окно ингредиента")
    def test_ingredient_modal_close(self, browser):
        main_page = MainPage(browser)
        modal = FeedPage(browser)

        with allure.step("Открываем главную страницу"):
            main_page.open(URLs.BASE_URL)

        with allure.step("Открываем ингредиент"):
            main_page.click_ingredient()

        with allure.step("Закрываем модальное окно"):
            main_page.close_modal()

        with allure.step("Проверяем, что модальное окно закрылось"):
            modal.is_visible_container(), "Модальное окно не закрылось"
    @allure.feature("Конструктор")
    def test_ingredient_counter_increases(self, browser):
        page = MainPage(browser)

        with allure.step("Открываем главную страницу"):
            page.open(URLs.BASE_URL)

        with allure.step("Считываем текущий счетчик"):
            before = page.get_ingredient_counter()

        with allure.step("Перетаскиваем ингредиент"):
            page.drag_ingredient_to_constructor()

        with (allure.step("Проверяем, что счетчик увеличился")):
            after = page.get_ingredient_counter()
            assert after == before + 1, f"Счетчик не увеличился: было {before}, стало {after}"

    @allure.feature("Оформление заказа с авторизацией")
    def test_create_oder(self, browser, get_numbers_in_feed, authorized_order):
        order_number = authorized_order["order_number"]
        main_page = authorized_order["main_page"]
        feed_page = FeedPage(browser)

        with allure.step("Проверка заказа в ленте"):
            main_page.open(URLs.BASE_URL)
            main_page.go_to_feed()
            assert feed_page.check_order_in_feed(order_number, 'ORDER'), f'Заказ № {order_number} не найден'



