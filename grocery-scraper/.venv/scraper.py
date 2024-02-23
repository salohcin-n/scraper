from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open a webpage
driver.get('https://www.atlanticsuperstore.ca/')

# Wait for the elements to load (you can use WebDriverWait for more advanced waiting)
time.sleep(5)
privacyBtn = driver.find_element(By.CSS_SELECTOR, 'button[class="lds__privacy-policy__btnClose"]')
privacyBtn.click()

y = 1000
for timer in range(0,5):
     driver.execute_script("window.scrollTo(0, "+str(y)+")")
     y += 500
     time.sleep(3)

# Scroll into view of the elements
# scrollIntoView = driver.find_element(By.CSS_SELECTOR, 'div[data-testid="mini-product-tile-carousel-header"]')
# driver.execute_script("arguments[0].scrollIntoView();", element)

# Find elements with the attribute 'data-testid' set to 'price'
elements = (driver.find_elements(By.CSS_SELECTOR, 'p[data-testid="price"]'))

# Extract text from each price element and store it in a list
prices = [element.text for element in price_elements]

# Close the browser
driver.quit()

# Print the list of prices to the console
for price in prices:
    print(price)







