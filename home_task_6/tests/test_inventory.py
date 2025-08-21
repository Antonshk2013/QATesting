import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from ..pages.inventory_page import InventoryPage
from ..pages.login_page import LoginPage
from ..pages.cart_page import CartPage


from home_task_6.tests.test_login import TestLogin


class TestInventory:
    @pytest.fixture()
    def driver(self):
       driver = webdriver.Chrome()
       driver.get("https://www.saucedemo.com/")
       yield driver
       driver.quit()

    @pytest.fixture()
    def inventory_page(self, driver):
       return InventoryPage(driver)

    @pytest.fixture()
    def login_page(self, driver):
       return LoginPage(driver)

    @pytest.fixture()
    def card_page(self, driver):
        return CartPage(driver)

    @pytest.fixture()
    def test_login(self, driver):
        return TestLogin(driver)

    def test_items_amount(self, inventory_page, login_page):
       login_page.success_login("standard_user", "secret_sauce")
       assert inventory_page.get_items_amount() == 6, "Количество товаров не совпадает."

    def test_all_items_are_displayed(self, inventory_page, login_page):
       login_page.success_login("standard_user", "secret_sauce")
       assert inventory_page.all_items_are_displayed(), "Не все товары отображаются."

    def test_all_items_names_are_displayed(self, inventory_page, login_page):
       login_page.success_login("standard_user", "secret_sauce")
       assert inventory_page.all_items_names_are_displayed(), "Не все названия товаров отображаются."

    def test_all_item_names_are_not_empty(self, inventory_page, login_page):
       login_page.success_login("standard_user", "secret_sauce")
       assert inventory_page.all_item_names_are_not_empty(), "Есть товары с пустыми названиями."

    def test_all_item_names_contains_sauce_labs(self, inventory_page, login_page):
       login_page.success_login("standard_user", "secret_sauce")
       assert inventory_page.all_item_names_contains_sauce_labs(), "Не все товары начинаются с 'Sauce Labs'."

    def test_compare_prices(self, inventory_page, login_page, card_page, test_login):
        test_login.test_successful_login()


