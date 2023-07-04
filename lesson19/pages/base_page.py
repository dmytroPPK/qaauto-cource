import allure
# from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    TIMEOUT = 10

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    @allure.step('Open a browser')
    def open(self):
        self.driver.get(self.url)

    def find_element(self, locator):
        return self._wait().until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return self._wait().until(EC.presence_of_all_elements_located(locator))

    def find_and_scroll(self, locator):
        element = self._wait().until(EC.presence_of_element_located(locator))
        self._scroll_to_element(element)
        return element


    def _scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def _wait(self, timeout=TIMEOUT):
        return Wait(self.driver, timeout)

