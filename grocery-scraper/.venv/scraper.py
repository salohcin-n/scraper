import time
from util.scraper_run import FRUIT_AND_VEGGIE_SCRAPERS, MEAT_SCRAPERS
from data.data import printData

def main():
    try:
        # Run each scraper
        # for scraper_instance in FRUIT_AND_VEGGIE_SCRAPERS:
        #     scraper_instance.run()

        # Running the meat scrapers
        for scraper_instance in MEAT_SCRAPERS:
            scraper_instance.run()

        # Check the function for errors before running.
        # Uncomment this line to print data to the console -for testing -may DELETE/DROP tables
        # printData()
    except:
        print("Issue with main scraper run")

if __name__ == "__main__":
    main()
