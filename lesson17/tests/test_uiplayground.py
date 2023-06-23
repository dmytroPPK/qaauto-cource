from services import Browsers
from services import BaseTest
from selenium.webdriver.common.by import By
import allure


BROWSER = Browsers.Chrome.value
URL = "http://uitestingplayground.com/home"


@allure.suite('UI Playground')
@allure.story('Sanity test of UI Playground')
class TestUIPlayground(BaseTest):

    
    @allure.severity(severity_level=allure.severity_level.MINOR)
    @allure.description('Validating section count on page')
    def test_check_count_overview_links(self, get_driver):
        driver = get_driver(browser=BROWSER)
        driver.get(URL)

        overview_links = (By.XPATH, "//section[@id='overview']//a")
        with allure.step('Check count'):
            assert len(self.find_elements(driver, overview_links)) == 18

    
    @allure.title('W3C resource')
    @allure.severity(severity_level=allure.severity_level.CRITICAL)
    @allure.description('Check w3c link')
    def test_check_w3c_resource(self, get_driver):
        driver = get_driver(browser=BROWSER)
        driver.get(URL)

        resource_link = (By.CSS_SELECTOR, "a[href='/resources']")
        self.find_element(driver, resource_link).click()

        w3c_link = (By.LINK_TEXT, "W3C")
        self.find_element(driver, w3c_link).click()

        with allure.step('Validating url'):
            assert driver.current_url == "https://www.w3.org/"
