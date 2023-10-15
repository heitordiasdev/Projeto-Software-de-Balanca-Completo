from exportadores.exportadorBase import *


class FilizolaExporter(Exporter):
    def format_product(self, product):
        code = product.code.zfill(6)
        product_type = product.product_type
        description = product.description.ljust(22)
        price = f"{int(float(product.price) * 100):07}"
        validity = product.validity or '000'
        return f"{code}{product_type}{description}{price}{validity}"
