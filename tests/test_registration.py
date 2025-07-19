import allure
from pages.login_page import LoginPage
from pages.login_page import RegisterPage
from pages.main_page import MainPage
from data.data import URLs

@allure.feature("Личный кабинет")
class TestAccount:
    @allure.story("Проверка регистрации")
    def test_account_registration(self, browser, get_credentials):
        name, email, password = get_credentials
        register_page = RegisterPage(browser)
        main_page = MainPage(browser)
        login_page = LoginPage(browser)

        with allure.step("Открываем главную страницу и переходим к регистрации"):
            main_page.open(URLs.BASE_URL)
            main_page.go_to_personal_account()
            login_page.new_registrathion()
            current_url = browser.current_url
            assert current_url == URLs.REGISTER_URL, f"Открыт неверный URL: {current_url}"

        with allure.step("Регистрируем нового пользователя"):
            register_page.register(name, email, password)

        with allure.step("Переходим на страницу входа и логинимся"):
            login_page.wait_url(URLs.LOGIN_URL)
            login_page.login(email, password)
            login_page.wait_url(URLs.BASE_URL)
            current_url = browser.current_url
            assert current_url == URLs.BASE_URL, f"Открыт неверный URL: {current_url}"
