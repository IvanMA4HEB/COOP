import random
# Данные пользователя
userName = str(input('Введите ваше имя:'))
if len(userName) > 600:
    print ("Вы превысили число допустимых символов!")
else:
    print ("Вы зарегистрированы")
userEmail = str(input("Введите вашу почту:"))
if len(userEmail) > 360:
    print ("Вы превысили число допустимых символов!")
else:
    print ("Вы зарегистрированы")
userId = random.randint(1, 99999999)
print (userId)
userPnum = int(input("7"))
if (userPnum) < 999999999999:
    print("+7", (userPnum))
else:
    print('Error')



manageName = str(input('Введите ваше имя:'))
if len(manageName) > 600:
    print ("Вы превысили число допустимых символов!")
else:
    print ("Вы зарегистрированы")
manageEmail = str(input("Введите вашу почту:"))
if len(manageEmail) > 360:
    print ("Вы превысили число допустимых символов!")
else:
    print ("Вы зарегистрированы")
manageId = random.randint(1, 99999999)
print (manageId)
managePnum = int(input("7"))
if (managePnum) < 999999999999:
    print("+7", (managePnum))
else:
    print('Error')

zakazNumbers = random.randint(1, 99999999)
zakazId = random.randint(1, 99999999)
zakazSum = int(input('Введите кол-во товара:'))
if (((zakazSum) < 1000000) & ((zakazSum) > 0)):
    print("Заказ оформлен")
else:
    
    print('Недопустимое количество')


storageNumber = range(1, 10)
storageSum = int(999999999)

productId = random.randint(1, 99999999)
productName = str(input('Введите название товара:'))
if len(productName) < 100:
    print('Товар в наличии')
else:
    print('Такого товара нет')