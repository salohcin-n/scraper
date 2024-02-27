from selenium import webdriver
from selenium.webdriver.common.by import By
from models.base import PriceExtractor, TitleExtractor
import time

# Initializing Chrome Web Driver
def initialize_driver(url):
    try:
        driver = webdriver.Chrome()
        driver.get(url)
        return driver
    except:
        print("Issue with webdriver")

# Function for auto scrolling down the page
def auto_scroll(driver):
    try:
        y = 1000
        time.sleep(2)
        for timer in range(0, 2):
            driver.execute_script("window.scrollTo(0, " + str(y) + ")")
            y += 2000
            time.sleep(0.5)
    except:
        print("Error with auto_scroll function")

# Function for scrolling to the bottom of the page immediately
def scroll_to_bottom(driver):
    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    except:
        print("Error with the scroll_to_bottom function")

# Function for web functions
def web_functions(driver):
    try:
        # Wait for the elements to load (you can use WebDriverWait for more advanced waiting)
        time.sleep(5)
        privacy_btn(driver)
        auto_scroll(driver)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Function will remove the privacy policy popup
def privacy_btn(driver):
    try:
        privacyBtn = driver.find_element(By.CSS_SELECTOR, 'button[class="lds__privacy-policy__btnClose"]')
        privacyBtn.click()
    except:
        print("Error with privacy button")

# Function will return the last page number of the called section
def last_page(driver):
    try:
        last_page_btn = driver.find_elements(By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button')
        last_page = int(last_page_btn[-2].text) # Grabbing second to last text value. -1 = last

        return last_page
    except:
        print(f"An error occurred: {str(e)}")