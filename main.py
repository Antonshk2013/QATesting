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


def test_about_page(driver):
    driver.get("https://itcareerhub.de/ru")
    sleep(5)