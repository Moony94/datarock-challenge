class Sku:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price

class CartItem:
    def __init__(self, sku, quantity=1, promotion=None):
        self.sku = sku
        self.quantity = quantity
        self.promotion = promotion
