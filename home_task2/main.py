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

def test_payments_methods(driver):
    driver.get("https://itcareerhub.de/ru")
    sleep(2)
    link_payment_method = driver.find_element(By.LINK_TEXT, "Способы оплаты")
    sleep(2)
    link_payment_method.click()
    sleep(2)
    driver.save_screenshot("payments_methods.png")
    sleep(2)
    driver.quit()