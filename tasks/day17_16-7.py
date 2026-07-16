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
        return f"{self.brand} traveled {distance}km, used {self.fuel}L fuel"
        
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
    __celsius:float

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
    def area(self):
        pass
    def perimeter(self):
        pass


# Example:
# sc = ShapeCollection()
# sc + Circle(5)
# sc + Rectangle(4, 6)
# len(sc)         → 2
# sc.total_area() → 102.54


# TASK 4 — [Polymorphism + Duck Typing + @classmethod]
# Create a notification system:
# - Base class Notification: message, timestamp
# - EmailNotification: adds recipient, subject
# - SMSNotification: adds phone number
# - PushNotification: adds device_id
# - NotificationSender class with:
#   - send(notification) — duck typing, calls notification.send()
#   - @classmethod bulk_send(cls, notifications) — sends all
#   - Each subclass implements own send() method

# Example:
# sender = NotificationSender()
# sender.send(EmailNotification("Hello", "ali@gmail.com", "Greeting"))
# → "[EMAIL] To: ali@gmail.com | Subject: Greeting | Hello"

# sender.send(SMSNotification("Hello", "0300-1234567"))
# → "[SMS] To: 0300-1234567 | Hello"



