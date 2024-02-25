from models.base import PriceExtractor, TitleExtractor, DisplayData
from util.functions import initialize_driver, extract_product_data

# Global variables
page_url = 'https://www.atlanticsuperstore.ca/food/fruits-vegetables/fresh-vegetables/c/28195'
# next_page_element = ''

class FreshExtractor:
    def __init__(self):
        self.driver = None

    def run(self):
        # Initialize the WebDriver
        self.driver = initialize_driver(page_url)

        # self.driver.find_element(By.CSS)
        # next_page(self.driver)

        # Open a webpage and perform actions
        extract_product_data(self.driver)

        # Create instances of PriceExtractor and TitleExtractor and extract data
        price_extractor = PriceExtractor(self.driver)
        title_extractor = TitleExtractor(self.driver)
        display = DisplayData()

        print(display.display_prices_and_titles(prices=price_extractor.extract_data(), titles=title_extractor.extract_data()))

        # Close the browser
        self.driver.quit()