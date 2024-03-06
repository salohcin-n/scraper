import time
from models.fruits_vegetables.fresh_vegetables import FreshVeggieExtractor
from models.fruits_vegetables.fresh_fruits import FreshFruitExtractor
from models.fruits_vegetables.packaged_salad import PackagedSaladAndDressingsExtractor
from models.fruits_vegetables.herbs import HerbExtractor
from data.data import printData

def main():
    try:
        # # Create an instance of a model
        # herb_extractor = HerbExtractor()
        #
        # # Run the extraction process
        # herb_extractor.run()

        # Create instances of the scrapers
        scrapers = [
            FreshVeggieExtractor(),
            FreshFruitExtractor(),
            PackagedSaladAndDressingsExtractor()
        ]

        # Run each scraper
        for scraper in scrapers:
            scraper.run()

        # Check the function for errors before running.
        # Uncomment this line to print data to the console -for testing -may DELETE/DROP tables
        # printData()
    except:
        print("Issue with main scraper run")

if __name__ == "__main__":
    main()
