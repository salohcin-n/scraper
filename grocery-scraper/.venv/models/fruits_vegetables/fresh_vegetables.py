from selenium.webdriver.common.by import By
from models.base import PriceExtractor, TitleExtractor, DisplayData, DataExtractor
from util.functions import initialize_driver, web_functions, auto_scroll, last_page
from data.data import saveData

# Global variables
page_url = 'https://www.atlanticsuperstore.ca/food/fruits-vegetables/fresh-vegetables/c/28195'

# Main class for Fresh Vegetables section
class FreshVeggieExtractor:

    # Method to self initialize the driver - Currently running from scraper.py
    # def __init__(self):
    #     self.driver = initialize_driver(page_url)

    def run(self):
        try:
            # Initialize the WebDriver
            self.driver = initialize_driver(page_url)

            # Initializing lists and display object for single page scrapes
            veg_data = []
            display = DisplayData()

            # Open a webpage and perform actions
            web_functions(self.driver)

            # Create instances of data extractor
            data_extractor = DataExtractor(self.driver)

            # If the next page button exists, loop through the max pages and extract data
            if(self.driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Next Page"]')):
                for x in range(last_page(driver=self.driver)):
                    veg_data.append(data_extractor.extract_data())
                    nextPageBtn = self.driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Next Page"]')
                    nextPageBtn.click()
                    auto_scroll(self.driver)

                # 2nd parameter is the table name
                saveData(veg_data, '''fresh_vegetables''')

            else:
                # Printing the list from a page if all products are on the same page
                print(display.display_prices_and_titles(prices=price_extractor.extract_data(), titles=title_extractor.extract_data()))

            # Close the browser
            self.driver.quit()

        # End of try/except error handling
        except:
            print("Unexpected error with run function - fresh_vegetables")