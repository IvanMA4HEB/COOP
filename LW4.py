import random
# Данные пользователя
class user:
    Name = ""
    userId = random.randint(1, 99999999)
    Email  =  "введите вашу почту:"
    userPnum = 0
    
    def __init__(self):
        self.check_name_length()
        self.check_Email_length()
        self.check_userPnum_length()
        self.userId = random.randint(1, 99999999)
        
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
        #self - ключевая команда ссылающая экзампляр класса(Элемент класса)


class manager:
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
    storageName = {}
    
    def __init__(self):
        self.storageList = {}
        self.storageName = {}
    
    def add_product(self, product, quantity = 0):
        for product.productId in self.storageList:
            self.storageList[product.productId] += quantity
        else:
            self.storageList[product.productId] = quantity

            
            
    def add_name(self, name, quantity = 0):
        if name.productName in self.storageName:
            self.storageName[name.productName] += quantity
        else:
            self.storageName[name.productName] = quantity

    def display_products(self):
        for name in self.storageName.items():
            print(f'Name: {name}')
        for product, quantity in self.storageList.items():
            print(f'Product ID: {product}, Name: {name}, Quantity: {quantity}')

product1 = Product("Монитор" )
product2 = Product("Клавиатура" )

storage = Storage()
storage.add_name(product1)
storage.add_product(product1,10)
storage.add_name(product2)
storage.add_product(product2,100)
storage.display_products()

        
class zakaz:
    zakazNumbers = random.randint(1, 99999999)
    zakazId = random.randint(1, 99999999)
    zakazSum = 0
    zakazList = []
    
    def __init__(self):
    #Оформление Заказа на площадке 
      self.check_zakazSum_length()
      self.zakazId = random.randint(1, 99999999)
      self.zakazNumbers = random.randint(1, 99999999)
      self.zakazList = []
      self.confirm_zakazList()
      
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
