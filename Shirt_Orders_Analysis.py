import numpy as np
import matplotlib.pyplot as plt
from Superstore import Superstore
from Errors_and_Exceptions import ClientNotFoundError

my_SuperStore = Superstore("products_supply.csv", "clients.csv","orders.csv","shirts.csv")

def question_1():
    orders_arry=np.genfromtxt('orders.csv', dtype='int32', delimiter=',', skip_header=1)
    return orders_arry

def question_2(orders_arry):
    price_arry=[]
    for i in orders_arry:
        quantity=i[3]
        product_id=i[2]
        shirt=my_SuperStore.Get_shirt(product_id)
        price_paid=quantity*shirt.price
        price_arry.append(price_paid)

    price_arry=np.reshape(price_arry,(200,1))

    orders_arry=np.append(orders_arry,price_arry,axis=1)

    return orders_arry


def question_3(orders_arry):
    maxprice=orders_arry[0][4]
    for i in orders_arry:
        if i[4]>maxprice:
            maxprice=i[4]
            shirts_order=i
    client=my_SuperStore.Get_Client(shirts_order[1])
    client_name=client.name
    product=my_SuperStore.Get_Product(shirts_order[2])
    product_name1=product.product_name
    print("order id is: "+str(shirts_order[0])+', '+"client name is: "+str(client_name)+', '+"product name is: " +product_name1+', '
      +" his price is: "+str(maxprice))


def question_4(client_id1):
    try:
        client1=my_SuperStore.Get_Client(client_id1)
        if client1==None:
            raise ClientNotFoundError
        print("The name of client is "+client1.name)
        countorders=0
        pay=0
        for i in orders_arry:
            if i[1]==client_id1:
                countorders+=1
                pay+=i[4]
        print("The number of orders is "+str(countorders))
        print("The total pay is "+str(pay))
    except ClientNotFoundError :
        print("Client Not Found Error")

def question_5(orders_arry):
    average_price=0
    for i in orders_arry:
        average_price+=i[4]
    average_price=average_price/len(orders_arry)
    for i in orders_arry:
        if i[4]>average_price:
           print("The order is\n"+"order_id:"+str(i[0])+" client_id:"+str(i[1])+' '+"product_id:"+str(i[2])+' '+"quantity:"+str(i[3]))

def question_6(orders_arry):
    listclientsid = []
    amount_orders = {}
    for i in orders_arry:
        listclientsid.append(i[1])
    listclientsid = list(dict.fromkeys(listclientsid))
    for i in listclientsid:
        count = 0
        for j in orders_arry:
            if j[1] == i:
                count += 1
        amount_orders[i] = count
    return amount_orders


def question_7(amount_orders):
    x_axis = []
    y_axis = []
    for i in amount_orders:
        x_axis.append(str(i))
        y_axis.append(str(amount_orders[i]))
    plt.bar(x_axis, y_axis)
    plt.title('The number of orders for each client')
    plt.xlabel('Clients ID')
    plt.ylabel('Number of orders')
    plt.show()


print(question_1())
y=question_1()
print(question_2(y))
orders_arry=question_2(y)
question_3(orders_arry)
client_id1 = int(input("please enter client id:"))
question_4(client_id1)
question_5(orders_arry)
print(question_6(orders_arry))
amount_orders=question_6(orders_arry)
question_7(amount_orders)
