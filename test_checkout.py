from checkout import Checkout
from models.product import Sku
from models.promotion import FreeItemPromotion, PriceModifierPromotion

# Define skus
skus = {
    'ipd': Sku('ipd', 'Super iPad', 549.99),
    'mbp': Sku('mbp', 'MacBook Pro', 1399.99),
    'atv': Sku('atv', 'Apple TV', 109.50),
    'vga': Sku('vga', 'VGA adapter', 30.00),
}

# Define promotions
promotions = {
    'atv': PriceModifierPromotion(
        sku='atv',
        min_quantity=3,
        discount_value=109.50,  # For every 3 ATVs, one is free
        discount_type="fixed_discount"
    ),
    'ipd': PriceModifierPromotion(
        sku='ipd',
        min_quantity=5,
        discount_value=50,
        discount_type="unit_price_discount"
    ),
    'mbp': FreeItemPromotion(
        sku='mbp',
        min_quantity=1,
        free_item_sku='vga'
    ),
}

def assert_equal(actual, expected, message):
    if actual == expected:
        print(f"PASS: {message}")
    else:
        print(f"FAIL: {message}. Expected {expected}, got {actual}")

def test_adding_items_to_cart():
    checkout = Checkout(skus, promotions)
    checkout.scan('atv')
    checkout.scan('ipd')

    assert_equal(len(checkout.cart), 2, "Adding items to cart")

def test_price_modifier_promotion_fixed_discount_atv():
    checkout = Checkout(skus, promotions)
    checkout.scan('atv')
    checkout.scan('atv')
    checkout.scan('atv')  # Apply fixed discount for 3 ATVs

    expected_total = round(skus['atv'].price * 2, 2)  # Price for 2 ATVs, third is free (discount applied)
    assert_equal(checkout.total(), expected_total, "Fixed discount promotion for ATV")

def test_price_modifier_promotion_unit_price_discount_ipd():
    checkout = Checkout(skus, promotions)
    for _ in range(5):
        checkout.scan('ipd')  # Apply unit price discount for iPads

    expected_total = round((skus['ipd'].price - 50) * 5, 2)  # Price for 5 iPads with discount per unit
    assert_equal(checkout.total(), expected_total, "Unit price discount promotion for IPD")

def test_free_item_promotion_mbp():
    checkout = Checkout(skus, promotions)
    checkout.scan('mbp')  # Add MacBook Pro and get a free VGA adapter
    
    expected_total = skus['mbp'].price  # Only price for MacBook Pro, VGA adapter is free
    assert_equal(checkout.total(), expected_total, "Free item promotion for MBP")
    assert_equal('vga' in checkout.cart, True, "VGA adapter added to cart")
    assert_equal(checkout.cart['vga'].quantity, 1, "Correct quantity of VGA adapter")

def test_calculating_total():
    checkout = Checkout(skus, promotions)

    # Scan 5 'ipd's with unit price discount
    for _ in range(5):
        checkout.scan('ipd')
    # Scan 3 'atv's with a 3 for 2 deal
    for _ in range(3):
        checkout.scan('atv')
    
    # Calculate expected total
    expected_ipd_total = (skus['ipd'].price - 50) * 5  # Discount applied to all 5 'ipd's
    expected_atv_total = skus['atv'].price * 2  # Only 2 'atv's are charged due to the 3 for 2 deal
    expected_total = expected_ipd_total + expected_atv_total

    # Calculate actual total
    actual_total = checkout.total()
    
    # Assert total is not negative and matches expected total
    assert_equal(actual_total, expected_total, "Actual total matches expected total after applying promotions")

def run_tests():
    test_adding_items_to_cart()
    test_price_modifier_promotion_fixed_discount_atv()
    test_price_modifier_promotion_unit_price_discount_ipd()
    test_free_item_promotion_mbp()
    test_calculating_total()

if __name__ == "__main__":
    run_tests()
