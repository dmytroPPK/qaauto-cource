from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    def click_login_button(self):
        self.find_and_scroll(self.Locators.LOGIN_BUTTON).click()

    def get_inputs_class(self):
        inputs = self.find_elements(self.Locators.FORM_INPUTS)
        return inputs[0].get_attribute('class'), inputs[1].get_attribute('class')



    class Locators:
        USER_NAME = (By.ID, "userName")
        PASSWORD = (By.ID, "password")
        LOGIN_BUTTON = (By.CSS_SELECTOR, "button#login")
        FORM_INPUTS = (By.CSS_SELECTOR, "form#userForm input")
