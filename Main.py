from Superstore import Superstore
from Products import Products
from Clients import Clients
from Shirts import Shirts
from Errors_and_Exceptions import ClientNotFoundError
from Errors_and_Exceptions import ShirtNotFoundError

sstore=Superstore('products_supply.csv','clients.csv','orders.csv','shirts.csv')

def Func15():
    shirt_lst = []
    for row in sstore.prodlist:
        if type(row) == Shirts:
            shirt_lst.append(row)
    return shirt_lst

def Menu():
    print("---MENU---\n"
          "1. Print all products\n"
          "2. Print all clients\n"
          "3. Add new product to the store\n"
          "4. Add new client to  the store\n"
          "5. Remove product\n"
          "6. Remove client\n"
          "7. Print all products under price\n"
          "8. Print the most expensive product\n"
          "9.print smartphone list\n"
          "10.print laptop list\n"
          "11. print average phone price\n"
          "12. print largest laptop screen\n"
          "13. print common camera resolution\n"
          "14. print popular products\n"
          "15. Print all shirts \n"
          "16. add new order \n"
          "17. Print all orders \n"
          "18. EXIT\n")
    option=int(input("select  option"))
    while option!=18:
        if option==1:
            Superstore.Print_Products(sstore)
        elif option==2:
            Superstore.Print_Clients(sstore)
        elif option==3:
            productid=int(input("insert digit product id"))
            brand=input("insert product brand")
            model=input("insert product model")
            year=int(input("insert 4 digit product year"))
            price=float(input("insert product price"+" "+"NIS"))
            p=Products(productid,brand,model,year,price)
            x=sstore.Add_Product(p)
            if x==True:
                print('new product added')
            else:
                print('product already exists')
        elif option==4:
            id=int(input("insert 5 digit id"))
            name=input("insert client name")
            email=input("insert client email")
            address=input("insert client address")
            phonenum=int(input("insert 10 digit phone number"))
            gender=input("insert client gender (M/F)")
            c=Clients(id,name,email,address,phonenum,gender)
            x=sstore.Add_Client(c)
            if x==True:
                print('new client added')
            else:
                print('client already exists')
        elif option==5:
            id=int(input("insert id of product you wish to remove"))
            x=sstore.Remove_Product(id)
            if x==True:
                print('product deleted')
            else:
                print('product does not exist')
        elif option==6:
            id=int(input("insert id of client you wish to remove"))
            x=sstore.Remove_Client(id)
            if x==True:
                print('client deleted')
            else:
                print('client does not exist')
        elif option==7:
            max=int(input("insert amount you want to spend"))
            print(f"all products cheaper than your price is:\n{sstore.Get_All_By_Price_Under(max)}")
        elif option==8:
            print(f"product with the highest price is:\n{sstore.Get_Most_Expensive_Product()}")
        elif option==9:
            print(f'{sstore.Get_All_Phones()}')
        elif option==10:
            print(f'{sstore.Get_All_Laptops()}')
        elif option==11:
            print(f'Phone avg price is: {sstore.Phone_Avg_Price()}')
        elif option==12:
            print(f'largest screen is:{sstore.Get_Max_Screen()}')
        elif option==13:
            print(f'common camera resolution is:{sstore.Get_Common_Cam()}')
        elif option==14:
            print(f'popular product is: {sstore.List_Popular()}')
        elif option==15:
            x=Func15()
            for row in x:
               print(row)
        elif option==16:
            cid= int(input("insert a client id:"))
            pid= int(input("insert a product id:"))
            q= int(input("insert quantity:"))
            try:
                 sstore.Add_Order(cid, pid, q)
            except ClientNotFoundError as e:
                 print("error call costumer service:", e)
            except ShirtNotFoundError as e:
                 print("error call costumer service:", e)
            except ValueError as e:
                  print("error call costumer service:", e)
        elif option==17:
            print("printing orders")
            for row in sstore.orderlist:
                print(row)

        print("---MENU---\n"
            "1. Print all products\n"
            "2. Print all clients\n"
            "3. Add new product to the store\n"
            "4. Add new client to  the store\n"
            "5. Remove product\n"
            "6. Remove client\n"
            "7. Print all products under price\n"
            "8. Print the most expensive product\n"
            "9. print smartphone list\n"
            "10.print laptop list\n"
            "11. print average phone price\n"
            "12. print largest laptop screen\n"
            "13. print common camera resolution\n"
            "14. print popular products\n"
            "15. Print all shirts \n"
            "16. add new order \n"
            "17. Print all orders \n"
            "18. EXIT\n")
        option = int(input("select  option"))
    print("thank you for shopping with superstore, have a nice day")
Menu()


