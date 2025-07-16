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



"""Кнопки переключения языка (ru и de)"""
def test_change_languig(driver):
    start_url = "https://itcareerhub.de/ru"
    driver.get(start_url)
    sleep(2)
    link_payment_method = driver.find_element(By.LINK_TEXT, "de")
    sleep(2)
    link_payment_method.click()
    sleep(2)
    new_url_str = "https://itcareerhub.de/"
    new_url = driver.current_url
    assert new_url_str == new_url

"""Открывает https://itcareerhub.de/ru
Проверяет, что на странице отображаются:
Логитип ITCareerHub
Ссылка “Программы”
Ссылка “Способы оплаты”
Ссылка “Новости”
Ссылка “О нас”
Ссылка “Отзывы”
Кнопки переключения языка (ru и de)
Кликнуть по иконке с телефонной трубкой
Проверить что текст “Если вы не дозвонились, заполните форму на сайте. Мы свяжемся с вами” отображается."""

def test_phone_icon(driver):
    start_url = "https://itcareerhub.de/ru"
    driver.get(start_url)
    sleep(2)

    selector_string = "#rec717843722 > div > div > div.t396__elem.tn-elem.tn-elem__7178437221710153310161 > a"
    link_payment_method = driver.find_element(By.CSS_SELECTOR, selector_string)
    sleep(2)
    link_payment_method.click()
    sleep(2)
    new_url_str = "https://itcareerhub.de/"
    new_url = driver.current_url
    assert new_url_str == new_url

# mg[imgfield="tn_img_1710153310161"]
