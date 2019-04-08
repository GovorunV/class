'''class User:
    name=""
    srname=""
    age=""
    email=""

    def set(self,name,srname,age): #self обезательный
        self.name=name
        self.srname=srname
        self.age=age
    def printall(self):
        print("Пользователь",self.name,"его возраст",self.age)

admin=User()
admin.set("Admin","Marg","23") # передача значений с ипользованием метода(функции)
#admin.name="admin" передача без функции
print(admin.name)

bob=User()
bob.set("Bob","Kolaw","23") # передача значений с ипользованием метода(функции)
#bob.name="Bob"
print(bob.name)
bob.printall()
'''
#Использование конструктора
'''
class User:
    name=""
    srname=""
    age=""
    email=""
    def __init__(self,name,srname,age,email): #конструктор (срабатывает при создании обьекта)
        self.name = name
        self.srname = srname
        self.age = age
        self.email=email

    def set(self,name,srname,age): #self обезательный
        self.name=name
        self.srname=srname
        self.age=age
    def printall(self):
        print("Пользователь",self.name,"его возраст",self.age)

admin=User("Admin","Marg","23","emasd@mail.com")
admin.printall()

bob=User("Bob","Kolaw","23","ssds@mail.ru")
bob.printall()
'''
class User:
    _name=""
    srname=""
    age=""
    email=""

    def set(self,name,srname,age): #self обезательный
        self._name=name #инкапсуляция _ ( не обезательно) или __
        self.srname=srname
        self.age=age
    def printall(self):
        print("Пользователь",self.name,"его возраст",self.age)
class Member (User): #наследния класа(полимирфизм) можно использовать все методы и переменые функции Юзер
    def printall(self): #переназначение метода
        print("Пользователь",self._name,"Фамилия",self.srname,"его возраст",self.age)
x3=Member()
x3.set("sfsdf","dfsd","23")
x3.printall()