from selenium import webdriver
from selenium.webdriver.common.by import By
from models.base import PriceExtractor, TitleExtractor
import time

# Initializing Chrome Web Driver
def initialize_driver(url):
    driver = webdriver.Chrome()
    driver.get(url)
    return driver

# Function for auto scrolling down the page
def auto_scroll(driver):
    try:
        y = 1000
        for timer in range(0, 20):
            driver.execute_script("window.scrollTo(0, " + str(y) + ")")
            y += 150
            time.sleep(0.5)
    except:
        print("Error with auto_scroll function")

# Function for scrolling to the bottom of the page immediately
def scroll_to_bottom(driver):
    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    except:
        print("Error with the scroll_to_bottom function")

# Function for extracting data
def extract_product_data(driver):
    try:
        # Initializing lists
        all_prices = []
        all_titles = []

        # Wait for the elements to load (you can use WebDriverWait for more advanced waiting)
        time.sleep(5)
        nextPageBtn = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Next Page"]')
        privacy_btn(driver)
        auto_scroll(driver)

        while(nextPageBtn):
            # for x in range(1, 6):
                # Go to next page and begin scrolling
            nextPageBtn.click()
            time.sleep(3)
            auto_scroll(driver)

            title_model += TitleExtractor.extract_data(driver)
            price_model += PriceExtractor.extract_data(driver)

        # Extract data
        title_model = TitleExtractor
        price_model = PriceExtractor

        title_model.extract_data(driver)
        price_model.extract_data(driver)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def privacy_btn(driver):
    try:
        privacyBtn = driver.find_element(By.CSS_SELECTOR, 'button[class="lds__privacy-policy__btnClose"]')
        privacyBtn.click()
    except:
        print("Error with privacy button")

# def next_page(driver):
#     try:
#         nextPageBtn = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Next Page"]')
#
#
#     except:
#         print(f"An error occurred: {str(e)}")