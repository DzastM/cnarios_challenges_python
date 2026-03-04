from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from ..base_page import BasePage
from .cart_page import CartPage

class ProductPurchasingPage(BasePage):

    HEADER = (By.TAG_NAME, "h1")
    EXPECTED_HEADER_TEXT = "E-commerce End-to-End Product Purchasing Flow"
    URL = "https://www.cnarios.com/challenges/product-purchasing"
    VIEW_CART_BUTTON = (By.CSS_SELECTOR, "header button")
    CART_SELECTOR = (By.CSS_SELECTOR, ".space-y-4 > div")
    PRODUCT_NAME = (By.XPATH, ".//p[contains(.,'($')]")
    PRODUCT_QUANTITY = (By.CSS_SELECTOR, ".space-x-2 > p")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".font-semibold")
    TOTAL_PRICE = (By.XPATH, ".//h6[contains(text(),'Total:')]")
    
    def add_product_to_cart(self, product_name):
        product_locator = By.XPATH, f"//div[h6='{product_name}']//div[button]"
        self.move_to_element(product_locator)
        self.click_element(product_locator)

    def click_view_cart(self) -> CartPage:
        self.scroll_to_top()
        self.click_element(self.VIEW_CART_BUTTON)
        return CartPage(self.driver)

    def assert_header_text(self):
        actual_text = self.driver.find_element(*self.HEADER).text
        assert actual_text == self.EXPECTED_HEADER_TEXT, f"Expected header text to be '{self.EXPECTED_HEADER_TEXT}', but got '{actual_text}'"
    
    def assert_if_cart_is_empty(self):
        cart_items_selector = self.driver.find_elements(*self.CART_SELECTOR)
        assert len(cart_items_selector) == 0, f"Expected cart to be empty, but found items: {[item.find_element(*self.PRODUCT_NAME).text for item in cart_items_selector]}"