from Products import Products

class Smartphone(Products):
    def __init__(self, product_id, brand, model, year, price, cell_net, num_cores, cam_res):
        super().__init__(product_id, brand, model, year, price)
        self.cell_net = cell_net
        self.num_cores = num_cores
        self.cam_res = cam_res

    def Print_Me(self):
        super().Print_Me()
        print(f'product_id:{self.cell_net}\nproduct_type:{self.num_cores}\nbrand:{self.cam_res}')

    def __str__(self):
        return f'{super().__str__()},{self.cell_net},{self.num_cores},{self.cam_res}'

    def __repr__(self):
        return str(self)

