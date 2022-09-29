# This file includes a class with instance methods that are responsible to react with the
# results to apply filtrations
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BookingFiltration:
    def __init__(self, driver: WebDriver):
        # We use driver: WebDriver so that the driver variable knows its type
        # and we get autocomplete as the normal driver
        self.driver = driver

    def sort_lowest(self):
        sort_button_element = self.driver.find_element(By.CSS_SELECTOR, 'button[data-testid="sorters-dropdown-trigger"]')
        sort_button_element.click()
        price_lowest_button = self.driver.find_element(By.CSS_SELECTOR, 'button[data-id="price"]')
        price_lowest_button.click()

    def apply_star_rating(self, *ratings):
        """
        Pass rating argument to select 2,3,4,5 stars.
        Pass 0 for unrated
        Don't pass a value if you don't want a filter
        """
        if ratings:
            for rating in ratings:
                if rating < 2 and rating != 0:
                    rating = 2
                if rating > 5:
                    rating = 5
                stars_button = self.driver.find_element(By.CSS_SELECTOR, f'input[name = "class={rating}"]')
                stars_button.click()

    #     To identify the child elements of a selected element we use:

    # <Previously_Selected_Element>.find_elements(By.CSS_SELECTOR, '*')
    # Note that we use find_elementS
    # Use get_attribute('<attr>') to get specific element attributes


