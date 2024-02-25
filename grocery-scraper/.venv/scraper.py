from models.vegetables.fresh import FreshExtractor

def main():
    # Create an instance of a model
    extractor = FreshExtractor()

    # Run the extraction process
    extractor.run()

if __name__ == "__main__":
    main()
