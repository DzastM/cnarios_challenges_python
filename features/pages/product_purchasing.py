from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from features.pages.base_page import BasePage

class ProductPurchasingPage(BasePage):
    HEADING = (By.TAG_NAME, "h1")
    URL = "https://www.cnarios.com/challenges/product-purchasing"
    VIEW_CART_BUTTON = (By.CSS_SELECTOR, "header button")

    def get_heading_text(self):
        return self.driver.find_element(*self.HEADING).text
    
    def add_product_to_cart(self, product_name):
        product_locator = By.XPATH, f"//div[h6='{product_name}']//div[button]"
        self.move_to_element(product_locator)
        self.click_element(product_locator)

    def click_view_cart(self):
        self.scroll_to_top()
        self.click_element(self.VIEW_CART_BUTTON)

    def get_cart_items(self) -> list:
        cart_items = self.driver.find_elements(By.CSS_SELECTOR, ".space-y-4 > div")
        list_of_items = {}
        for item in cart_items:
            list_of_items[item.find_element(By.XPATH, ".//p[contains(.,'($')]").text] = (item.find_element(By.CSS_SELECTOR, ".space-x-2 > p").text, item.find_element(By.CSS_SELECTOR, ".font-semibold").text)
        return list_of_items       
    
    def get_item_name_and_quantity(self, item):
        
        return name, quantity