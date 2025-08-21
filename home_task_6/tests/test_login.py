import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from home_task_6.pages.login_page import LoginPage

@pytest.mark.usefixtures("driver")
class TestLogin:
    @pytest.fixture(scope="class")
    def driver(self):
       driver = webdriver.Chrome()
       driver.get("https://www.saucedemo.com/")
       yield driver
       driver.quit()

    @pytest.fixture(autouse=True)
    def setup_login_page(self, driver):
        self.login_page = LoginPage(driver)

    def test_successful_login(self):
        self.login_page.enter_username("standard_user")
        self.login_page.enter_password("secret_sauce")
        self.login_page.click_on_login_button()
        assert "inventory.html" in self.login_page.driver.current_url

    def test_invalid_password(self):
        self.login_page.enter_username("standard_user")
        self.login_page.enter_password("wrong_password")
        self.login_page.click_on_login_button()
        assert "Username and password do not match" in self.login_page.error_message().text, "Неверное сообщение об ошибке."

    def test_locked_out_user(self):
        self.login_page.enter_username("locked_out_user")
        self.login_page.enter_password("secret_sauce")
        self.login_page.click_on_login_button()
        assert "Sorry, this user has been locked out." in self.login_page.error_message().text, "Неверное сообщение об ошибке."

    def test_empty_username(self):
        self.login_page.enter_password("secret_sauce")
        self.login_page.click_on_login_button()
        assert "Username is required"
