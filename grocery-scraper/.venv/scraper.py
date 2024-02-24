from util.functions import initialize_driver, auto_scroll_and_extract_prices

# Initialize the WebDriver
driver = initialize_driver()

# Open a webpage and perform actions
auto_scroll_and_extract_prices(driver)

# Close the browser
driver.quit()

