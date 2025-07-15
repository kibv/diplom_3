from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
    CONSTRUCTOR_HEADER = (By.XPATH, "//h1[text()='Соберите бургер']")
    ACCOUNT_BUTTON = (By.XPATH, "//a[@href='/account']")
    FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]//a")

class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]")
    LOGIN_HEADER = (By.XPATH, "//h2[text()='Вход']")
    RESET_PASSWORD_LINK = (By.LINK_TEXT, "Восстановить пароль")

class RegistrationPageLocators:
    NAME_FIELD = (By.XPATH, "//fieldset[1]//input")
    EMAIL_FIELD = (By.XPATH, "//fieldset[2]//input")
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    PASSWORD_ERROR = (By.XPATH, "//p[contains(@class, 'input__error')]")
    LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]")

class PersonalAccountLocators:
    PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")
    ORDER_HISTORY_TAB = (By.XPATH, "//a[contains(text(),'История заказов')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    RECOVERY_LINK = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]")

class ConstructorPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']/..")
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']/..")
    FILLINGS_SECTION = (By.XPATH, "//span[text()='Начинки']/..")
    ACTIVE_SECTION = (By.CSS_SELECTOR, ".tab_tab_type_current")
    INGREDIENT = (By.CSS_SELECTOR, ".burger-ingredient")
    INGREDIENT_NAME = (By.CSS_SELECTOR, ".burger-ingredient span")
    COUNTER = (By.CSS_SELECTOR, ".counter")
    MODAL = (By.CSS_SELECTOR, ".Modal_modal__content__")
    CLOSE_MODAL_BUTTON = (By.XPATH, "//button[contains(@class,'modal__close')]")

class FeedPageLocators:
    FEED_ORDERS = (By.CSS_SELECTOR, ".OrderFeed_order__list__item")
    ORDER_CARD = (By.CSS_SELECTOR, ".OrderFeed_order__list__item")
    ORDER_DETAILS_MODAL = (By.CSS_SELECTOR, ".Modal_modal__content__")
    CLOSE_MODAL_BUTTON = (By.XPATH, "//button[contains(@class,'modal__close')]")
    TOTAL_DONE = (By.XPATH, "//p[text()='Выполнено за всё время']/following-sibling::p")
    TOTAL_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня']/following-sibling::p")
    IN_PROGRESS = (By.XPATH, "//h2[text()='В работе']")

# class ResetPasswordPageLocators:
#     EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
#     PASS_RESTORE_INPUT = (By.XPATH, "//input[@name='Введите новый пароль']")
#     RESTORE_BUTTON = (By.XPATH, "//button[contains(text(), 'Восстановить')]")
#     SHOW_PASSWORD_TOGGLE = (By.CSS_SELECTOR, "div.input__icon.input__icon-action")
#     PASSWORD_INPUT_CONTAINER = (By.XPATH, "//div[contains(@class,'input') and .//input[@name='name']]")

class ResetPasswordPageLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASS_RESTORE_INPUT = (By.XPATH, "//input[@name='Введите новый пароль']")
    RESTORE_BUTTON = (By.XPATH, "//button[contains(text(), 'Восстановить')]")
    SHOW_PASSWORD = (By.CSS_SELECTOR, "div.input__icon.input__icon-action")
    PASSWORD_INPUT_CONTAINER = (By.XPATH, "//input[@name='Введите новый пароль']")
