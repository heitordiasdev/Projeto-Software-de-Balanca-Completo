class Exporter:
    def __init__(self, filename):
        self.filename = filename

    def export(self, products):
        with open(self.filename, 'w') as file:
            for product in products:
                file.write(self.format_product(product) + '\n')

    def format_product(self, product):
        pass