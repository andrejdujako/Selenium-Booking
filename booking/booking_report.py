# We use this file to parse the hotel cards
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver


class BookingReport:
    # def __init__(self, *deal_boxes: WebElement):
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_attributes(self):
        results = []
        deal_boxes = self.driver.find_elements(By.CSS_SELECTOR, 'div[data-testid="property-card"]')
        for deal_box in deal_boxes:
            deal_name = deal_box.find_element(By.CSS_SELECTOR,
                                              'div[data-testid="title"]')\
                                            .get_attribute('innerHTML').strip()

            deal_price = deal_box.find_element(By.CSS_SELECTOR,
                                               'div[data-testid="price-and-discounted-price"]')
            price = deal_price.find_elements(By.XPATH, "./child::*")[0].get_attribute('innerHTML')\
                .strip().split("&nbsp;")
            final_price = ' '.join(price)

            deal_score = deal_box.find_element(By.CSS_SELECTOR,
                                               'div[data-testid="review-score"]')
            score = deal_score.find_elements(By.XPATH, "./child::*")[0].get_attribute('innerHTML')

            results.append([deal_name, final_price, score])
            # print(deal_name, final_price, score)
        return results

# data-testid="title" # WE WILL USE THIS TO GET THE TITLE OF THE CARD
# data-testid="price-and-discounted-price" # USED TO GET THE PRICE
# data-testid="review-score" # USED TO GET THE SCORE