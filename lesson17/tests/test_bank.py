from services import Browsers
from services import BaseTest
from selenium.webdriver.common.by import By
from random import randint
import allure



BROWSER = Browsers.Chrome.value
URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
fname, lname, post_code = f'Bob{randint(1,100)}', f'Bobrovych{randint(1,100)}', f'{randint(1,9)}' * 6

@allure.story('Regression testing of Banking Project')
@allure.suite('Bank Project')
class TestBankingProject(BaseTest):

    @allure.description('Login customer via our service')
    @allure.title("Login customer")
    @allure.severity(severity_level=allure.severity_level.CRITICAL)
    def test_customer_login(self, get_driver):
        driver = get_driver(browser=BROWSER)
        driver.get(URL)

        customer_button = (By.XPATH, "//button[text() = 'Customer Login']")
        self.find_element(driver, customer_button).click()

        names_select = (By.ID, "userSelect")
        self.find_select(driver, names_select).select_by_visible_text("Harry Potter")
        

        login_button = (By.XPATH, "//button[text() = 'Login']")
        self.find_element(driver,login_button).click()

        name_span = (By.CSS_SELECTOR, "strong > span.fontBig")
        customer_name = self.find_element(driver,name_span).text

        with allure.step("Validating customer name"):
            assert customer_name == "Harry Potter"


    @allure.severity(severity_level=allure.severity_level.CRITICAL)
    @allure.description('Add customer to db and check it in list via search field')
    @allure.title('Add customer')
    def test_add_customer(self, get_driver):
        driver = get_driver(browser=BROWSER)
        driver.get(URL)

        manager_button = (By.XPATH, "//button[text() = 'Bank Manager Login']")
        self.find_element(driver, manager_button).click()

        add_customer_button = (By.XPATH, "//button[contains(text(), 'Add')]")
        self.find_element(driver, add_customer_button).click()

        fname_input = (By.XPATH, "//input[@placeholder='First Name']")
        lname_input = (By.XPATH, "//input[@placeholder='Last Name']")
        post_code_input = (By.XPATH, "//input[@placeholder='Post Code']")
        self.find_element(driver,fname_input).send_keys(fname)
        self.find_element(driver,lname_input).send_keys(lname)
        self.find_element(driver, post_code_input).send_keys(post_code)

        submit_button = (By.XPATH, "//button[@type='submit' and text()='Add Customer']")
        self.find_element(driver,submit_button).click()

        self.alert(driver).accept()

        customers_button = (By.XPATH, "//button[contains(text(), 'Customers')]")
        self.find_element(driver, customers_button).click()

        search_input = (By.XPATH, "//input[@placeholder='Search Customer']")
        self.find_element(driver, search_input).send_keys(fname)

        fname_td = (By.XPATH, "//table/tbody//td[1]")
        td_text = self.find_element(driver,fname_td).text

        with allure.step("Customer name is in a list"):
            assert td_text == fname
