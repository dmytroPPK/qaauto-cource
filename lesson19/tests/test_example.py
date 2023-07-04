import time

from pages.base_page import BasePage

from selenium.webdriver.common.by import By



def no_test_1(driver):
    page = BasePage(driver, "https://demoqa.com/text-box")
    page.open()
    time.sleep(5)
    permanent_address = (By.ID, "permanentAddress")
    # page.element_is_visible(permanent_address)
    page.find_element(permanent_address).send_keys("hello world")
    time.sleep(5)

