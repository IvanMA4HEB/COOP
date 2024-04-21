import random
# Данные пользователя
class User:
    Name = ""
    userId = random.randint(1, 99999999)
    Email  =  ""
    userPnum = 0
    userIdList = {}
    
    def __init__(self):
        self.check_name_length()
        self.check_Email_length()
        self.check_userPnum_length()
        self.userId = random.randint(1, 99999999)
        self.userIdList = {}
        
    def check_name_length(self):
        val = input("input name:")
        if len(val) > 600:
            print ("Вы превысили число допустимых символов!")
        else:
            self.Name = val
            print ("Вы зарегистрированы")
            
    def check_Email_length(self):
        val = input("input Email:")
        if len(val) > 360:
             print ("Вы превысили число допустимых символов!")
        else:
            self.Email = val
            print("Вы зарегистрированы")
            
    def check_userPnum_length(self):
        val = input("input Pnum:")
        if len(val) > 20:
             print ("Вы превысили число допустимых символов!")
        else:
            self.userPnum = val
            print("Вы зарегистрированы")
            print(f"User ID: {self.userId}")
        #self - ключевая команда ссылающая экзампляр класса(Элемент класса)
    



user = User()
user.check_name_length
user.check_Email_length
user.check_userPnum_length

class Manager:
    ManageName = ""
    ManageEmail = ""
    ManageId = random.randint(1, 99999999)
    managePnum =  0
    
    def __init__(self):
        self.check_ManageName_length()
        self.check_ManageEmail_length()
        self.check_ManagePnum_length()
        self.ManageId = random.randint(1, 99999999)
        # Данные менеджера
                     
    def check_ManageName_length(self):
         val = input("input Manage name:")
         if len(val) > 600:
             print ("Вы превысили число допустимых символов!")
         else:
             self.ManageName = val
             print ("Вы зарегистрированы")
                
    def check_ManageEmail_length(self):
          val = input("input Manage Email:")
          if len(val) > 360:
            print ("Вы превысили число допустимых символов!")
          else:
             self.ManageEmail = val
             print("Вы зарегистрированы")
                
    def check_ManagePnum_length(self):
            val = input("input Pnum:")
            if len(val) > 20:
                print ("Вы превысили число допустимых символов!")
            else:
             self.ManagePnum = val
             print("Вы зарегистрированы")    
  
class Product:
    productId = random.randint(1, 99999999)
    productName = ""
    
    def __init__(self, name):
        
        self.productId = random.randint(1, 99999999)
        self.productName = name
    
        

class Storage:
    storageList = {}
    
    def __init__(self):
        self.storageList = {}
    
    def add_product(self, product, quantity=0):
        if product.productId in self.storageList:
            self.storageList[product.productId][0] += quantity
        else:
            self.storageList[product.productId] = [quantity, product.productName]

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


        
class Zakaz:
    zakazNumbers = random.randint(1, 99999999)
    zakazId = random.randint(1, 99999999)
    zakazSum = 0
    zakazList = {}
    
    def __init__(self):
    #Оформление Заказа на площадке 
      self.check_zakazSum_length()
      self.zakazId = random.randint(1, 99999999)
      self.zakazNumbers = random.randint(1, 99999999)
      self.zakazList = {}
      
    def check_zakazSum_length(self):
            val = input("input Sum")
            if len(val) > 1000000:
                print("Вы привысили допустимое количество товара!")
            else:
             self.zakazSum = val
             print("Заказ оформлен")
             
    def confirm_zakazList(self):
        val = input('Для подтверждения заказа введите "1", для отмены "0"')
        if val == 1:
            self.zakazList = list(self.productList)
            print('Заказ подтверждён')
        elif val == 0:
            print('Заказ отменён')
        else:
            self.zakazList = val
            print('Ошибка!')

