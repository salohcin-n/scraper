from models.base import PriceExtractor, TitleExtractor, DisplayData
from util.functions import initialize_driver, auto_scroll_and_extract_prices

class FreshExtractor:
    def __init__(self):
        self.driver = None

    def run(self):
        # Initialize the WebDriver
        self.driver = initialize_driver()

        # Open a webpage and perform actions
        auto_scroll_and_extract_prices(self.driver)

        # Create instances of PriceExtractor and TitleExtractor and extract data
        price_extractor = PriceExtractor(self.driver)
        title_extractor = TitleExtractor(self.driver)
        display = DisplayData()

        print(display.display_prices_and_titles(prices=price_extractor.extract_data(), titles=title_extractor.extract_data()))

        # Close the browser
        self.driver.quit()