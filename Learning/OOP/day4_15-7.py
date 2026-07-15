
from dataclasses import dataclass
@dataclass
class Pizza:
    toppings:list
    def describe(self):
        return f"{type(self).__name__} with "+ ", ".join(self.toppings)

    @classmethod
    def margherita(cls):
        return cls(["cheese", "tomato"])
    
    @staticmethod
    def is_valid_topping(toppings):
        return toppings in ["cheese", "olives", "tomato", "mushroom"]

p1 = Pizza(["cheese", "olives"])
p2 = Pizza.margherita()
print(p1.describe())
print(p2.describe())
print(Pizza.is_valid_topping("pepperoni"))
print(p1)






from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks" if hasattr(self, 'name') else "Woof"

# d = Dog()
# print(d.speak())

# a = Animal()


# from abc import ABC, abstractmethod


# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

#     @abstractmethod
#     def perimeter(self):
#         pass


# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2

# c = Circle(5)

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def describe(self):   # NOT abstract, just a normal method
        return f"This shape has area {self.area()}"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
print(Circle(5).describe())

from abc import ABC,abstractmethod
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
    
    @abstractmethod
    def refund(self,amount):
        pass

class CreditCard(PaymentMethod):
    
    def pay(self,amount):
        return f"Paid {amount} via {type(self).__name__}"
    
    def refund(self,amount):
        return f"refund {amount} via {type(self).__name__}"

class PayPal(PaymentMethod):
    
    def pay(self,amount):
        return f"Paid {amount} via {type(self).__name__}"
    
    def refund(self,amount):
        return f"refund {amount} via {type(self).__name__}"


# p=PaymentMethod()
p=[CreditCard(),PayPal()]
for c in p:
    print(c.pay(100))
    print(c.refund(100))





class Dog:
    pass

d = Dog()
print(type(d))          # step 1
print(type(d).__name__) # step 2
print(Dog.__name__)


cd "C:\Users\Muhammad Irtaza\OneDrive\Documents\Learning python\Learning-Python"
git add . 
git commit -m "Day 17" 
git push


















