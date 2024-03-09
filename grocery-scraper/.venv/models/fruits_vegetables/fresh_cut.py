from selenium.webdriver.common.by import By
from models.base import DataExtractor
from util.functions import initialize_driver, web_functions, auto_scroll, last_page
from data.data import saveData

# Global variables
page_url = 'https://www.atlanticsuperstore.ca/food/fruits-vegetables/fresh-cut-fruits-vegetables/c/28198'

# Main class for Fresh Vegetables section
class FreshCutProduceExtractor:

    def run(self):
        try:
            # Initialize the WebDriver
            self.driver = initialize_driver(page_url)

            # Initializing lists and display object
            fresh_cut_data = []

            # Open a webpage and perform actions
            web_functions(self.driver)

            #Adding extracted data to a tuple list.
            data_extractor = DataExtractor(self.driver)
            fresh_cut_data.append(data_extractor.extract_data())

            # Save data and Close the browser
            saveData(fresh_cut_data, '''fresh_cut_produce''')
            self.driver.quit()

        # End of try/except error handling
        except Exception as e:
            print(f"Unexpected error with run function - herbs: {str(e)}")