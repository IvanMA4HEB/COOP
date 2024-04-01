import random
# Данные пользователя
class user:
    Name = ""
    userId = random.randint(1, 99999999)
    Email  =  str (input("введите вашу почту:"))
    userPnum = int
    
    def __init__(self):
        
        self.Name = str(input('Введите ваше имя:'))
        #check_name_length(self)
        self.userId = random.randint(1, 99999999)
        self.Email = str(input("Введите вашу почту:"))
        if len(self.Email) > 360:
            print ("Вы превысили число допустимых символов!")
        else:
            print ("Вы зарегистрированы")
        
        self.userPnum = int(input("Введите номер телефона +7"))
        if (self.userPnum) < int(999999999999):
            print("+7", (self.userPnum))
        else:
            print('Error')
        
    def check_name_length(self):
        if len(self.Name) > 600:
            print ("Вы превысили число допустимых символов!")
        else:
            print ("Вы зарегистрированы")
            #self - ключевая команда ссылающая экзампляр класса(Элемент класса) 

class manager:
    manageName = ""
    manageEmail = str(input('Введите ваше имя:'))
    manageId = random.randint(1, 99999999)
    managePnum =  int(input("Введите номер телефона +7"))
    
    def __init__(self):
        # Данные менеджера
          self.manageName = str(input('Введите ваше имя:'))
          if len(self.manageName) > 600:
              print ("Вы превысили число допустимых символов!")
          else:
              print ("Вы зарегистрированы")
          self.manageEmail = str(input("Введите вашу почту:"))
          if len(self.manageEmail) > 360:
              print ("Вы превысили число допустимых символов!")
          else:
              print ("Вы зарегистрированы")
              self.manageId = random.randint(1, 99999999)
              print (self.manageId)
              self.managePnum = int(input("7"))
              if (self.managePnum) < 999999999999:
                  print("+7", (self.managePnum))
              else:
                  print('Error')
  
  
class zakaz:
    zakazNumbers = random.randint(1, 99999999)
    zakazId = random.randint(1, 99999999)
    zakazSum = int(input('Введите кол-во товара:'))
    
    def __init__(self):
    #Оформление Заказа на площадке 
      self.zakazNumbers = random.randint(1, 99999999)
      self.zakazId = random.randint(1, 99999999)
      self.zakazSum = int(input('Введите кол-во товара:'))
      if (((self.zakazSum) < 1000000) & ((self.zakazSum) > 0)):
          print("Заказ оформлен")
      else:
          print('Недопустимое количество')


class storage:
     storageNumber =  range(1, 10)
     storageList = list('Видеокарта', 'Монитор', 'Дверь')
     def new_func():
         storageSum = int(999999999)
    
     def __init__(self):
    #Проверка товара на складе 
      self.storageNumber = range(1, 10)
      self.storageSum = int(999999999)
      self.storageList = list('Видеокарта', 'Монитор', 'Дверь')


class product:
    productId = random.randint(1, 99999999)
    productName = str(input('Введите название товара:'))
    
def __init__(self):    
# Проверка товара на маркетплейсе и его добавление 
  self.productId = random.randint(1, 99999999)
  self.productName = str(input('Введите название товара:'))
  if ((self.productName) == (self.storageList)):
      print('Товар в наличии')
  else:
      print('Такого товара нет')