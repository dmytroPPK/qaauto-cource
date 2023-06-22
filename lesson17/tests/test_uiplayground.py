from services import Browsers
from services import BaseTest
from selenium.webdriver.common.by import By


BROWSER = Browsers.Chrome.value
URL = "http://uitestingplayground.com/home"


class TestUIPlayground(BaseTest):

    def test_check_count_overview_links(self, get_driver):
        driver = get_driver(browser=BROWSER)
        driver.get(URL)

        overview_links = (By.XPATH, "//section[@id='overview']//a")
        assert len(self.find_elements(driver, overview_links)) == 18

    def test_check_w3c_resource(self, get_driver):
        driver = get_driver(browser=BROWSER)
        driver.get(URL)

        resource_link = (By.CSS_SELECTOR, "a[href='/resources']")
        self.find_element(driver, resource_link).click()

        w3c_link = (By.LINK_TEXT, "W3C")
        self.find_element(driver, w3c_link).click()

        assert driver.current_url == "https://www.w3.org/"
