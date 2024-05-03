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
    orderNumber = random.randint(1, 99999999)
    orderSum = ''
    orderList = {}
    orderProducts = ''
    orderVal = int()
    
    def __init__(self):
    #Оформление Заказа на площадке 
      self.orderProducts = ''
      self.orderSum = ''
      self.orderNumber = random.randint(1, 99999999)
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
                self.orderList[user.userName] += [user.userId, self.orderProducts, self.orderNumber, self.orderSum]
            else:
                self.orderList[user.userName] = [user.userId, self.orderProducts, self.orderNumber, self.orderSum]
        elif self.orderVal == (0):
            pass         
    
    def display_order_info(self):
        print(self.orderList)

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
    
    def confirm_order(self):
        con = int(input('(1) - Подтвердить заказ, (0) - Не подтверждать'))
        if con == (0):
            print('Заказ не подтверждён')
            sys.exit()
        elif con == (1):
            print('Заказ подтверждён')
            print(f'User ID: {user.userId}, Имя заказчика: {user.userName}, Email: {user.userEmail}, Телефон: {user.userPnum}')
            print(f"Номер заказа: {order.orderNumber}, Товары: {order.orderProducts}, Количество: {order.orderSum}")
            sys.exit()
        else:
            return self.confirm_order()
    
    def sum_products(self):
        val = int(input('Введите количество товара:'))
        if val <= (0):
            print('Недопустимое значение!')
            return self.sum_products()
        elif val > (0):
            print(F'{val} единиц(-а) товара заказано на склад.')
            self.confirm_order()
        else:
            return self.sum_products()
    
    def order_storage(self):
        sto = int(input('(1) - Заказать товар на склад, (0) - Отмена'))
        if sto == (0):
            sys.exit()
        elif sto == (1):
            self.sum_products()
        else:
            return self.order_storage()
    
    def compare_quantity(self):
        if order.orderProducts in storage.storageNames:
            if order.orderSum <= storage.storageNames[order.orderProducts]:
                print('На складе есть требуемое количество товара')
                self.confirm_order()
            else:
                print('На складе не хватает товаров!')
                self.order_storage()
        else:
            print('Товар не найден!')
    
    def check_confirm(self):
        print(f'Здравствуйте {self.manageName}!')
        val = int(input('Для просмотра и проверки заказа введите (1), для выхода введите (0).'))
        if val == (0):
            sys.exit()
        elif val == (1):
            print(f'User ID: {user.userId}, Имя заказчика: {user.userName}, Email: {user.userEmail}, Телефон: {user.userPnum}')
            print(f"Номер заказа: {order.orderNumber}, Товары: {order.orderProducts}, Количество: {order.orderSum}")
            self.compare_quantity()
            
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

order = Order()
order.add_orderProducts()
order.check_orderSum()
order.agree_order()
order.add_orderList(user1)
order.add_orderProducts()
order.check_orderSum()
order.agree_order()
order.add_orderList(user2)
order.display_order_info()          
             
manager = Manager()
manager.check_manageName_length()
manager.check_manageEmail_length()
manager.check_managePnum_length()
manager.display_manager_info()
manager.check_confirm()