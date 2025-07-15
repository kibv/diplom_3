import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="chrome or firefox")

# @pytest.fixture(scope="function")
# def browser(request):
#     browser_name = request.config.getoption("browser_name")
#     if browser_name == "chrome":
#         driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#         # driver.maximize_window()
#     elif browser_name == "firefox":
#         driver = webdriver.Firefox()
#     else:
#         raise ValueError("Unsupported browser: {}".format(browser_name))
#     # driver.maximize_window()
#     yield driver
#     driver.quit()

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

