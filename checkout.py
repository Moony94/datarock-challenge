from models.product import CartItem
from models.promotion import FreeItemPromotion, PriceModifierPromotion

class Checkout:
    def __init__(self, skus, promotions):
        self.skus = skus
        self.promotions = promotions
        self.cart = {}
        
    def scan(self, sku_code):
        if sku_code in self.cart:
            self.cart[sku_code].quantity += 1
        else:
            sku = self.skus.get(sku_code, None)
            promotion = self.promotions.get(sku_code, None)
            if sku:
                self.cart[sku_code] = CartItem(sku, 1, promotion)
            else:
                print(f"Sku with code {sku_code} not found.")

    def total(self):
        total_price = 0
        for sku, cart_item in self.cart.items():
            subtotal = cart_item.sku.price * cart_item.quantity

            if cart_item.promotion:
                if isinstance(cart_item.promotion, FreeItemPromotion):
                    free_item_sku = cart_item.promotion.apply(cart_item.quantity)
                    if free_item_sku:
                        self.scan(free_item_sku) # Add the free item to the cart
                elif isinstance(cart_item.promotion, PriceModifierPromotion):
                    discount = cart_item.promotion.apply(cart_item.quantity)
                    if discount:
                        subtotal -= discount

            total_price += subtotal

        return round(total_price, 2)



