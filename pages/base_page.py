from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        self.driver.get(url)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()
        # element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        # element.click()

    def input_text(self, locator, text):
        elem = self.wait.until(EC.visibility_of_element_located(locator))
        elem.clear()
        elem.send_keys(text)

    def is_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    # def click_with_time(self, locator):
    #     element = WebDriverWait(self.driver, 200).until(EC.element_to_be_clickable(locator))
    #     element.click()

    def click_with_wait(self, locator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        WebDriverWait(self.driver, 200).until(lambda d: element.is_enabled() and element.is_displayed())
        element.click()
    def wait_for_element(self, locator):
        # return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

        element = WebDriverWait(self.driver, 200).until(EC.visibility_of_element_located(locator))
        WebDriverWait(self.driver, 200).until(lambda d: element.is_enabled() and element.is_displayed())