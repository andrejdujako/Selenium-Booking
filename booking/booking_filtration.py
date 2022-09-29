# This file includes a class with instance methods that are responsible to react with the
# results to apply filtrations
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BookingFiltration:
    def __init__(self, driver: WebDriver):
        # We use driver: WebDriver so that the driver variable knows its type
        # and we get autocomplete as the normal driver
        self.driver = driver

    def apply_star_rating(self):
        four_stars_button = self.driver.find_element(By.CSS_SELECTOR, 'input[name = "class=4"]')
        four_stars_button.driver.click()

    #     To identify the child elements of a selected element we use:

    # <Previously_Selected_Element>.find_elements(By.CSS_SELECTOR, '*')
    # Note that we use find_elementS



    # id = __bui - c655072 - 18
    # name = "class=4"