import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AlertsPage(BasePage):

    def click_first_button(self):
        self.find_and_scroll(self.Locators.ALERT_BUTTON).click()

    def get_alert_text(self):
        alert = self.driver.switch_to.alert
        time.sleep(1)
        text = alert.text
        alert.accept()
        return text

    class Locators:
        ALERT_BUTTON = (By.CSS_SELECTOR, "button#alertButton")
