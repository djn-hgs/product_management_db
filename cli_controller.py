import model

class ControllerCLI:
    def __init__(self, db_controller: 'ProductDbController', db_model: model.ProductDatabase):
        self.db_controller = db_controller
        self.db_model = db_model

    def mainloop(self):
        looping = True

        while looping:
            choices = {
                1: 'List all manufacturers',
                2: 'List all products',
                3: 'Add manufacturer',
                4: 'Add product',
                5: 'Delete manufacturer',
                6: 'Delete product',
                7: 'Quit'
            }

            for i in choices:
                print(f'{i} - {choices[i]}')

            choice_txt = input('Make a selection: ')

            if choice_txt.isdigit():
                choice = int(choice_txt)

                if choice == 1:
                    for i in self.db_controller.get_all_manufacturers():
                        print(i)
                elif choice == 2:
                    for i in self.db_controller.get_all_products():
                        print(i)
                elif choice == 3:
                    manufacturer = input('Manufacturer: ')
                    self.db_controller.add_manufacturer(manufacturer)
                elif choice == 4:
                    product = input('Product: ')
                    manufacturer = input('Manufacturer: ')
                    manufacturer_id_list = self.db_controller.get_manufacturer_id(manufacturer)
                    manufacturer_id = manufacturer_id_list.pop()
                    self.db_controller.add_product(product, manufacturer_id)
                elif choice == 5:
                    pass
                elif choice == 6:
                    pass
                elif choice == 7:
                    looping = False
                else:
                    print('Make another choice')

            else:
                print('Make another choice')

class ProductDbController:
    def __init__(self, model_name: model.ProductDatabase):
        self.model = model_name

    def add_manufacturer(self, manufacturer_name) -> [bool, int]:
        manufacturer_matches = self.model.get_manufacturer_id(manufacturer_name)

        if manufacturer_matches:
            present = True
            manufacturer_id = manufacturer_matches.pop()
        else:
            present = False
            manufacturer_id = self.model.add_manufacturer(manufacturer_name)

        return present, manufacturer_id

    def add_product(self, product_name, manufacturer_id) -> [bool, int]:
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

    def get_manufacturer_id(self, manufacturer_name) -> list[int]:
        return self.model.get_manufacturer_id(manufacturer_name)


if __name__ == '__main__':
    my_db = model.ProductDatabase()
    my_controller = ProductDbController(my_db)
    my_cli = ControllerCLI(my_controller, my_db)

    my_cli.mainloop()



