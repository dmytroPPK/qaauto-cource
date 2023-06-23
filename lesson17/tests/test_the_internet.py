from services import Browsers
from services import BaseTest
from selenium.webdriver.common.by import By
import allure


BROWSER = Browsers.Chrome.value
URL = "http://the-internet.herokuapp.com/"


@allure.story('Some impovements of TheInternet project')
@allure.suite('TheInternet')
class TestTheInternet(BaseTest):


    @allure.severity(severity_level=allure.severity_level.BLOCKER)
    @allure.description('Validating GitHub link')
    @allure.title('GitHub link')
    def test_check_github_link(self, get_driver):
        driver = get_driver(browser=BROWSER)
        driver.get(URL)

        github_img = (By.XPATH, "/html/body/div[2]/a/img")
        self.find_element(driver, github_img).click()

        with allure.step('Validating link'):
            assert driver.current_url == 'https://github.com/saucelabs/the-internet'


    @allure.severity(allure.severity_level.NORMAL)
    @allure.title('AB testing')
    @allure.description('Check url of page')
    def test_check_abtesting_link(self, get_driver):
        driver = get_driver(browser=BROWSER)
        driver.get(URL)

        ab_link = (By.LINK_TEXT, "A/B Testing")
        self.find_element(driver, ab_link).click()

        assert driver.current_url == "http://the-internet.herokuapp.com/abtest"


