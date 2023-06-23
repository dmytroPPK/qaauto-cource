from enum import Enum
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert


class Browsers(Enum):
    Chrome = 'chrome'
    FireFox = 'firefox'
    Chromium = 'chromium'
    Edge = 'edge'


class BaseTest:

    def find_element(self, driver, locator, timeout=10) -> WebElement | None:
        wait = Wait(driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, driver, locator, timeout=10) -> [WebElement]:
        wait = Wait(driver, timeout)
        return wait.until(EC.presence_of_all_elements_located(locator))

    def wait_page(self, driver, url, timeout=5):
        wait = Wait(driver, timeout)
        wait.until(EC.url_to_be(url))

    def find_select(self, driver, locator, timeout=10) -> Select:
        return Select(self.find_element(driver, locator, timeout))
    
    def alert(self, driver) -> Alert:
        return Alert(driver)
    
    
        


