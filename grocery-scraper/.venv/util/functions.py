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
    y = 1000
    for timer in range(0, 10):
        driver.execute_script("window.scrollTo(0, " + str(y) + ")")
        y += 500
        time.sleep(1)

# Function for extracting data
def extract_product_data(driver):
    try:
        # Wait for the elements to load (you can use WebDriverWait for more advanced waiting)
        time.sleep(5)
        privacyBtn = driver.find_element(By.CSS_SELECTOR, 'button[class="lds__privacy-policy__btnClose"]')
        privacyBtn.click()
        auto_scroll(driver)

        # Extract data
        title_model = TitleExtractor
        title_model.extract_data(driver)

        price_model = PriceExtractor
        price_model.extract_data(driver)

    except Exception as e:
        print(f"An error occurred: {str(e)}")