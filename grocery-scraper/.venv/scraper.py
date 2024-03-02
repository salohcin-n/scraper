import time
from models.fruits_vegetables.fresh_vegetables import FreshVeggieExtractor
from models.fruits_vegetables.fresh_fruits import FreshFruitExtractor
from models.fruits_vegetables.packaged_salad import PackagedSaladAndDressingsExtractor
from data.data import printData

def main():
    try:
        # Create an instance of a model
        veggie_extractor = FreshVeggieExtractor()
        fruit_extractor = FreshFruitExtractor()
        packaged_salad_extractor = PackagedSaladAndDressingsExtractor()


        # Run the extraction process
        veggie_extractor.run()
        fruit_extractor.run()
        packaged_salad_extractor.run()

        # Uncomment this line to print data to the console -for testing
        # printData()
    except:
        print("Issue with main scraper run")

if __name__ == "__main__":
    main()
