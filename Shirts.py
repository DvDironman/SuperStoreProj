from Products import Products

class Shirts(Products):
    def __init__(self, productid, product_name, price, units_in_stock, brand="SuperStore", model="", year=2023):
        super().__init__(productid, brand, model, year, price)
        self.product_name = product_name
        self.units_in_stock = units_in_stock

    def Print_Me(self):
        super().Print_Me()
        print(f'product_name: {self.product_name}', f'\nunits_in_stock: {self.units_in_stock}')

    def __str__(self):
        return f'{self.productid},{self.brand},{self.model},{self.year},{self.price},{self.product_name},{self.units_in_stock}'



