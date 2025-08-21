from tests.base_test import BaseTest


class TestCheckoutProcess(BaseTest):
    def test_full_checkout(self,login_page):

        # Step 1: Open site and login
        self.login_page.enter_username("standard_user")
        self.login_page.enter_password("secret_sauce")
        self.login_page.click_on_login_button()
        assert self.login_page.driver.current_url == "https://www.saucedemo.com/inventory.html", "Не удалось войти в систему."
        inventory_list = self.login_page.get_inventory_list()
        assert inventory_list, "Список товаров не найден на странице."

        # Step 2: Add items to cart
        self.inventory_page.add_item_to_cart("add-to-cart-sauce-labs-backpack")
        self.inventory_page.add_item_to_cart("add-to-cart-sauce-labs-bolt-t-shirt")
        self.inventory_page.add_item_to_cart("add-to-cart-sauce-labs-onesie")

        # # Step 3: Go to cart and proceed to checkout
        self.inventory_page.go_to_cart()
        self.cart_page.click_checkout()

        # Step 4: Fill checkout form
        self.checkout_info.fill_info("Sergii", "Ivanov", "79312")

        # Step 5: Read and verify total
        total = self.overview_page.get_total_price()
        assert total == 58.29, f"Expected total to be 58.29, but got {total}"