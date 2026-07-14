# class Animal:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def describe(self):
#         print(f"name = {self.name}")
#         print(f"age = {self.age}")
        
# class dog(Animal):
#     def bark(self):
#         print("wooh wooh")
        
# class cat(Animal):
#     def meow(self):
#         print("meow meow")        


class Animal:
    def speak(self):
        return "Some generic sound"


class Dog(Animal):
    pass


d = Dog()
print(d.speak())

# A class Vehicle with __init__(self, brand, speed) and a method describe() returning something like "Toyota moving at 60 km/h".
# A class Car(Vehicle) that:
class Vehicle:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
    
    def describe(self):
        return f"{self.brand} moving at {self.speed} km/h"

class car(Vehicle):
    def __init__(self, brand, speed,nums_door):
        super().__init__(brand, speed)
        self.num_doors=nums_door
    
    def describe(self):
        return f"{super().describe()} with {self.num_doors} doors"

print(car.__mro__)

# adds num_doors in its own __init__ (using super() for the shared parts)
# overrides describe() to reuse Vehicle's describe() via super(), and adds the door count to the message.


class Father:
    def skills(self):
        return "Gardening"


class Mother:
    def skills(self):
        return "Cooking"


class Child(Father, Mother):
    pass


c = Child()
print(Child.__mro__)


class Animal:
    def speak(self):
        return "Some sound"


class Father(Animal):
    def speak(self):
        return "Father sound"


class Mother(Animal):
    def speak(self):
        return "Mother sound"


class Child(Father, Mother):
    pass


c = Child()
print(c.speak())
print(Child.__mro__)

c = Child()
print(isinstance(c, Father))
print(isinstance(c, Animal))
print(isinstance(c, Mother))
print(issubclass(Child, Animal))
print(issubclass(Father, Mother))

class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} barks"


print(Dog.speak())   # calling on the class, not an instance

