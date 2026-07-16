class Battery:
    def charge_level(self):
        return f"Battery at 80%"
    
class CPU:
    def process(self):
        return f"processing data ...."

class laptop:
    def __init__(self):
        self.battery=Battery()
        self.cpu=CPU()
    
    def check_battery(self):
        return self.battery.charge_level()
    
    def run(self):
        return self.cpu.process()
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"


p1 = Point(1, 2)
p2 = Point(3, 4)

p3 = p1 + p2
print(p3)



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Point(1, 2)
p2 = Point(1, 2)

print(p1 == p2)


class Money:
    def __init__(self, amount):
        self.amount = amount
    def __eq__(self, other):
        return self.amount == other.amount
    def __add__(self, other):
        return Money(self.amount + other.amount)


    def __lt__(self, other):
        return self.amount < other.amount

    def __repr__(self):
        return f"${self.amount}"


m1 = Money(50)
m2 = Money(30)
m3 = Money(90)

print(sorted([m1, m2, m3]))
from dataclasses import dataclass

@dataclass
class Dog:
    name: str
    species: str = "Canine"


d1 = Dog("Rex")
d2 = Dog("Max", "Wolf-hybrid")

d2.species="d"
print(d1.name, d1.species)
print(d2.name, d2.species)