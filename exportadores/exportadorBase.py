class Exporter:
    def __init__(self, filename):
        self.filename = filename

    def export(self, products):
        with open(self.filename, 'w') as file:
            for product in products:
                try:
                    file.write(self.format_product(product) + '\n')
                except ValueError as e:
                    # Tratamento de exceção para preços inválidos
                    print(f"Erro ao exportar o produto {product.code}: {e}")
                except Exception as e:
                    # Tratamento de exceção genérica
                    print(f"Erro inesperado ao exportar o produto {product.code}: {e}")

    def format_product(self, product):
        pass
