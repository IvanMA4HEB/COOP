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
  
class product:
    productId = random.randint(1, 99999999)
    productName = ""
    productlist = []
    Nameproduct:str = "Монитор"
    id: int = 1
    Nameproduct:str = "Клавиатура"
    id: int = 2   
    
    def front_typing_include_list(self):
            val = input("input Name")
            if (len(val) < 1000000) & (val == (self.storageList)):
                print("Вы добавили товар в корзину")
                self.productList.append(val)
            else:
                self.productName = val
                print("Недопустимое значение!") #Список товара 
    #productlist.append('Монитор')
    #productlist.append('Системный блок')
    #productlist.append('видеокарта')
    
class storage:
     #StorageProduct = []
     StorageProduct = [ ("Монитор", 1),  ("Клавиатура", 2)]
     storageNumber =  range(1, 10)
     storageList = ['Системный блок', 'Микрофон', 'Монитор', 'Клавиатура', 'Процессор', 'Видеокарта']
     storageSum = int(999999999)
    
     def __init__(self):
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
        
    #Список товара 
    #productlist.append('Монитор')
    #productlist.append('Системный блок')
    #productlist.append('видеокарта')
    
def __init__(self):
# Проверка товара на маркетплейсе и его добавление 
  self.productId = random.randint(1, 99999999)
  self.front_typing_include_list()
  self.productList = []


        
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
