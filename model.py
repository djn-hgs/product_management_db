import sqlite3


class ProductDatabase:
    def __init__(self, filename='productdb.sqlite3'):
        self.filename = filename

        self.connection = sqlite3.connect(filename)

        self.cursor = self.connection.cursor()

        self.initialise_tables()

    def get_products(self):
        all_products_query = 'SELECT * FROM Product'

        self.cursor.execute(all_products_query)

        print(self.cursor.fetchall())

    def initialise_tables(self):
        tables_query = 'SELECT name FROM sqlite_master WHERE type="table";'

        self.cursor.execute(tables_query)
        all_tables = self.cursor.fetchall()

        print(all_tables)

        if ('Product',) not in all_tables:
            product_ddl = ('CREATE TABLE Product'
                           '('
                           'ProductID INTEGER PRIMARY KEY AUTOINCREMENT,'
                           'ProductName STRING,'
                           'ManufacturerID INTEGER'
                           ');'
                           )

            self.cursor.execute(product_ddl)

        if ('Manufacturer',) not in all_tables:
            manufacturer_ddl = ('CREATE TABLE Manufacturer'
                                '('
                                'ManufacturerID INTEGER PRIMARY KEY AUTOINCREMENT,'
                                'ManufacturerName STRING'
                                ');'
                                )

            self.cursor.execute(manufacturer_ddl)

        self.cursor.execute(tables_query)
        all_tables = self.cursor.fetchall()

        print(all_tables)

        self.connection.commit()

    def get_manufacturer_id(self, name):
        id_match_query = 'SELECT ManufacturerID FROM Manufacturer WHERE ManufacturerName = ?'

        self.cursor.execute(id_match_query, (name,))

        id_matches = self.cursor.fetchall()

        if id_matches:
            return [a for (a,) in id_matches]

    def add_manufacturer(self, name):
        add_manufacturer_query = 'INSERT INTO Manufacturer (ManufacturerName) VALUES (?)'

        self.cursor.execute(add_manufacturer_query, (name,))

        self.connection.commit()

        return self.cursor.lastrowid

    def add_product(self, product_name, manufacturer_id):
        add_product_query = 'INSERT INTO Product (ProductName, ManufacturerID) VALUES (?, ?)'

        self.cursor.execute(add_product_query, (product_name, manufacturer_id))

        self.connection.commit()

        return self.cursor.lastrowid

    def get_product_id(self, product_name):
        id_match_query = 'SELECT ProductID FROM Product WHERE ProductName = ?'

        self.cursor.execute(id_match_query, (product_name,))

        id_matches = self.cursor.fetchall()

        if id_matches:
            return [a for (a,) in id_matches]

    def get_all_manufacturers(self):
        all_manufacturer_query = 'SELECT ManufacturerID, ManufacturerName FROM Manufacturer;'

        self.cursor.execute(all_manufacturer_query)

        all_manufacturer_list = self.cursor.fetchall()

        return [
            {'ManufacturerID': manufacturer_id, 'ManufacturerName': manufacturer_name}
            for manufacturer_id, manufacturer_name in all_manufacturer_list
        ]

    def get_all_products(self):
        all_product_query = 'SELECT ProductID, ProductName, ManufacturerID FROM Product;'

        self.cursor.execute(all_product_query)

        all_product_list = self.cursor.fetchall()

        return [
            {'ProductID': product_id, 'ProductName': product_name, 'ManufacturerID': manufacturer_id}
            for product_id, product_name, manufacturer_id in all_product_list
        ]


if __name__ == '__main__':
    my_db = ProductDatabase()



    apple_id = my_db.add_manufacturer('Apple')

    print(my_db.get_manufacturer_id('Apple'))

    my_db.add_product('Macbook', manufacturer_id=apple_id)

    