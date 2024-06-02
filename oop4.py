import random

class User:
    def __init__(self):
        self.__userName = ""
        self.__userId = random.randint(1, 999999)
        self.__userEmail = ""
        self.__userPnum = ""
        self.__userInfo = []

    def set_userName(self, userName):
        userName = input('Введите ваше имя:')
        if len(userName) > 600:
            print("Вы превысили число допустимых символов!")
        else:
            self.__userName = userName

    def get_userName(self):
        return self.__userName

    def set_userEmail(self, userEmail):
        userEmail = input('Введите ваш Email:')
        if len(userEmail) > 360:
            print("Вы превысили число допустимых символов!")
        else:
            self.__userEmail = userEmail

    def get_userEmail(self):
        return self.__userEmail

    def set_userPnum(self, userPnum):
        userPnum = input('Введите ваш телефон +7:')
        if len(userPnum) > 20:
            print("Некорректный номер телефона!")
        else:
            self.__userPnum = userPnum

    def get_userPnum(self):
        return self.__userPnum

    def display_user_info(self):
        print(f"User ID: {self.__userId}")
        print(f"Имя пользователя: {self.__userName}")
        print(f"Email: {self.__userEmail}")
        print("Номер телефона: +7", (self.__userPnum))

user1 = User()
user1.set_userName(user1)
user1.get_userName()
user1.set_userEmail(user1)
user1.get_userEmail()
user1.set_userPnum(user1)
user1.get_userPnum()
user1.display_user_info()