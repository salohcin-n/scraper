from selenium.webdriver.common.by import By
from models.base import DataExtractor
from util.functions import initialize_driver, web_functions, auto_scroll, last_page
from data.data import saveData

# Global variables
page_url = 'https://www.atlanticsuperstore.ca/food/fruits-vegetables/dried-fruits-nuts/c/28199'

# Main class for Fresh Vegetables section
class DriedFruitsAndNutsExtractor:

    def run(self):
        try:
            # Initialize the WebDriver
            self.driver = initialize_driver(page_url)

            # Initializing lists and display object
            dried_fruits_nuts_data = []

            # Open a webpage and perform actions
            web_functions(self.driver)

            #Adding extracted data to a tuple list.
            data_extractor = DataExtractor(self.driver)
            dried_fruits_nuts_data.append(data_extractor.extract_data())

            # Save data and Close the browser
            saveData(dried_fruits_nuts_data, '''dried_fruits_and_nuts''')
            self.driver.quit()

        # End of try/except error handling
        except Exception as e:
            print(f"Unexpected error with run function - dried fruits and nuts: {str(e)}")