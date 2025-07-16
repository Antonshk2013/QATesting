import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

lib_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@pytest.fixture
def driver():
    service = Service(lib_dir+"/chromedriver-linux64/chromedriver")
    options = Options()
    driver = webdriver.Firefox(service=service, options=options)
    yield driver
    driver.quit()



def test_checkbox_1(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    wait = WebDriverWait(driver, 10)
    result = wait.until(EC.visibility_of_element_located((By.ID, "landscape")))
    assert result.get_attribute('src') == 'https://bonigarcia.dev/selenium-webdriver-java/img/landscape.png'



# def test_check_button(driver):
#     element = driver.find_element(By.ID, "newButtonName")
#     element.click()
#     element.send_keys("ITCH")
#     button = driver.find_element(By.ID, "updatingButton")
#     button.click()
#     wait = WebDriverWait(driver, 10)
#     wait.until(EC.text_to_be_present_in_element(By.ID, "updatingButton"))