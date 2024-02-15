from abc import ABC, abstractmethod

class Promotion(ABC):
    def __init__(self, sku, min_quantity):
        self.sku = sku
        self.min_quantity = min_quantity
    
    @abstractmethod
    def apply(self, count):
        pass

class FreeItemPromotion(Promotion):
    def __init__(self, sku, min_quantity, free_item_sku):
        super().__init__(sku, min_quantity)
        self.free_item_sku = free_item_sku
    
    def apply(self, count):
        if count >= self.min_quantity:
            return self.free_item_sku
        return None

class PriceModifierPromotion(Promotion):
    def __init__(self, sku, min_quantity, discount_value, discount_type="fixed_discount"):
        super().__init__(sku, min_quantity)
        self.discount_value = discount_value
        self.discount_type = discount_type  # "fixed_discount" or "unit_price_discount"
    
    def apply(self, count):
        if count >= self.min_quantity:
            if self.discount_type == "fixed_discount":
                return self.discount_value  # Fixed amount off the total
            elif self.discount_type == "unit_price_discount":
                return self.discount_value * count
        return None

