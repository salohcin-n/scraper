from selenium.webdriver.common.by import By
from models.base import DataExtractor
from models.types import GroceryType
from util.functions import initialize_driver, web_functions, auto_scroll, last_page
from data.data import saveData

# Global variables
page_url = 'https://www.atlanticsuperstore.ca/food/fruits-vegetables/fresh-juice-smoothies/c/28200'

# Main class for Fresh Vegetables section
class FreshJuiceAndSmoothiesExtractor:

    def run(self):
        try:
            # Initialize the WebDriver
            self.driver = initialize_driver(page_url)

            # Initializing lists and display object
            fresh_juice_and_smoothies_data = []

            # Open a webpage and perform actions
            web_functions(self.driver)

            #Adding extracted data to a tuple list.
            data_extractor = DataExtractor(self.driver)
            fresh_juice_and_smoothies_data.append(data_extractor.extract_data())

            # Save data and Close the browser
            saveData(fresh_juice_and_smoothies_data, GroceryType.JUICE_AND_SMOOTHIES.value)
            self.driver.quit()

        # End of try/except error handling
        except Exception as e:
            print(f"Unexpected error with run function - Fresh juice and smoothies: {str(e)}")