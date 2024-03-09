# Import all the scraper classes
from models.fruits_vegetables.fresh_vegetables import FreshVeggieExtractor
from models.fruits_vegetables.fresh_fruits import FreshFruitExtractor
from models.fruits_vegetables.packaged_salad import PackagedSaladAndDressingsExtractor
from models.fruits_vegetables.herbs import HerbExtractor
from models.fruits_vegetables.fresh_cut import FreshCutProduceExtractor
from models.fruits_vegetables.dried_fruits_nuts import DriedFruitsAndNutsExtractor

# Define a list of all scraper classes
SCRAPERS = [
    FreshVeggieExtractor(),
    FreshFruitExtractor(),
    PackagedSaladAndDressingsExtractor(),
    HerbExtractor(),
    FreshCutProduceExtractor(),
    DriedFruitsAndNutsExtractor()
]
