import random
# Данные пользователя

class User:
    userName = ""
    userId = random.randint(1, 999999)
    userEmail = ""
    userPnum = ""
    
    def __init__(self):
        self.userName = ""
        self.userId = random.randint(1, 999999)
        self.userEmail = ""
        self.userPnum = ""

    def check_userName_length(self):
        val = input("Введите имя пользователя: ")
        if len(val) > 600:
            print("Вы превысили число допустимых символов!")
        else:
            self.userName = val

    def check_userEmail_length(self):
        val = input("Введите Email: ")
        if len(val) > 360:
            print("Вы превысили число допустимых символов!")
        else:
            self.userEmail = val

    def check_userPnum_length(self):
        val = input("Введите номер телефона +7: ")
        if len(val) > 20:
            print("Некорректный номер телефона!")
        else:
            self.userPnum = val

    def display_user_info(self):
        print(f"User ID: {self.userId}")
        print(f"Имя пользователя: {self.userName}")
        print(f"Email: {self.userEmail}")
        print("Номер телефона: +7", (self.userPnum))

user = User()
user.check_userName_length()
user.check_userEmail_length()
user.check_userPnum_length()
user.display_user_info()

class Manager:
    manageName = ""
    manageEmail = ""
    manageId = random.randint(1, 99999999)
    managePnum = ''
    
    def __init__(self):
        self.manageId = random.randint(1, 99999999)
        self.manageName = ''
        self.manageEmail = ''
        self.managePnum = ''
        # Данные менеджера
                     
    def check_manageName_length(self):
         val = input("Введите имя менеджера:")
         if len(val) > 600:
             print ("Вы превысили число допустимых символов!")
         else:
             self.manageName = val
                
    def check_manageEmail_length(self):
          val = input("Введите Email:")
          if len(val) > 360:
            print ("Вы превысили число допустимых символов!")
          else:
             self.manageEmail = val
                
    def check_managePnum_length(self):
            val = input("Введите номер телефрна +7:")
            if len(val) > 20:
                print ("Вы превысили число допустимых символов!")
            else:
             self.managePnum = val
             
    def display_manager_info(self):
        print(f"Manager ID: {self.manageId}")
        print(f"Имя менеджера: {self.manageName}")
        print(f"Email: {self.manageEmail}")
        print("Номер телефона: +7", (self.managePnum))
             
manager = Manager()
manager.check_manageName_length()
manager.check_manageEmail_length()
manager.check_managePnum_length()
manager.display_manager_info()
  
import random

class Product:
    productId = random.randint(1, 99999999)
    productName = ""
    
    def __init__(self, name):
        self.productId = random.randint(1, 99999999)
        self.productName = name
    
        

class Storage:
    storageList = {}
    storageNames = []
    storageQuan = []
    
    def __init__(self):
        self.storageList = {}
        self.storageNames = []
    
    def add_product(self, product, quantity=0):
        if product.productId in self.storageList:
            self.storageList[product.productId][0] += quantity
        else:
            self.storageList[product.productId] = [quantity, product.productName]
            self.storageNames.append(product.productName)

    def display_products(self):
        for product_id, data in self.storageList.items():
            print(f'Product ID: {product_id}, Product Name: {data[1]}, Quantity: {data[0]}')


product1 = Product("Монитор")
product2 = Product("Клавиатура")

storage = Storage()
storage.add_product(product1, 10)
storage.add_product(product2, 100)
storage.add_product(product1, 40)
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
            print(f"Номер заказа: {self.orderNumber}, Товары: {self.orderProducts}, Количество: {self.orderSum}")
        elif val == (0):
            print('Заказ отменён')
        else:
            return self.display_order_info()    
            
order = Order()
order.add_orderProducts()
order.check_orderSum()
order.display_order_info()
   