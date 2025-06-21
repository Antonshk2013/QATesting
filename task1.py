from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import pytest
import os


current_dir = os.path.dirname(os.path.abspath(__file__))

@pytest.fixture
def driver():
    service = Service(current_dir+"/chromedriver-linux64/chromedriver")
    options = Options()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


def test_success_path(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    user = "tomsmith"
    password = "SuperSecretPassword!"
    driver.find_element(By.ID, "username").send_keys(user)
    driver.find_element(By.ID, "password").send_keys(password)
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    success_message = "You logged into a secure area!"
    message_box = driver.find_element(By.ID, "flash")
    assert success_message in message_box.text
    assert "https://the-internet.herokuapp.com/secure" == driver.current_url


def test_incorrect_username(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    user = "tomsmith2"
    password = "SuperSecretPassword!"
    driver.find_element(By.ID, "username").send_keys(user)
    driver.find_element(By.ID, "password").send_keys(password)
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    unsuccessful_message = "Your username is invalid!"
    sleep(5)
    message_box = driver.find_element(By.CLASS_NAME, "flash")
    assert unsuccessful_message in message_box.text
    assert "https://the-internet.herokuapp.com/login" == driver.current_url

def test_incorrect_password(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    user = "tomsmith"
    password = "SuperSecret"
    driver.find_element(By.ID, "username").send_keys(user)
    driver.find_element(By.ID, "password").send_keys(password)
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    unsuccessful_message = "Your password is invalid!"
    sleep(5)
    message_box = driver.find_element(By.CLASS_NAME, "flash")
    assert unsuccessful_message in message_box.text
    assert "https://the-internet.herokuapp.com/login" == driver.current_url




