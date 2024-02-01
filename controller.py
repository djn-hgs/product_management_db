import model


class ProductDbController:
    def __init__(self, model_name: model.ProductDatabase):
        self.model = model_name

    def add_manufacturer(self, manufacturer_name):
        manufacturer_matches = self.model.get_manufacturer_id(manufacturer_name)

        if manufacturer_matches:
            present = True
            manufacturer_id = manufacturer_matches.pop()
        else:
            present = False
            manufacturer_id = self.model.add_manufacturer(manufacturer_name)

        return present, manufacturer_id

    def add_product(self, product_name, manufacturer_id):
        product_matches = self.model.get_product_id(product_name)

        if product_matches:
            present = False
            product_id = product_matches.pop()
        else:
            present = True
            product_id = self.model.add_product(product_name, manufacturer_id)

        return present, product_id

    def get_all_manufacturers(self):
        return self.model.get_all_manufacturers()

    def get_all_products(self):
        return self.model.get_all_products()

if __name__ == '__main__':
    my_db = model.ProductDatabase()
    my_controller = ProductDbController(my_db)

    apple_present, apple_id = my_controller.add_manufacturer('Apple')
    microsoft_present, microsoft_id = my_controller.add_manufacturer('Microsoft')

    macbook_present, macbook_id = my_controller.add_product('Macbook', manufacturer_id=apple_id)
    iphone_present, iphone_id = my_controller.add_product('iPhone', manufacturer_id=apple_id)
    surface_present, surface_id = my_controller.add_product('Surface', manufacturer_id=microsoft_id)

    print(my_controller.get_all_manufacturers())
    print(my_controller.get_all_products())
