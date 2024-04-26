import random
import sys

class Product:
    productId = random.randint(1, 99999999)
    productName = ""
    
    def __init__(self, name):
        self.productId = random.randint(1, 99999999)
        self.productName = name
        

class Storage:
    storageList = {}
    storageNames = {}
    quantity = 0
    
    def __init__(self):
        self.storageList = {}
        self.storageNames = {}
        self.quantity = 0
        
    
    def add_product(self, product, quantity=0):
        if product.productId in self.storageList:
            self.storageList[product.productId][0] += quantity
        else:
            self.storageList[product.productId] = [quantity, product.productName]
            #self.storageNames.append(product.productName)
            
    def add_product2(self, product, quantity = 0):
        if product.productName in self.storageNames:
            self.storageNames[product.productName] += quantity
        else:
            self.storageNames[product.productName] = quantity

    def display_products(self):
        for product_id, data in self.storageList.items():
            print(f'Product ID: {product_id}, Product Name: {data[1]}, Quantity: {data[0]}')
            print(self.storageNames)


product1 = Product("Монитор")
product2 = Product("Клавиатура")

storage = Storage()
storage.add_product(product1, 10)
storage.add_product(product2, 100)
storage.add_product(product1, 40)
storage.add_product2(product1, 10)
storage.add_product2(product2, 100)
storage.add_product2(product1, 40)
storage.display_products()
     
class Order:
    orderNumber = random.randint(1, 99999999)
    orderSum = ''
    orderList = {}
    orderProducts = ''
    
    def __init__(self):
    #Оформление Заказа на площадке 
      self.orderProducts = ''
      self.orderSum = ''
      self.orderNumber = random.randint(1, 99999999)
      
    def add_orderProducts(self):
        val = input('Введите название товара:')
        if val in storage.storageNames:
            self.orderProducts = val
            print('Товар добавлен')
        else:
            print('Товара нет на складе')
            return self.add_orderProducts
    
    def check_orderSum(self):
        val = int(input('Введите количество товара:'))
        if val <= 1000000:
            self.orderSum = val
        else:
            print('Такого количества товара нет!')
            return self.check_orderSum()
       
    def display_order_info(self):
        val = int(input('Вы подтверждаете заказ? (1 - Да, 0 - Нет)'))
        if val == (1):
            print('Заказ оформлен')
            #print(f'User ID: {user.userId}, Имя заказчика: {user.userName}, Email: {user.userEmail}, Телефон: {user.userPnum}')
            print(f"Номер заказа: {self.orderNumber}, Товары: {self.orderProducts}, Количество: {self.orderSum}")
        elif val == (0):
            print('Заказ отменён')
            sys.exit()
        else:
            return self.display_order_info()    
            
order = Order()
order.add_orderProducts()
order.check_orderSum()
order.display_order_info()

class Manager:
    def compare_quantity(self):
        if order.orderProducts in storage.storageNames:
            if order.orderSum <= storage.storageNames[order.orderProducts]:
                print('The requested quantity is available in storage.')
            else:
                print('Insufficient quantity available in storage.')
        else:
            print('Product not found in storage.')

manager = Manager()
manager.compare_quantity()