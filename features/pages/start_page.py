from selenium.webdriver.common.by import By

class StartPage:
    URL = "https://www.cnarios.com/#how-it-works"
    HEADING = (By.TAG_NAME, "h1")  

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        return self
    
    def get_heading_text(self):
        return self.driver.find_element(*self.HEADING).text