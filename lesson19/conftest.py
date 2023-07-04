import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
import allure
from datetime import datetime


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Specify the browser (chrome, firefox, edge, chromium)")

@pytest.fixture
def chrome_driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def ff_driver():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def edge_driver():
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def chromium_driver():
    driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")

    if browser == 'chrome':
        return request.getfixturevalue('chrome_driver')
    elif browser == 'firefox':
        return request.getfixturevalue('ff_driver')
    elif browser == 'edge':
        return request.getfixturevalue('edge_driver')
    elif browser == 'chromium':
        return request.getfixturevalue('chromium_driver')
    else:
        raise ValueError(f"Unsupported browser typing via --browser option or --browser option in pytest.ini")
