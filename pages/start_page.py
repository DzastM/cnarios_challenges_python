from selenium.webdriver.common.by import By

from .base_page import BasePage
from .challenges_page import ChallengesPage
from .start_exploring_page import StartExploringPage

class StartPage(BasePage): 
    URL = "https://www.cnarios.com/#how-it-works"
    HEADING = (By.TAG_NAME, "h1")
    CHALLENGES_TEXT = "Challenges"
    START_EXPLORING_TEXT = "Start Exploring"
    CHALLENGES_BUTTON = (By.XPATH, f"//button[text()='{CHALLENGES_TEXT}']")
    START_EXPLORING_BUTTON = (By.XPATH, f"//button[text()='{START_EXPLORING_TEXT}']")

    def click_option_button(self, name:str) -> None:
        if name == self.CHALLENGES_TEXT:
            self.click_element(self.CHALLENGES_BUTTON)
            return ChallengesPage(self.driver)
        else:
            self.click_element(self.START_EXPLORING_BUTTON)
            return StartExploringPage(self.driver)


    
    def get_heading_text(self):
        return self.driver.find_element(*self.HEADING).text