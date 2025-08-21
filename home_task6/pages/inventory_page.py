from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def add_item_to_cart(self, item_id):
        add_button = self.wait.until(EC.element_to_be_clickable((By.ID, item_id)))
        add_button.click()

    def go_to_cart(self):
        cart = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
        cart.click()