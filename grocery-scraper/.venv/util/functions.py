from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

def initialize_driver():
    # Initialize the WebDriver
    driver = webdriver.Chrome()
    return driver

def auto_scroll(driver):
    y = 1000
    for timer in range(0, 9):
        driver.execute_script("window.scrollTo(0, " + str(y) + ")")
        y += 500
        time.sleep(1)

def auto_scroll_and_extract_prices(driver):
    # Open a webpage
    driver.get('https://www.atlanticsuperstore.ca/')

    # Wait for the elements to load (you can use WebDriverWait for more advanced waiting)
    time.sleep(5)
    privacyBtn = driver.find_element(By.CSS_SELECTOR, 'button[class="lds__privacy-policy__btnClose"]')
    privacyBtn.click()
    auto_scroll(driver)

    # Find elements with the attribute 'data-testid' set to 'price'
    elements = driver.find_elements(By.CSS_SELECTOR, 'p[data-testid="price"]')

    # Extract text from each price element and store it in a list
    prices = [element.text for element in elements]

    # Print the list of prices to the console
    for price in prices:
        if "sale" not in price.lower():
            print(price)

