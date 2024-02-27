from selenium.webdriver.common.by import By
from models.base import PriceExtractor, TitleExtractor, DisplayData
from util.functions import initialize_driver, web_functions, auto_scroll, last_page

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

            # Initializing lists and display object
            all_prices = []
            all_titles = []
            display = DisplayData()

            # Open a webpage and perform actions
            web_functions(self.driver)

            # Create instances of PriceExtractor and TitleExtractor and extract data
            price_extractor = PriceExtractor(self.driver)
            title_extractor = TitleExtractor(self.driver)

            if(self.driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Next Page"]')):
                for x in range(last_page(driver=self.driver)):
                    all_prices.append(price_extractor.extract_data())
                    all_titles.append(title_extractor.extract_data())
                    nextPageBtn = self.driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Next Page"]')
                    nextPageBtn.click()
                    auto_scroll(self.driver)

                # Looping through the list array to display list items with the prices
                for price, title in zip(all_prices, all_titles):
                    print(display.display_prices_and_titles(price, title))

            else:
                # Printing the list from a page if all products are on the same page
                print(display.display_prices_and_titles(prices=price_extractor.extract_data(), titles=title_extractor.extract_data()))

            # Close the browser
            self.driver.quit()

        # End of try/except error handling
        except:
            print("Unexpected error with run function")