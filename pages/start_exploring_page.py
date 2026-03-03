from selenium.webdriver.common.by import By

from .base_page import BasePage

class StartExploringPage(BasePage):
    HEADING = (By.TAG_NAME, "h1")

    def get_heading_text(self):
        return self.driver.find_element(*self.HEADING).texts