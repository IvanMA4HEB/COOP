import random
# Данные пользователя
class user:
    Name = ""
    userId = random.randint(1, 99999999)
    Email  =  "введите вашу почту:"
    userPnum = 0
    
    def init(self):
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
    
    def init(self):
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
  
  
class zakaz:
    zakazNumbers = random.randint(1, 99999999)
    zakazId = random.randint(1, 99999999)
    zakazSum = 0
    
    def init(self):
    #Оформление Заказа на площадке 
      self.check_zakazSum_length()
      self.zakazId = random.randint(1, 99999999)
      self.zakazNumbers = random.randint(1, 99999999)
      
    def check_zakazSum_length(self):
            val = input("input Sum")
            if len(val) > 1000000:
                print("Вы привысили допустимое количество товара!")
            else:
             self.zakazSum = val
             print("Заказ оформлен")
   
      
class storage:
     storageNumber =  range(1, 10)
     storageList = ['Системный блок', 'Микрофон', 'Монитор', 'Клавиатура', 'Процессор', 'Видеокарта']
     storageSum = int(999999999)
    
     def init(self):
    #Проверка товара на складе 
      self.storageNum = range(1, 10)
      self.storageList = ['Системный блок', 'Микрофон', 'Монитор', 'Клавиатура', 'Процессор', 'Видеокарта']
      self.check_storageSum_lenght()
      
def check_storageSum_length(self):
    val = input("input Sum")
    if len(val) > 1000000:
        print("Вы привысили допустимое количество товара!")
    else:
        self.storageSum = val
        print("Заказ оформлен")
        
        
class product:
    productId = random.randint(1, 99999999)
    productName = ""
    productlist = ['Монитор', 'Системный блок', 'Клавиатура']
    #Список товара 
    #productlist.append('Монитор')
    #productlist.append('Системный блок')
    #productlist.append('видеокарта')
    
def init(self):
# Проверка товара на маркетплейсе и его добавление 
  self.productId = random.randint(1, 99999999)
  self.check_productName_length()
  self.productList = ['Монитор', 'Системный блок', 'Клавиатура']

def check_productName_length(self):
    val = input("input Name")
    if len(val) > 1000000:
        print("Вы привысили допустимое количество товара!")
    else:
        self.productName = val
        print("Заказ оформлен")