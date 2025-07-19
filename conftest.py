import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import RegisterPage
from pages.main_page import MainPage
from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from data.data import URLs
from data.helpers import generate_name, generate_password, generate_email
import allure
import requests
def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="chrome or firefox")

@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    browser_name = request.param

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def get_credentials():
    name = generate_name()
    email = generate_email()
    password = generate_password()
    return name, email, password

@pytest.fixture
def registered_user_web(browser):
    name = generate_name()
    email = generate_email()
    password = generate_password()

    register_page = RegisterPage(browser)
    register_page.open(URLs.REGISTER_URL)

    register_page.register(name, email, password)

    return {
        "name": name,
        "email": email,
        "password": password
    }
@pytest.fixture(scope="function")
def registered_user():
    name = generate_name()
    email = generate_email()
    password = generate_password()

    # Регистрация
    res = requests.post(URLs.REGISTER_URL_API, json={
        "name": name,
        "email": email,
        "password": password
    })
    assert res.status_code == 200
    return {
        "name": name,
        "email": email,
        "password": password,
        "status_code": res.status_code
    }

@pytest.fixture
def get_numbers_in_feed(browser):
    main_page = MainPage(browser)
    feed_page = FeedPage(browser)
    main_page.open(URLs.BASE_URL)
    main_page.go_to_feed()
    feed_page.wait_feed_order()
    number_all_before = feed_page.get_total()
    number_day_before = feed_page.get_today()
    return {
        "total": number_all_before,
        "today": number_day_before
    }

@pytest.fixture
def authorized_order(browser, registered_user):
    email = registered_user["email"]
    password = registered_user["password"]
    main_page = MainPage(browser)
    login_page = LoginPage(browser)

    with allure.step("Открываем главную страницу"):
        main_page.open(URLs.BASE_URL)

    with allure.step("Перетаскиваем ингредиент"):
        main_page.drag_ingredient_to_constructor()

    with allure.step("Входим в аккаунт"):
        main_page.login_for_order()
        login_page.login(email, password)
        login_page.wait_for_url_change(URLs.BASE_URL)
        current_url = browser.current_url

    with allure.step("Создаем заказ"):
        main_page.create_order()

    with allure.step("Получаем номер заказа"):
        order_number = main_page.get_order_number()


    return {
        "order_number": order_number,
        "main_page": main_page,
        "user": registered_user,
    }