from selenium import webdriver

def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()  # Ensure chromedriver is in your PATH
    context.driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to be found

def after_scenario(context, scenario):
    context.driver.quit()