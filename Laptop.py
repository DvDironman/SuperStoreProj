from Products import Products

class Laptop(Products):
    def __init__(self,productid,brand,model,year,price,cpu,hard_disk,screen):
        super().__init__(productid,brand,model,year,price)
        self.cpu = cpu
        self.hard_disk = hard_disk
        self.screen = screen

    def Print_Me(self):
        super().Print_Me()
        print(f'cpu:{self.cpu}\nhard_disk:{self.hard_disk}\nscreen:{self.screen}')

    def __str__(self):
        return f'{super().__str__()},{self.cpu},{self.hard_disk},{self.screen}'

    def __repr__(self):
        return f'{super().__str__()},{self.cpu},{self.hard_disk},{self.screen}'

