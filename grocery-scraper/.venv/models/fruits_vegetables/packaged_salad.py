from selenium.webdriver.common.by import By
from models.base import DisplayData, DataExtractor
from models.types import GroceryType
from util.functions import initialize_driver, web_functions, auto_scroll, last_page
from data.data import saveProduceData

# Global variables
page_url = 'https://www.atlanticsuperstore.ca/food/fruits-vegetables/packaged-salad-dressing/c/28196'

# Main class for Packaged Salads section
class PackagedSaladAndDressingsExtractor:

    def run(self):
        try:
            # Initialize the WebDriver
            self.driver = initialize_driver(page_url)

            # Initializing lists and display object
            packaged_salad_data = []
            display = DisplayData()

            # Open a webpage and perform actions
            web_functions(self.driver)

            # Create instances of PriceExtractor and TitleExtractor and extract data
            data_extractor = DataExtractor(self.driver)

            if(self.driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Next Page"]')):
                for x in range(last_page(driver=self.driver)):
                    packaged_salad_data.append(data_extractor.extract_data())
                    nextPageBtn = self.driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Next Page"]')
                    nextPageBtn.click()
                    auto_scroll(self.driver)

                saveProduceData(packaged_salad_data, GroceryType.SALAD_DRESSING.value)

            else:
                # Printing the list from a page if all products are on the same page
                print(display.display_prices_and_titles(prices=price_extractor.extract_data(), titles=title_extractor.extract_data()))

            # Close the browser
            self.driver.quit()

        # End of try/except error handling
        except:
            print("Unexpected error with run function - packaged_salad")