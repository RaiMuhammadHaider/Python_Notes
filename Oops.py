class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info (self):
        print(f"Name : {self.name} \n Age : {self.age}")
    def studyInfo(self,level , grade):
        self.level = level
        self.grade = grade
        return f"Level of study is : {level} , \n Grades are : {grade}"
college = student('Ali Haider' , 21)
# print(college.info())
print(college.studyInfo('Bscs' , 'OKO'))

#  Encapsulation 
class bankBalance:
    def __init__(self, owner , balance):
        self.owner = owner
        self.__balance = balance # private can not be access directly it can be get only get by calling method
    def deposit(self , amount):
        if amount > 0:
            self.__balance += amount
    def get_balance(self):
        return f"{self.__balance} Your Total amount is "
amount = bankBalance('Ali', 100)
print(amount.deposit(1600))
# print(amount._balance)
print(amount.get_balance())

# Inheritance 
class Animal :
    def __init__(self , name , bread):
        self.name = name
        self.bread = bread
        print('Constructor called')
    def crow(self , milk , color):
        print('crow speak')
        print( f"{milk} : {color}" ) # local variable k sath self use nahi hota self is only use for globelly constructor
    def got(self, milk , color):
        return f"{milk} in Kg : {color} in Color"

class birds(Animal):
    def Birds_Name(self, name):
        return f"Name is {name}"
# animal = Animal('bird', 'Green')
# print(animal.crow(10, 'black'))
# print(animal.got(39,'Green'))
alll = birds('haider' , 'OKKKKKKKKKKKK')
print(alll.got(40, 'yellow'))

# pholimorphisim
class White:
    def wallColor(self):
      return 'wall Color is Whte'
class Black:
    def wallColor(self):
      return'Black color'
for obj in (White(),Black()):
    print(obj.wallColor())


class CreditCardPayment:
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card.")

class PayPalPayment:
    def pay(self, amount):
        print(f"Paid {amount} using PayPal.")

def payment_processing(payment_method , amount):
    payment_method.pay(amount)
payment_processing(CreditCardPayment() , 100)
payment_processing(PayPalPayment() , 2000)

########################################################

class Car:
    total_car = 0
    def __init__(self , brand , Model): # constructor 
        self.__brand = brand # we make the brand as private now it can not be access by with class but can get access by method
        self.__Model = Model
        Car.total_car += 1 # to count how many a constructor is call or to find how may cars are created
        print('Automatically called a Constructor')
    def get_brand(self): # getter method to get private attribute atteribute can not be directly ass but we can get by it mothod

        return self.__brand + '!'
    def set_brand(self , new_brand):
        if new_brand > 0:
            __brand = new_brand
        else:
            print('Enter in String')
    def car_info(self):
        return f"Brand : {self.__brand} & Model : {self.__Model} bettery_size"
    def fule_type(self): # polymorphism
        return 'Petrol & Deisal'
    @staticmethod # this is use to make any method intoa staticmethod mean it can be access easily without wiring using self into method mena it can be easily access by using class withoud converting it into object when use staticmethod do not use self these are also called decorators
    def general_description():
        return 'Static mrthod'
    @property # want to hide property can only be access by the method
    def model(self):
        return self.__Model
  
  
# car = Car('Honda' , 'Civic')
class Electric_Car(Car):
    def __init__(self, brand , Model , Bettery_Size):
        super().__init__(brand,Model)
        self.Bettery_size = Bettery_Size
    def fule_type(self): # polymorphism
        return 'Electric Charge'
# print(car.brand)
# print(car.Model)
# new_car = Car('Tayota', ' Safari')
# print(new_car.brand)
# print(new_car.Model)
# print(car.car_info())
my_tesla = Electric_Car('Tesla', 'Model S' , '39KWh')
# Multiple Inheritance
class Engin:
    def car_Engin(self):
        return 'Car Engine is Electric'
class Bettery:
    def car_bettery(self):
        return 'Car bettery is leathum'
class Electric_car_Model(Engin , Bettery , Car):
    pass
new_tesla_car = Electric_car_Model('Tesla','T Shap')
print(new_tesla_car.car_bettery())
print(new_tesla_car.fule_type())
print(new_tesla_car.car_info())
# print(my_tesla.brand)
# print(my_tesla.car_info())
# print(my_tesla.get_brand())
# print(my_tesla.set_brand(192))
# print(my_tesla.get_brand())
# print(my_tesla.__brand)
# print(my_tesla.__brand)
# polymorphism mean a method can have same name but different behaviour like fule type in electric car and fule type in petrol car or deisal car 
print(my_tesla.fule_type())
car = Car('Tesla', 'Model S' , )
c = Car('Tesla', 'Model S' , )
c = Car('Tesla', 'Model S' , )
ca = Car('Tesla', 'Model S' , )
print(car.total_car)
print(car.fule_type())
print(car.general_description())
print(Car.general_description())
print(car.model)
print(isinstance (car , Car))
print(isinstance (car , Electric_Car))
print(isinstance (my_tesla , Electric_Car)) # to check is the object is the instance of class in boolean form 
