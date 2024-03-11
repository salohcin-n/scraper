from selenium.webdriver.common.by import By
from models.base import DataExtractor
from models.types import GroceryType
from util.functions import initialize_driver, web_functions, auto_scroll, last_page
from data.data import saveData

# Global variables
page_url = 'https://www.atlanticsuperstore.ca/food/fruits-vegetables/in-store-salads/c/59222'

# Main class for In-Store Salads section
class InStoreSaladsExtractor:

    def run(self):
        try:
            # Initialize the WebDriver
            self.driver = initialize_driver(page_url)

            # Initializing lists and display object
            salads_data = []

            # Open a webpage and perform actions
            web_functions(self.driver)

            #Adding extracted data to a tuple list.
            data_extractor = DataExtractor(self.driver)
            salads_data.append(data_extractor.extract_data())

            # Save data and Close the browser
            saveData(salads_data, GroceryType.SALADS.value)
            self.driver.quit()

        # End of try/except error handling
        except Exception as e:
            print(f"Unexpected error with run function - in store salads: {str(e)}")