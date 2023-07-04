from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TexBoxPage(BasePage):

    def fill_all_fields(self, form_data: dict):
        self.find_element(self.Locators.FULL_NAME).send_keys(form_data.get("user_name"))
        self.find_element(self.Locators.USER_EMAIL).send_keys(form_data.get("user_email"))
        self.find_element(self.Locators.CURRENT_ADDR).send_keys(form_data.get("current_addr"))
        self.find_element(self.Locators.PERMANENT_ADDR).send_keys(form_data.get("permanent_addr"))

    def click_on_submit(self):
        self.find_and_scroll(self.Locators.SUBMIT_BUTTON).click()

    def get_created_fields(self):
        paragraphs = self.find_elements(self.Locators.CREATED_FIELDS)
        user_name = paragraphs[0].text.split(':')[-1]
        user_email = paragraphs[1].text.split(':')[-1]
        current_addr = paragraphs[2].text.split(':')[-1]
        permanent_addr = paragraphs[3].text.split(':')[-1]

        return dict(
            user_name=user_name,
            user_email=user_email,
            current_addr=current_addr,
            permanent_addr=permanent_addr
        )



    class Locators:
        FULL_NAME = (By.ID, "userName")
        USER_EMAIL = (By.ID, "userEmail")
        CURRENT_ADDR = (By.ID, "currentAddress")
        PERMANENT_ADDR = (By.ID, "permanentAddress")
        SUBMIT_BUTTON = (By.CSS_SELECTOR, "button#submit")
        CREATED_FIELDS = (By.CSS_SELECTOR, "div#output p")


class ButtonsPage(BasePage):

    def click_on_button(self):
        self.find_element(self.Locators.LCLICK_BUTTON).click()

    def get_msg_shown(self):
        return self.find_element(self.Locators.LCLICK_MSG).text

    class Locators:
        LCLICK_BUTTON = (By.XPATH, "//button[text()='Click Me']")
        LCLICK_MSG = (By.CSS_SELECTOR, "p#dynamicClickMessage")
