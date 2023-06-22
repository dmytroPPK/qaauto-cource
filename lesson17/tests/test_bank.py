from services import Browsers
from services import BaseTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from random import randint


BROWSER = Browsers.Chrome.value
URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
fname, lname, post_code = f'Bob{randint(1,100)}', f'Bobrovych{randint(1,100)}', f'{randint(1,9)}' * 6


class TestBankingProject(BaseTest):

    def test_customer_login(self, get_driver):
        driver = get_driver(browser=BROWSER)
        driver.get(URL)

        customer_button = (By.XPATH, "//button[text() = 'Customer Login']")
        self.find_element(driver, customer_button).click()

        names_select = (By.ID, "userSelect")
        select = Select(self.find_element(driver,names_select))
        select.select_by_visible_text("Harry Potter")

        login_button = (By.XPATH, "//button[text() = 'Login']")
        self.find_element(driver,login_button).click()

        name_span = (By.CSS_SELECTOR, "strong > span.fontBig")
        customer_name = self.find_element(driver,name_span).text

        assert customer_name == "Harry Potter"


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

        alert = Alert(driver)
        alert.accept()

        customers_button = (By.XPATH, "//button[contains(text(), 'Customers')]")
        self.find_element(driver, customers_button).click()

        search_input = (By.XPATH, "//input[@placeholder='Search Customer']")
        self.find_element(driver, search_input).send_keys(fname)

        fname_td = (By.XPATH, "//table/tbody//td[1]")
        td_text = self.find_element(driver,fname_td).text

        assert td_text == fname
