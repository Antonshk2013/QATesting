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

def test_header_cats(driver):
    driver.get("https://suninjuly.github.io/cats.html")
    sleep(2)
    header = driver.find_element(By.TAG_NAME, "h1")
    # header = driver.find_element(By.CSS_SELECTOR, "body > main > section > div > h1")
    sleep(2)
    assert header.text == "Cat memes"


def test_count_imges(driver):
    driver.get("https://suninjuly.github.io/cats.html")
    sleep(2)
    images = driver.find_elements(By.TAG_NAME, "img")
    assert len(images) == 6


