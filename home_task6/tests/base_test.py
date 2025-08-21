import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..")))

from home_task6.pages.inventory_page import InventoryPage
from home_task6.pages.login_page import LoginPage
from home_task6.pages.cart_page import CartPage
from home_task6.pages.checkout_info_page import CheckoutInfoPage
from home_task6.pages.checkout_overview_page import CheckoutOverviewPage


@pytest.mark.usefixtures("driver")
class BaseTest:
    @pytest.fixture(scope="class")
    def driver(self):
        options = Options()
        options.add_argument("--incognito")
        service = Service(r'c:\dist\chromedriver-win64\chromedriver.exe')
        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        yield driver
        driver.quit()

    @pytest.fixture(autouse=True)
    def inventory_page(self, driver):
        self.inventory_page = InventoryPage(driver)

    @pytest.fixture(autouse=True)
    def login_page(self, driver):
        self.login_page = LoginPage(driver)

    @pytest.fixture(autouse=True)
    def cart_page(self, driver):
        self.cart_page = CartPage(driver)

    @pytest.fixture(autouse=True)
    def checkout_info(self, driver):
        self.checkout_info = CheckoutInfoPage(driver)

    @pytest.fixture(autouse=True)
    def overview_page(self, driver):
        self.overview_page = CheckoutOverviewPage(driver)