from . import constants as const
import os, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from . booking_filtration import BookingFiltration
from . booking_report import BookingReport
from prettytable import PrettyTable


class Booking(webdriver.Firefox):
    def __init__(self, driver_path=r"E:\Selenium", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        # self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            # print("I am from __exit__")
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency=None):
        currency_element = self.find_element(By.CSS_SELECTOR,
                                             'button[data-tooltip-text="Choose your currency"]')
        currency_element.click()
        selected_currency_element = self.find_element(By.CSS_SELECTOR,
                                                      f'a[data-modal-header-async-url-param*="selected_currency={currency}"]')
        selected_currency_element.click()
        # data-modal-header-async-url-param="changed_currency=1&selected_currency=USD&top_currency=1"

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element(By.ID, "ss")
        search_field.clear()  # Clean the existing text in the field
        search_field.send_keys(place_to_go)
        time.sleep(1)
        first_result = self.find_element(By.CSS_SELECTOR, 'li[data-i="0"]')
        first_result.click()

    def select_date(self, check_in, check_out):
        check_in_element = self.find_element(By.CSS_SELECTOR, f'td[data-date="{check_in}"]')
        check_in_element.click()
        check_out_element = self.find_element(By.CSS_SELECTOR, f'td[data-date="{check_out}"]')
        check_out_element.click()
    # data - date = "2022-09-20"

    def select_adults(self, adults, children, rooms):
        self.find_element(By.ID, "xp__guests__toggle").click()
        # Click on the settings bar

        if adults < 2:
            adult_minus_button = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Decrease number of Adults"]')
            adult_minus_button.click()
        if adults > 2:
            adult_plus_button = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Increase number of Adults"]')

            for _ in range(adults-2):
                adult_plus_button.click()
        #         element.get_attribute('<attribute>') to get a value back (might be a string)
        if children:
            children_plus_button = self.find_element(By.CSS_SELECTOR,
                                                     'button[aria-label="Increase number of Children"]')
            for _ in range(children):
                children_plus_button.click()
            self.find_element(By.CSS_SELECTOR, 'select[data-group-child-age="0"]').click()
            self.find_element(By.CSS_SELECTOR, 'option[value="14"]').click()

        if rooms and rooms > 1:
            rooms_plus_button = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Increase number of Rooms"]')
            for _ in range(rooms-1):
                rooms_plus_button.click()

    def click_search(self):
        self.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        # search_button = self.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        # search_button.click()

    def apply_filters(self):
        filters = BookingFiltration(driver=self)
        # We pass the webdriver we use to the other class used for filters
        filters.sort_lowest()
        filters.apply_star_rating(3, 4)

    def get_results(self):
        report = BookingReport(driver=self)
        table = PrettyTable(field_names=["Name", "Price", "Score"])
        table.add_rows(report.get_attributes())
        # It's good to pass a nested list like we have already
        print(table)

