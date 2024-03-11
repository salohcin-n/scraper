from enum import Enum

class GroceryType(Enum):
    JUICE_AND_SMOOTHIES = 'juice & smoothies'
    HERBS = 'herbs'
    VEGETABLES = 'vegetables'
    FRUITS = 'fruits'
    DRIED_NUTS = 'dried fruits & nuts'
    FRESH_CUT = 'fresh cut fruits & veggies'
    SALAD_DRESSING = 'packaged salad dressings'
    SALADS = 'in-store salads'

# Example usage:
# print(GroceryType.JUICE_AND_SMOOTHIES.value)  # Output: juice & smoothies