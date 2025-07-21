import allure
from pages.login_page import LoginPage
from pages.reset_password_page import ResetPasswordPage
from data.data import TestData, URLs

@allure.title("Восстановление пароля")
class TestPassword:
    @allure.story("Переход на страницу восстановления пароля и проверка функционала")
    def test_password_reset_flow(self, browser):
        with allure.step("Открываем страницу входа"):
            login = LoginPage(browser)
            login.open(URLs.LOGIN_URL)

        with allure.step("Переходим на страницу восстановления пароля"):
            login.click_reset_password()

        with allure.step("Вводим e-mail и отправляем форму восстановления"):
            reset = ResetPasswordPage(browser)
            reset.input_email(TestData.TEST_EMAIL)
            reset.click_restore()

        with allure.step("Проверка кнопки показать/скрыть пароль меняет тип поля"):
            type_before = reset.get_password_input_type()
            reset.input_pass_restore(TestData.TEST_PASS)
            reset.click_show_password()
            type_after = reset.get_password_input_type()
            assert type_before != type_after, f"Тип поля не изменился после клика: был {type_before}, стал {type_after}"


