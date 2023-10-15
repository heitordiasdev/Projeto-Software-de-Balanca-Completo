from exportadores.filizola import filizolaLayout
from exportadores.filizola.filizolaLayout import FilizolaExporter
from exportadores.toledo.toledoLayout import ToledoExporter
from exportadores.urano.uranoLayout import UranoExporter
from produtos.produto import Product

products = [
        Product("000270", "P", "QUEIJO GRUYERE KG", "21.90"),
        Product("000288", "P", "QUEIJO PROVOLETE KG", "12.29")
    ]

filizola_exporter = FilizolaExporter("CADTXT.TXT")
toledo_exporter = ToledoExporter("ITENSMGV.TXT")
urano_exporter = UranoExporter("PRODUTOS.TXT")

filizola_exporter.export(products)
toledo_exporter.export(products)
urano_exporter.export(products)