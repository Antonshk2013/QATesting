from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def click_checkout(self):
        btn = self.wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        btn.click()

    def get_total_price(self) -> float:
        total_text = self.driver.find_element(By.CLASS_NAME, "summary_total_label").text
        # Пример: "Total: $58.29"
        total_str = total_text.replace("Total: $", "")
        return float(total_str)