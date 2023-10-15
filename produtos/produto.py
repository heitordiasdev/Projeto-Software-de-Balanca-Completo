class Product:
    def __init__(self, code, product_type, description, price, validity=None):
        self.code = code
        self.product_type = product_type
        self.description = description
        self.price = price
        self.validity = validity