import random
# Данные пользователя
import sys

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

class Product:
    productId = random.randint(1, 99999999)
    productName = ""
    
    def __init__(self, name):
        self.productId = random.randint(1, 99999999)
        self.productName = name    

class Storage:
    storageList = {}
    storageNames = {}
    
    def __init__(self):
        self.storageList = {}
        self.storageNames = {}
    
    def add_product(self, product, quantity=0):
        if product.productId in self.storageList:
            self.storageList[product.productId][0] += quantity
        else:
            self.storageList[product.productId] = [quantity, product.productName]
            
    def add_product2(self, product, quantity = 0):
        if product.productName in self.storageNames:
            self.storageNames[product.productName] += quantity
        else:
            self.storageNames[product.productName] = quantity

    def display_products(self):
        for product_id, data in self.storageList.items():
            print(f'Product ID: {product_id}, Product Name: {data[1]}, Quantity: {data[0]}')
     
class Order:
    orderSum = ''
    orderList = {}
    orderProducts = ''
    orderVal = int()
    
    def __init__(self):
    #Оформление Заказа на площадке 
      self.orderProducts = ''
      self.orderSum = ''
      self.orderList = {}
      self.orderVal = int()
      
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
        
    def agree_order(self):
        val = int(input('(1) - Подтвердить заказ, (0) - Отменить заказ'))
        if val == (1):
            print('Заказ оформлен!')
            self.orderVal = val
        elif val == (0):
            print('Заказ отменён')
            self.orderVal = val       
        else:
            return self.agree_order()
    
    def add_orderList(self, user):
        if self.orderVal == (1):
            if user.userName in self.orderList:
                self.orderList[user.userName] += [user.userId, self.orderProducts, self.orderSum]
            else:
                self.orderList[user.userName] = [user.userId, self.orderProducts, self.orderSum]
        elif self.orderVal == (0):
            pass         
    
    def display_order_info(self):
        for user, data in self.orderList.items():
            print(f'Имя заказчика: {user}, ID Заказчика: {data[0]}, Товары: {data[1]}, Количество: {data[2]}')

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
    
    def show_check_order(self, order: Order):
        order.display_order_info()
        self.check_order(order)
        
    def check_order(self, order: Order):
        if order.orderProducts in storage.storageNames:
            if order.orderSum <= storage.storageNames[order.orderProducts]:
                print('На складе есть требуемое количество товара')
                self.confirm_order()
            else:
                print('На складе не хватает товаров!')
                self.order_to_storage()
        else:
            print('Товар не найден!')

    def order_to_storage(self, order: Order):
        print(f'На складе: {storage.storageNames[order.orderProducts]}')
        print(f'Заказано: {order.orderSum}')
        a = int(storage.storageNames[order.orderProducts])
        b = int(order.orderSum)
        val = ((b) - (a))
        print(f'Необходимо заказать: {val}')
        self.end()
        
    def end(self):
        con = int(input('(1) - Заказать товар на склад, (0) - Отмена'))
        if con == (0):
            sys.exit()
        elif con == (1):
            print('Товар заказан')
            self.confirm_order()
        else:
            return self.end()       
    
    def confirm_order(self):
        val = int(input('(1) - Подтвердить заказ, (0) - Не подтверждать заказ'))
        if val == (1):
            print('Заказ подтверждён')
        elif val == (0):
            print('Заказ не подтверждён')
        else:
            return self.confirm_order()
    
    def hello_manager(self, list_orders = []):
        print(f'Здравствуйте {self.manageName}!')
        val = int(input('(1) - Просмотр заказов, (0) - Закрыть'))
        if val == (0):
            sys.exit()
        elif val == (1):
            for order in list_orders:
                self.show_check_order(order)
        else:
            return self.hello_manager()            
user1 = User()
user1.check_userName_length()
user1.check_userEmail_length()
user1.check_userPnum_length()
user1.display_user_info()

user2 = User()
user2.check_userName_length()
user2.check_userEmail_length()
user2.check_userPnum_length()
user2.display_user_info()

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

order1 = Order()
order1.add_orderProducts()
order1.check_orderSum()
order1.agree_order()
order1.add_orderList(user1)
order1.display_order_info()

order2 = Order()
order2.add_orderProducts()
order2.check_orderSum()
order2.agree_order()
order2.add_orderList(user2)
order2.display_order_info()
             
manager = Manager()
manager.check_manageName_length()
manager.check_manageEmail_length()
manager.check_managePnum_length()
manager.display_manager_info()
manager.hello_manager([order1, order2])
