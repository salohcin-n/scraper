from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from models.base import PriceExtractor, TitleExtractor
import time
import threading

def timer():
    start_time = time.time()  # Get the current time in seconds since the epoch

    try:
        while True:
            elapsed_time = time.time() - start_time
            print(f"Timer: {int(elapsed_time)} seconds elapsed", end='\r')
            time.sleep(1)  # Sleep for 1 second
    except KeyboardInterrupt:
        # Handle KeyboardInterrupt (Ctrl+C)
        print("\nTimer stopped.")

class TimerThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def run(self):
        start_time = time.time()
        while not self._stop_event.is_set():
            elapsed_time = time.time() - start_time
            print(f"Timer: {int(elapsed_time)} seconds elapsed", end='\r')
            time.sleep(1)


# Initializing Chrome Web Driver
def initialize_driver(url):
    # Global varible to toggle headless mode, not implemented yet.
    # global HEADLESS_MODE
    try:
        # Set Chrome options to run headless
        chrome_options = Options()
        # chrome_options.add_argument("--headless")  # Run Chrome in headless mode
        # chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration, sometimes necessary in headless mode
        # chrome_options.add_argument("--no-sandbox")  # Bypass OS security model

        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        return driver
    except WebDriverException as e:
        print("Issue with webdriver:", e)
        return None
    except Exception as e:
        print("An unexpected error occurred:", e)
        return None

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
        survey_btn(driver)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Function will remove the privacy policy popup
def privacy_btn(driver):
    try:
        privacyBtn = driver.find_element(By.CSS_SELECTOR, 'button[class="lds__privacy-policy__btnClose"]')
        privacyBtn.click()
    except:
        print("Error with privacy button")

# Function will close the survey window if prompt appears
def survey_btn(driver):
    try:
        closeSurveyBtn = driver.find_elements(By.CSS_SELECTOR, 'button[aria-label="Close Survey"]')

        if closeSurveyBtn:
            closeSurveyBtn[0].click()
    except:
        print("Error with closing the survey prompt")

# Function will return the last page number of the called section
def last_page(driver):
    try:
        last_page_btn = driver.find_elements(By.CSS_SELECTOR, 'nav[aria-label="Pagination"] > button')
        last_page = int(last_page_btn[-2].text) # Grabbing second to last text value. -1 = last

        return last_page
    except:
        print(f"An error occurred: {str(e)}")