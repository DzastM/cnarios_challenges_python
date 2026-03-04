from selenium.webdriver.common.by import By

from ..base_page import BasePage

class CartPage(BasePage):

    CART_SELECTOR = (By.CSS_SELECTOR, ".space-y-4 > div")
    PRODUCT_NAME = (By.XPATH, ".//p[contains(.,'($')]")
    PRODUCT_QUANTITY = (By.CSS_SELECTOR, ".space-x-2 > p")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".font-semibold")
    TOTAL_PRICE = (By.XPATH, ".//h6[contains(text(),'Total:')]")

    def get_cart_items(self) -> dict:
        cart_items_selector = self.driver.find_elements(*self.CART_SELECTOR)
        full_cart_items_info = {}  # Dictionary of items in format {item_name: (quantity, price)}
        for item in cart_items_selector:
            full_cart_items_info[item.find_element(*self.PRODUCT_NAME).text.split('(')[0].strip()] = (item.find_element(*self.PRODUCT_QUANTITY).text, item.find_element(*self.PRODUCT_PRICE).text)
        return full_cart_items_info       
    
    def get_item_name_and_quantity(self) -> dict:
        item_names_and_quantities = {}
        full_cart_items_info = self.get_cart_items()
        for item_name in full_cart_items_info:
            item_names_and_quantities[item_name] = int(full_cart_items_info[item_name][0])  # Extracting quantity from the tuple
        return item_names_and_quantities

    def get_total_price(self) -> str:
        return self.driver.find_element(*self.TOTAL_PRICE).text.split(':')[1].strip()

    def update_product_quantity(self, product_name:str, expected_quantity:int):
        current_quantity = int(self.get_item_name_and_quantity()[product_name])
        minus_button = (By.XPATH, f"//p[contains(normalize-space(.),'{product_name}')]/following-sibling::div//button[1]")
        plus_button = (By.XPATH, f"//p[contains(normalize-space(.),'{product_name}')]/following-sibling::div//button[2]")
        if current_quantity < expected_quantity:
            for _ in range(expected_quantity - current_quantity):
                self.click_element(plus_button)
        elif current_quantity > expected_quantity:
            for _ in range(current_quantity - expected_quantity):
                self.click_element(minus_button)