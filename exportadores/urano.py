from exportadores.exportadorBase import *


class UranoExporter(Exporter):
    def format_product(self, product):
        code = product.code.zfill(6)
        product_type = product.product_type
        description = product.description.ljust(20)
        price = f"{int(float(product.price) * 1000):09}"
        validity = (product.validity or '000') + 'D'
        return f"{code}*{product_type}{description}{price}{validity}"
