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



def test_home_work3(driver):
    start_url = "https://itcareerhub.de/ru"
    driver.get(start_url)


    """# Проверяет, что на странице отображаются: Логитип ITCareerHub"""
    assert driver.find_element(By.CSS_SELECTOR, 'img[alt="IT Career Hub"]'), "logo not found"

    """# Проверяет, что на странице отображаются: 
        Ссылка “Программы”
        Ссылка “Способы оплаты”
        Ссылка “Новости”
        Ссылка “О нас”
        Ссылка “Отзывы”"""

    texts = [
        "Программы",
        "Способы оплаты",
        "Новости",
        "О нас",
        "Отзывы"
    ]
    for text in texts:
        assert driver.find_element(By.LINK_TEXT, text), f"Link '{text}' not found"

    """# Проверяет, что на странице отображаются: Кнопки переключения языка (ru и de)"""
    button_lang_de = driver.find_element(By.LINK_TEXT, "de")
    button_lang_ru = driver.find_element(By.LINK_TEXT, "ru")
    assert button_lang_de.is_displayed(), "Button 'de' is hidden"
    assert button_lang_ru.is_displayed(), "Button 'ru' is hidden"

    """# Проверяет, что на странице отображаются: Кнопки переключения языка (ru и de)"""
    icon = driver.find_element(By.CSS_SELECTOR, 'img[imgfield="tn_img_1710153310161"]')
    icon.click()
    driver.implicitly_wait(2)

    """Проверяет, что на странице отображаются Проверить что текст “Если вы не дозвонились, заполните форму на сайте. Мы свяжемся с вами” отображается"""
    text = "Если вы не дозвонились, заполните форму на сайте. Мы свяжемся с вами"
    assert text in driver.page_source, "Waiting anothe text"
