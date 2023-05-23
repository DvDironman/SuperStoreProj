class Products:

    def __init__(self,productid,brand,model,year,price):
        self.productid=productid
        self.brand=brand
        self.model=model
        self.year=year
        self.price=price
        if len(str(self.year))!=4:
            self.year="null"
        if price<0:
            self.price=0

    def Print_Me(self):
        print(f'product_id:{self.productid}\nbrand:{self.brand}\nmodel:{self.model}\nyear:{self.year}\nprice:{self.price}')

    def __str__(self):
        return f'{self.productid},{self.brand},{self.model},{self.year},{self.price}'

    def __repr__(self):
        return str(self)

    def Is_Popular(self):
            if int(self.year) > 2017 and int(self.price) < 3000:
                return True
            return False



