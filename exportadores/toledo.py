from exportadores.exportadorBase import *


class ToledoExporter(Exporter):
    def format_product(self, product):
        code = product.code.zfill(6)
        product_type = product.product_type
        price = f"{int(float(product.price) * 100):06}"
        validity = product.validity or '000'
        description = product.description.ljust(50)

        # Campos adicionais
        department_association = "|01|"
        extra_info_code = "000000"
        image_code = "0000"
        nutrition_code = "000000"
        expiration_date_print = "0"
        packaging_date_print = "0"
        supplier_code = "0000"
        lot = "000000000000"
        ean_13_code = "00000000000"
        price_version = "0"
        sound_code = "0000"
        predetermined_tare_code = "0000"
        fracionator_code = "0000"
        extra_field_1 = "0000"
        extra_field_2 = "0000"
        conservation_code = "0000"
        ean_13_supplier = "000000000000"
        glaciamento_percent = "000000"
        department_association_sequence = "|01|"
        item_description_line_3 = " " * 35
        item_description_line_4 = " " * 35
        extra_field_3 = "000000"
        extra_field_4 = "000000"
        media_code = "000000"

        return f"{code}{product_type}{price}{validity}{description}{department_association}{extra_info_code}{image_code}{nutrition_code}{expiration_date_print}{packaging_date_print}{supplier_code}{lot}{ean_13_code}{price_version}{sound_code}{predetermined_tare_code}{fracionator_code}{extra_field_1}{extra_field_2}{conservation_code}{ean_13_supplier}{glaciamento_percent}{department_association_sequence}{item_description_line_3}{item_description_line_4}{extra_field_3}{extra_field_4}{media_code}0000000|0000|0||"
