from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import pytest
import os


lib_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@pytest.fixture
def driver():
    service = Service(lib_dir+"/chromedriver-linux64/chromedriver")
    options = Options()
    driver = webdriver.Firefox(service=service, options=options)
    yield driver
    driver.quit()

# def test_cats(driver):
#     driver.get("https://the-internet.herokuapp.com/checkboxes")
#     sleep(2)
#     check_box = driver.find_element(By.CSS_SELECTOR, "#checkboxes > input[type=checkbox]:nth-child(1)")
#     sleep(1)
#     check_box.click()
#     sleep(1)
#     assert check_box.get_attribute("checked") == "true"

def test_checkbox_1(driver):
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    sleep(2)
    checkbox = driver.find_element(By.CSS_SELECTOR, "#checkboxes > input[type=checkbox]:nth-child(1)")
    sleep(1)
    checkbox.click()
    sleep(1)
    assert checkbox.get_attribute("checked") == "true"

def test_checkboxes_2(driver):
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    sleep(2)
    check_box = driver.find_element(By.CSS_SELECTOR, "#checkboxes > input[type=checkbox]:nth-child(3)")
    sleep(2)
    check_box.click()
    sleep(2)
    assert not check_box.is_selected()



