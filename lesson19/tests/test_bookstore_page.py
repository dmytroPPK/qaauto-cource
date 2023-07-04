import allure
from pages.bookstore_page import LoginPage


@allure.suite("Book Store Application")
class TestBookStore:
    @allure.feature('Negative Test Login Page')
    class TestLoginNegative:
        @allure.title('empty fields')
        def test_check_empty_fields(self, driver):
            login_page = LoginPage(driver, "https://demoqa.com/login")
            login_page.open()
            with allure.step('click on login button'):
                login_page.click_login_button()
            with allure.step('check added validation class'):
                name_class, password_class = login_page.get_inputs_class()
                assert "is-invalid" in name_class
                assert "is-invalid" in password_class

