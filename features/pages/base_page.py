class BasePage:


    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        return self

    def clickButton(self, by_locator):
        self.driver.find_element(*by_locator).click()