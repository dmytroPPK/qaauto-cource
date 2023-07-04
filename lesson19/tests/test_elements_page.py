import allure
from pages.elements_page import TexBoxPage, ButtonsPage


@allure.suite("Elements")
class TestElements:
    @allure.feature('Test TextBox Page')
    class TestTextBox:
        @allure.title('fill all fields')
        def test_fill_fields(self, driver):
            form_data = {
                "user_name": "John Beaver",
                "user_email": "j.beaver@gmail.com",
                "current_addr": "malibu 153",
                "permanent_addr": "monako 147"
            }
            with allure.step('fill all fields'):
                text_box_page = TexBoxPage(driver, "https://demoqa.com/text-box")
                text_box_page.open()
                text_box_page.fill_all_fields(form_data)

            with allure.step('click on submit button'):
                text_box_page.click_on_submit()

            with allure.step('check created fields'):
                name, email, current_addr, permanent_addr = text_box_page.get_created_fields().values()

                assert name == form_data.get("user_name")
                assert email == form_data.get("user_email")
                assert current_addr == form_data.get("current_addr")
                assert permanent_addr == form_data.get("permanent_addr")

    @allure.feature('Test Buttons Page')
    class TestButtons:
        @allure.title('left button click')
        def test_left_click(self, driver):
            buttons_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            buttons_page.open()
            with allure.step('left click on button'):
                buttons_page.click_on_button()
            with allure.step('check msg shown'):
                msg = buttons_page.get_msg_shown()
                assert msg == "You have done a dynamic click"






