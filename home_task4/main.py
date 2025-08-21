from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
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


"""Задание 1: Проверка изменения текста кнопки
Тестируемый сайт:
http://uitestingplayground.com/textinput
Шаги теста:
Перейдите на сайт Text Input.
Введите в поле ввода текст "ITCH".
Нажмите на синюю кнопку.
Проверьте, что текст кнопки изменился на "ITCH"."""
def test_home_work_task1(driver):
    start_url = "http://uitestingplayground.com/textinput"
    driver.get(start_url)
    button_locator = (By.ID, "updatingButton")
    input_locator = (By.ID, "newButtonName")
    wait = WebDriverWait(driver, 10)

    input_field = driver.find_element(*input_locator)
    input_field.clear()
    input_field.send_keys("ITCH")

    button = driver.find_element(*button_locator)
    button.click()
    wait.until(EC.text_to_be_present_in_element(button_locator, "ITCH"))


"""Задание 2: Проверка загрузки изображений
Тестируемый сайт:
https://bonigarcia.dev/selenium-webdriver-java/loading-images.html
Шаги теста:
Перейдите на сайт Loading Images.
Дождитесь загрузки всех изображений.
Получите значение атрибута alt у третьего изображения.
Убедитесь, что значение атрибута alt равно "award"."""
def test_home_work_task2(driver):
    start_url = "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    driver.get(start_url)
    wait = WebDriverWait(driver, 15)
    container_locator = (By.CSS_SELECTOR, "#image-container img")
    text_locator = (By.ID, "text")

    wait.until(EC.text_to_be_present_in_element(text_locator, "Done!"))

    images = driver.find_elements(*container_locator)
    assert len(images) >= 3, f"Waiting 3 images, but get less"

    third_img_alt = images[2].get_attribute("alt")
    assert third_img_alt == "award", f"Waiting alt='award', but get alt='{third_img_alt}'"