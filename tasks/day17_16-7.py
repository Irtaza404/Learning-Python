# DAY 16 — OOP PRACTICE
# ════════════════════════

# TASK 1 — [Classes + Inheritance + __str__]
# Create a vehicle system:
# - Base class Vehicle: brand, speed, fuel
# - Car(Vehicle): extra attribute doors
# - Bike(Vehicle): extra attribute type ("sport"/"cruiser")
# - Truck(Vehicle): extra attribute payload (tons)
# - Each has __str__ showing all attributes
# - Each has a travel(km) method that calculates
#   fuel consumed (km / speed * fuel)

class Vehicle:
    def __init__(self,brand,speed,fuel):
        self.brand=brand
        self.speed=speed
        self.fuel=fuel
    def __str__(self):
        return f"{self.brand} |speed= {self.speed}| fuel = {self.fuel}| "
    def travel(self,distance):
        fuel_used = (distance / self.speed) * self.fuel
        return f"{self.brand} traveled {distance}km, used {fuel_used}L fuel"
class Car(Vehicle):
    def __init__(self, brand, speed, fuel,doors):
        super().__init__(brand, speed, fuel)
        self.doors=doors
    
    def __str__(self):
        return super().__str__()+f"doors = {self.doors}"
    
class Bike(Vehicle):
    def __init__(self, brand, speed, fuel,type):
        super().__init__(brand, speed, fuel)
        self.type=type
    def __str__(self):
        return super().__str__()+f"type = {self.type}"
        
class Truck(Vehicle):
    def __init__(self, brand, speed, fuel,payload):
        super().__init__(brand, speed, fuel)
        self.payload=payload
    def __str__(self):
        return super().__str__()+f"payload = {self.payload}"        


# Example:
# c = Car("Toyota", 120, 15, 4)
# c.travel(300)  → "Toyota traveled 300km, used 37.5L fuel"
# print(c)       → "Toyota | 120km/h | 4 doors"


# TASK 2 — [@dataclass + @property + Encapsulation]
# Create a Temperature class using @dataclass:
# - Private attribute __celsius
# - Properties: celsius, fahrenheit, kelvin
# - Setter validates temp > -273.15 (absolute zero)
# - classmethod from_fahrenheit(f) → creates from F
# - classmethod from_kelvin(k) → creates from K
# - __str__ → "25°C | 77°F | 298.15K"
from dataclasses import dataclass
@dataclass
class Temperature:
    _celsius:float
    def __str__(self):
        return f"{self._celsius}°C | {self.fahrenheit}°F | {self.kelvin}K"
    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Below absolute zero")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32
    
    @property
    def kelvin(self):
        return self._celsius + 273.15
    @classmethod
    def from_fahrenheit(cls, f):
        return cls((f - 32) * 5/9)  # convert to celsius first

    @classmethod
    def from_kelvin(cls, k):
        return cls(k - 273.15)  # convert to celsius first

# Example:
# t = Temperature(25)
# t.fahrenheit  → 77.0
# t.kelvin      → 298.15
# t.celsius = -300  → ValueError: Below absolute zero


# TASK 3 — [Abstract + Composition + Operator Overloading]
# Create a shape calculator:
# - Abstract base Shape: abstract methods area(), perimeter()
# - Circle, Rectangle, Triangle implement Shape
# - ShapeCollection class that:
#   - Holds list of shapes (composition)
#   - __add__ adds a shape to collection
#   - __len__ returns count
#   - __str__ prints all shapes and their areas
#   - total_area() returns sum of all areas

from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter():
        pass
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
        return 3.14*self.radius**2
    def perimeter(self):
        return 2 * 3.14 * self.radius

class Triangle (Shape):
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return  (s(s-self.a)(s-self.b)(s-self.c))**0.5
    
    def perimeter(self):
        return self.a +self. b + self.c

class Rectangle(Shape):
    def __init__(self,width ,height):
        self.width=width
        self.height=height
        
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)

class ShapeCollection:
    def __init__(self):
        self.shapes = []  
    def __add__(self, shape):
        self.shapes.append(shape)
        return self  
    def __len__(self):
        return len(self.shapes)
    def total_area(self):
        return sum(s.area() for s in self.shapes)
# Example:
# sc = ShapeCollection()
# sc + Circle(5)
# sc + Rectangle(4, 6)
# len(sc)         → 2
# sc.total_area() → 102.54


