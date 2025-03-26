import unittest
from selenium.webdriver.common.by import By
from config.config import BASE_URL, VALID_USERNAME, VALID_PASSWORD, INVALID_USERNAME, INVALID_PASSWORD
from library import BaseTest
from assertions import Assertions
from pages import LoginPage, InventoryPage, CartPage

class TestSauceDemo(unittest.TestCase, BaseTest):
    def setUp(self):
        self.setup()
        self.driver.get(BASE_URL)
        print("\n🔄 Memulai test...")

    def test1_successful_login(self):
        print("🟢 Test: Login dengan kredensial valid")
        login_page = LoginPage(self.driver)
        login_page.login(VALID_USERNAME, VALID_PASSWORD)
        expected_url = f"{BASE_URL}/inventory.html"
        Assertions.assert_equal(self.driver.current_url, expected_url, "Login gagal!")
        print("✅ Login berhasil!")

    def test2_invalid_login(self):
        print("🔴 Test: Login dengan kredensial tidak valid")
        login_page = LoginPage(self.driver)
        login_page.login(INVALID_USERNAME, INVALID_PASSWORD)
        
        try:
            error_message = self.driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
            Assertions.assert_in("Epic sadface", error_message, "Pesan error tidak muncul!")
            print("✅ Pesan error muncul dengan benar!")
        except:
            print("❌ Pesan error tidak ditemukan!")

    def test3_add_to_cart_and_checkout(self):
        print("🛒 Test: Menambahkan produk ke keranjang dan checkout")
        login_page = LoginPage(self.driver)
        login_page.login(VALID_USERNAME, VALID_PASSWORD)

        inventory_page = InventoryPage(self.driver)
        inventory_page.add_product_to_cart()
        inventory_page.go_to_cart()

        cart_page = CartPage(self.driver)
        cart_page.proceed_to_checkout()
        cart_page.fill_checkout_info("Abdillah", "Arsyaf", "42116")
        cart_page.complete_checkout()

        success_message = cart_page.verify_order_success()
        Assertions.assert_equal(success_message, "Thank you for your order!", "Checkout gagal!")
        print("✅ Checkout berhasil!")

    def tearDown(self):
        print("📌 Test selesai, menutup browser...\n")
        self.teardown()

if __name__ == "__main__":
    unittest.main(verbosity=2)
