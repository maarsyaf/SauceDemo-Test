from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.zip_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.finish_button = (By.ID, "finish")
        self.complete_header = (By.CSS_SELECTOR, '[data-test="complete-header"]')

    def proceed_to_checkout(self):
        self.driver.find_element(*self.checkout_button).click()

    def fill_checkout_info(self, first_name, last_name, zip_code):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.zip_code_input).send_keys(zip_code)
        self.driver.find_element(*self.continue_button).click()

    def complete_checkout(self):
        self.driver.find_element(*self.finish_button).click()

    def verify_order_success(self):
        return self.driver.find_element(*self.complete_header).text
