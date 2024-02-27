from selenium.webdriver.common.by import By

class BaseExtractor:
    def __init__(self, driver):
        self.driver = driver

    def extract_data(self):
        raise NotImplementedError("extract_data method must be implemented in subclass")

# Extracting product prices from elements on the webpage
class PriceExtractor(BaseExtractor):
    def __init__(self, driver):
        super().__init__(driver)

    def extract_data(self):
        try:
            # Find elements with the attribute 'data-testid' set to 'price'
            price_elements = self.driver.find_elements(By.CSS_SELECTOR, 'p[data-testid="price"]')

            # Extract text from each price element and store it in a list
            prices = [element.text for element in price_elements]

            # Filter out prices with "sale"
            prices = [price for price in prices if "sale" not in price.lower()]

            return prices

        except Exception as e:
            print(f"An error occurred while extracting prices: {str(e)}")
            return []

# Extracting product titles from elements on the webpage
class TitleExtractor(BaseExtractor):
    def __init__(self, driver):
        super().__init__(driver)

    def extract_data(self):
        try:
            # Find elements with the attribute 'data-testid' set to 'product-title'
            title_elements = self.driver.find_elements(By.CSS_SELECTOR, 'h3[data-testid="product-title"]')

            # Extract text from each title element and store it in a list
            titles = [element.text for element in title_elements]

            return titles

        except Exception as e:
            print(f"An error occurred while extracting titles: {str(e)}")
            return []

# Class to display data from each extraction
class DisplayData:
    @staticmethod
    def display_prices_and_titles(prices, titles):
        try:
            for price, title in zip(prices, titles):
                print(f"Title: {title} - Price: {price}")
        except Exception as e:
            print(f"An error occurred while printing data: {str(e)}")