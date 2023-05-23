import csv

from Products import Products
from Clients import Clients
from Laptop import Laptop
from Smartphone import Smartphone
from Shirts import Shirts
from Order import Order
from Errors_and_Exceptions import ClientNotFoundError
from Errors_and_Exceptions import ShirtNotFoundError

class Superstore:

    def __init__(self,productfile,clientfile,orderlist,shirts):
        self.prodlist=[]
        self.clntlist=[]
        self.orderlist=[]

        with open(productfile) as product_file:
            prod = csv.reader(product_file)
            next(prod)
            for row in prod:
                productid = int(row[0])
                brand = row[2]
                model = row[3]
                year = int(row[4])
                price = int(row[5])
                if row[1] == "laptop":
                    cpu=row[6]
                    hard_disk=row[7]
                    screen=row[8]
                    p=Laptop(productid, brand, model, year, price,cpu,hard_disk,screen)
                    self.prodlist.append(p)
                elif row[1]=="smartphone":
                    cell_net=row[9]
                    num_cores=row[10]
                    cam_res=row[11]
                    p = Smartphone(productid,brand, model, year, price,cell_net,num_cores,cam_res)
                    self.prodlist.append(p)
                else:
                    p=Products(productid, brand, model, year, price)
                    self.prodlist.append(p)




        with open(clientfile) as client_file:
            clnt=csv.reader(client_file)

            next(clnt)
            for row in clnt:
                clientid=int(row[0])
                name=row[1]
                email=row[2]
                address=row[3]
                phonenum=int(row[4])
                gender=row[5]
                c=Clients(clientid,name,email,address,phonenum,gender)
                self.clntlist.append(c)

        with open(shirts) as sf:
            shrt = csv.reader(sf)
            next(shrt)
            for row in shrt:
                productid=int(row[0])
                product_name=row[1]
                price=int(row[2])
                units_in_stock=int(row[3])
                s=Shirts(productid, product_name, price, units_in_stock)
                self.prodlist.append(s)

        with open(orderlist) as order_file:
            order_file = csv.reader(order_file)
            next(order_file)
            for row in order_file:
                order_id=int(row[0])
                client_id=int(row[1])
                product_id=int(row[2])
                quantity=int(row[3])
                o=Order(order_id, client_id, product_id, quantity)
                self.orderlist.append(o)

    def Print_Products(self):
        print(f'productid, producttype, brand, model, year, price')
        for row in self.prodlist:
            print(row)

    def Get_Product(self,product_id):
        for i in self.prodlist:
            if i.productid == product_id:
                return i
        return None

    def Add_Product(self,p):
        for row in self.prodlist:
            if row.productid==p.productid:
                return False
        self.prodlist.append(p)
        return True

    def Remove_Product(self,prodid):
        for row in self.prodlist:
            if row.productid==prodid:
                self.prodlist.remove(row)
                return True
        return False

    def Get_All_By_Brand(self,brand):
        newlist=[]
        for row in self.prodlist:
            if row.brand==brand:
                newlist.append(str(row))
        return newlist

    def Get_All_By_Price_Under(self,max):
        maxlist=[]
        for row in self.prodlist:
            if row.price < max:
                maxlist.append(str(f'{row}\n'))
        return maxlist

    def Get_Most_Expensive_Product(self):
        max1=0
        max2=''
        for row in self.prodlist:
            if max1 < row.price:
                max2=row
            return max2

    def Print_Clients(self):
        print(f'clientid, name, email, address, phone num, gender')
        for row in self.clntlist:
            print(row)

    def Get_Client(self,idclient):
        for i in self.clntlist:
            if i.clientid == idclient:
                return i
        return None

    def Add_Client(self,c):
        for row in self.clntlist:
            if row.clientid==c.clientid:
                return False
            self.clntlist.append(c)
        return True

    def Remove_Client(self,clntid):
        for row in self.clntlist:
            if row.clientid==clntid:
                self.clntlist.remove(row)
                return True
        return False

    def Get_All_Phones(self):
        sp=[]
        for row in self.prodlist:
            if type(row).__name__=="Smartphone":
                sp.append(row)
        return sp


    def Get_All_Laptops(self):
        l=[]
        for row in self.prodlist:
            if type(row).__name__=="Laptop":
                l.append(row)
        return l

    def Phone_Avg_Price(self):
        avg=self.Get_All_Phones()
        sum=0
        c=0
        for row in avg:
            c=c+1
            sum=sum+row.price
        return sum/c

    def Get_Max_Screen(self):
        max1=self.Get_All_Laptops()
        max2=0
        for row in max1:
            if int(row.screen) >= int(max2) :
                max2=row.screen
        return max2

    def Get_Common_Cam(self):
        counter=0
        freq=None
        for row in self.Get_All_Phones() :
            if self.Get_All_Phones().count(row)>counter:
                counter = self.Get_All_Phones().count(row)
                freq=row.cam_res
        return freq

    def List_Popular(self):
        popular=[]
        for row in self.prodlist:
            if row.Is_Popular()==True:
                popular.append(row)
        return popular

    def __iadd__(self, other):
        for row in self.prodlist:
            if row.productid == other.product_id:
                return False
        else:
            self.prodlist.append(other)
            return True

    def Get_shirt(self,s_id):
        for row in self.prodlist:
            if type(row).__name__ =="Shirts" and row.productid == s_id:
                return row
        else:
            return None

    def Get_Max_Order_Id(self):
        max=0
        for row in self.orderlist:
            if row.order_id>=max:
                max=row.order_id
        return max

    def Add_Order(self, clientid_lst, productid_lst, quantity_lst):
        orderid = int(self.Get_Max_Order_Id())+1
        try:
            clientid=[]
            productid=[]
            for row in self.clntlist:
                clientid.append(row.clientid)
            if clientid_lst not in  clientid:
                raise ClientNotFoundError
            for row in self.prodlist:
                productid.append(row.productid)
            if productid_lst not in productid:
                raise ShirtNotFoundError

            for row in self.prodlist:
                if type(row)==Laptop or type(row)==Smartphone:
                    if quantity_lst>1:
                        raise ValueError
                    else:
                        if quantity_lst>row.units_in_stock:
                            raise ValueError

        except ClientNotFoundError:
            return "client not in list"

        except ShirtNotFoundError:
            return "product not in list"

        except ValueError:
            return"value error"

        n_order=Order(orderid,clientid_lst,productid_lst,quantity_lst)
        self.orderlist.append(n_order)
        return "order approved!"