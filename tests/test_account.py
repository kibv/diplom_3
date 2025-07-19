import allure
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from pages.main_page import MainPage
from data.data import URLs

@allure.feature("Личный кабинет")
class TestAccount:
    def test_account_register(self, browser, registered_user):
        email = registered_user["email"]
        password = registered_user["password"]
        assert registered_user["status_code"] == 200

        with allure.step("Переходим в аккаунт"):
            main_page = MainPage(browser)
            login_page = LoginPage(browser)
            account_page = AccountPage(browser)
            main_page.open(URLs.BASE_URL)
            main_page.go_to_personal_account()
            login_page.wait_url(URLs.LOGIN_URL)
            current_url = browser.current_url
            assert current_url == URLs.LOGIN_URL, f"Открыт неверный URL: {current_url}"

        with allure.step("Логинимся"):
            login_page.login(email, password)
            login_page.wait_url(URLs.BASE_URL)
            current_url = browser.current_url
            assert current_url == URLs.BASE_URL, f"Открыт неверный URL: {current_url}"

        with allure.step("Переходим в ленту заказов"):
            main_page.go_to_feed()
            login_page.wait_url(URLs.FEED_URL)
            current_url = browser.current_url
            assert current_url == URLs.FEED_URL, f"Открыт неверный URL: {current_url}"

        with allure.step("Переходим в аккаунт для выхода"):
            main_page.go_to_personal_account()
            login_page.wait_url(URLs.ACCOUNT_URL)
            current_url = browser.current_url
            assert current_url == URLs.ACCOUNT_URL, f"Открыт неверный URL: {current_url}"
            account_page.logout()
            login_page.wait_url(URLs.LOGIN_URL)
            current_url = browser.current_url
            assert current_url == URLs.LOGIN_URL, f"Открыт неверный URL: {current_url}"
