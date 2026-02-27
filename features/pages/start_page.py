from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage
from features.pages.challenges_page import ChallengesPage
from features.pages.start_exploring_page import StartExploringPage

class StartPage(BasePage): 
    URL = "https://www.cnarios.com/#how-it-works"
    HEADING = (By.TAG_NAME, "h1")
    CHALLENGES_TEXT = "Challenges"
    START_EXPLORING_TEXT = "Start Exploring"
    CHALLENGES_BUTTON = (By.XPATH, f"//button[text()='{CHALLENGES_TEXT}']")
    START_EXPLORING_BUTTON = (By.XPATH, f"//button[text()='{START_EXPLORING_TEXT}']")

    def click_option_button(self, name:str) -> None:
        if name == self.CHALLENGES_TEXT:
            self.clickButton(self.CHALLENGES_BUTTON)
            return ChallengesPage(self.driver)
        else:
            self.clickButton(self.START_EXPLORING_BUTTON)
            return StartExploringPage(self.driver)


    
    def get_heading_text(self):
        return self.driver.find_element(*self.HEADING).text