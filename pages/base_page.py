from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        self.driver.get(url)

    def wait_page_loaded(self, element_locator, timeout=30):
        wait = WebDriverWait(self.driver, timeout)
        try:
            wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
            wait.until(EC.visibility_of_element_located(element_locator))

        except TimeoutException as e:
            raise TimeoutException(
                f"Страница не загрузилась за {timeout} секунд. "
                f"Локатор: {element_locator}. Ошибка: {str(e)}"
            )

    def wait_for_url_change(self, url):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.url_to_be(url))

    def click(self, locator):
        self.wait_page_loaded(locator)
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def input_text(self, locator, text):
        elem = self.wait.until(EC.visibility_of_element_located(locator))
        elem.clear()
        elem.send_keys(text)

    def is_visible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_with_wait(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

            self.driver.execute_script("arguments[0].click();", element)
        except Exception as e:
            raise Exception(f"Элемент не был найден или кликабелен: {e}")

    def wait_for_url(self, expected_url, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_to_be(expected_url))

    def check_current_url(self, expected_url):
        actual = self.driver.current_url
        assert actual.startswith(expected_url), f"Открыт неверный URL:\nожидали: {expected_url}\nфактически: {actual}"

    def scroll_to_element(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        element.click()

    def get_text_or_default(self, locator, default="0"):
        try:
            elem = self.driver.find_element(*locator)
            return elem.text
        except:
            return default

    def drag_and_drop_js(self, source_locator, target_locator):
        source = self.wait.until(EC.visibility_of_element_located(source_locator))
        target = self.wait.until(EC.visibility_of_element_located(target_locator))
        script = """
        function simulateDragDrop(sourceNode, targetNode) {
            var event = new MouseEvent('dragstart', { bubbles: true });
            sourceNode.dispatchEvent(event);
            event = new MouseEvent('dragover', { bubbles: true });
            targetNode.dispatchEvent(event);
            event = new MouseEvent('drop', { bubbles: true });
            targetNode.dispatchEvent(event);
        }
        simulateDragDrop(arguments[0], arguments[1]);
        """
        self.driver.execute_script(script, source, target)

    def wait_for_overlay(self, locator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(locator))

    def wait_for_real_order_number(self, locator, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until_not(
            lambda driver: driver.find_element(*locator).text == text
        )

