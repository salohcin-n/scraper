# Import all the scraper classes
from models.fruits_vegetables.fresh_vegetables import FreshVeggieExtractor
from models.fruits_vegetables.fresh_fruits import FreshFruitExtractor
from models.fruits_vegetables.packaged_salad import PackagedSaladAndDressingsExtractor
from models.fruits_vegetables.herbs import HerbExtractor
from models.fruits_vegetables.fresh_cut import FreshCutProduceExtractor
from models.fruits_vegetables.dried_fruits_nuts import DriedFruitsAndNutsExtractor
from models.fruits_vegetables.in_store_salads import InStoreSaladsExtractor
from models.fruits_vegetables.fresh_juice_smoothie import FreshJuiceAndSmoothiesExtractor
from models.meat.chicken_turkey import ChickenTurkeyExtractor

# Define a list of all scraper classes
FRUIT_AND_VEGGIE_SCRAPERS = [
    FreshVeggieExtractor(),
    FreshFruitExtractor(),
    PackagedSaladAndDressingsExtractor(),
    HerbExtractor(),
    FreshCutProduceExtractor(),
    DriedFruitsAndNutsExtractor(),
    InStoreSaladsExtractor(),
    FreshJuiceAndSmoothiesExtractor()
]

MEAT_SCRAPERS = [
    ChickenTurkeyExtractor()
]
