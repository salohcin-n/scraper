from selenium import webdriver
from selenium.webdriver.common.by import By
from models.base import PriceExtractor, TitleExtractor
import time

def initialize_driver():
    # Initialize the WebDriver
    driver = webdriver.Chrome()
    return driver

def auto_scroll(driver):
    y = 1000
    for timer in range(0, 10):
        driver.execute_script("window.scrollTo(0, " + str(y) + ")")
        y += 500
        time.sleep(1)

def auto_scroll_and_extract_prices(driver):
    try:
        # Open a webpage
        driver.get('https://www.atlanticsuperstore.ca/')

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
