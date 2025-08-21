import time
import pytest
import os

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

lib_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@pytest.fixture
def driver():
    service = Service(lib_dir+"/chromedriver-linux64/chromedriver")
    options = Options()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

"""
Задание 1: Проверка наличия текста в iframe
Открыть страницу
Перейти по ссылке: https://bonigarcia.dev/selenium-webdriver-java/iframes.html.
Проверить наличие текста
Найти фрейм (iframe), в котором содержится искомый текст.
Переключиться в этот iframe.
Найти элемент, содержащий текст "semper posuere integer et senectus justo curabitur.".
Убедиться, что текст отображается на странице."""
def test_home_work_task1(driver):
    start_url = "https://bonigarcia.dev/selenium-webdriver-java/iframes.html"
    driver.get(start_url)
    text = r'semper posuere integer et senectus justo curabitur.'
    iframe_locator = (By.TAG_NAME, "iframe")
    body_locator = (By.TAG_NAME, "body")
    wait = WebDriverWait(driver, 10)
    iframes = wait.until(EC.presence_of_all_elements_located(iframe_locator))
    target_iframe = None

    for iframe in iframes:
        driver.switch_to.frame(iframe)
        body_text = driver.find_element(*body_locator).text
        if text in body_text:
            target_iframe = iframe
            break
        driver.switch_to.default_content()

    assert target_iframe is not None, "Iframe с искомым текстом не найден"
    elements = driver.find_elements(By.XPATH, "//p")
    target_el = None
    for el in elements:
        if text in el.text:
            target_el = el
            break

    assert target_el is not None and target_el.is_displayed(), "Текст не отображается на странице"


    assert target_iframe is not None, "Iframe с искомым текстом не найден"

"""Задание 2: Тестирование Drag & Drop (Перетаскивание изображения в корзину)
Открыть страницу Drag & Drop Demo.
Перейти по ссылке: https://www.globalsqa.com/demo-site/draganddrop/.
Выполнить следующие шаги:
Захватить первую фотографию (верхний левый элемент).
Перетащить её в область корзины (Trash).
Проверить, что после перемещения:
В корзине появилась одна фотография.
В основной области осталось 3 фотографии."""
def test_home_work_task2(driver):
    start_url = "https://www.globalsqa.com/demo-site/draganddrop/"
    driver.get(start_url)
    wait = WebDriverWait(driver, 10)
    trash_locator = (By.ID, "trash")
    iframe_locator = (By.CSS_SELECTOR, "iframe.demo-frame")
    agree_button_locator = (By.XPATH, "/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/button[1]")
    gallery_items_locator = (By.CSS_SELECTOR, "#gallery > li")
    trash_items_locator = (By.CSS_SELECTOR, "#trash > ul > li")

    agree_button = wait.until(EC.element_to_be_clickable(agree_button_locator))
    agree_button.click()

    iframe = wait.until(EC.presence_of_element_located(iframe_locator))
    driver.switch_to.frame(iframe)

    gallery_items = driver.find_elements(*gallery_items_locator)
    draggable_li = gallery_items[0]
    trash = driver.find_element(*trash_locator)

    actions = ActionChains(driver)
    actions.drag_and_drop(draggable_li, trash).perform()

    time.sleep(2)
    trash_items = driver.find_elements(*trash_items_locator)
    gallery_items = driver.find_elements(*gallery_items_locator)
    assert len(trash_items) == 1, f"Ожидалось 1 элемент в корзине, найдено: {len(trash_items)}"
    assert len(gallery_items) == 3, f"Ожидалось 3 элемента в галерее, найдено: {len(gallery_items)}"