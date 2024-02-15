# Checkout System
This checkout system is designed to handle a shopping cart where items can be added, and promotions can be applied to those items to calculate the total price. It supports fixed discount promotions, unit price discount promotions, and promotions that add free items to the cart.

## Installation
Ensure you have Python installed on your system. This project was developed using Python 3.8, but it should be compatible with most Python 3.x versions.

## Running the Tests
To run the tests, navigate to the project directory where the test file is located (repo root - test_checkout.py and run,
  python3 test_checkout.py

## Using the Checkout System
To use the Checkout class in your own project, you'll need to import the necessary classes from their respective modules. Here's a quick example of how you can set up the checkout system, add items to the cart, and calculate the total price with promotions applied:

from checkout import Checkout
from models.product import Sku
from models.promotion import FreeItemPromotion, PriceModifierPromotion

### Define your SKUs
skus = {
    'ipd': Sku('ipd', 'Super iPad', 549.99),
    'mbp': Sku('mbp', 'MacBook Pro', 1399.99),
    'atv': Sku('atv', 'Apple TV', 109.50),
    'vga': Sku('vga', 'VGA adapter', 30.00),
}

### Define your promotions
promotions = {
    'atv': PriceModifierPromotion('atv', 3, 109.50, "fixed_discount"),
    'ipd': PriceModifierPromotion('ipd', 5, 50, "unit_price_discount"),
    'mbp': FreeItemPromotion('mbp', 1, 'vga'),
}

### Initialize the checkout system
checkout = Checkout(skus, promotions)

### Scan items
checkout.scan('atv')
checkout.scan('mbp')
checkout.scan('ipd')

### Print the total
print(f"Total price: ${checkout.total()}")

