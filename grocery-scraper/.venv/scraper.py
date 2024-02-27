from models.fruits_vegetables.fresh_vegetables import FreshVeggieExtractor
from models.fruits_vegetables.fresh_fruits import FreshFruitExtractor

def main():
    try:
        # Create an instance of a model
        veggie_extractor = FreshVeggieExtractor()
        fruit_extractor = FreshFruitExtractor()

        # Run the extraction process
        veggie_extractor.run()
        fruit_extractor.run()

    except:
        print("Issue with main scraper run")

if __name__ == "__main__":
    main()
