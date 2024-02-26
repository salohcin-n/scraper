from models.vegetables.fresh import FreshExtractor

def main():
    try:
        # Create an instance of a model
        extractor = FreshExtractor()

        # Run the extraction process
        extractor.run()
    except:
        print("Issue with main scraper run")

if __name__ == "__main__":
    main()
