from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutOverviewPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def get_total_price(self):
        total_text = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))).text
        return float(total_text.replace("Total: $", ""))
