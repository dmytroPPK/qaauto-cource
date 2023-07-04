import allure
from pages.alerts_frame_windows_page import AlertsPage


@allure.suite("Alerts Frame Windows")
class TestElements:
    @allure.feature('Test Alerts Page')
    class TestAlerts:
        @allure.title('check alert')
        def test_check_alert(self, driver):
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open()
            with allure.step('click on 1st button'):
                alerts_page.click_first_button()
            with allure.step('check alert text'):
                assert alerts_page.get_alert_text() == "You clicked a button"
