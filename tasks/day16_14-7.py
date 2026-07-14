# Day 16 Task: Shape Hierarchy
# Part 1 — Basic Inheritance

# Create a class Shape with:

# __init__(self, name) that stores self.name
# a method area() that returns 0 (default, since a generic "shape" has no defined area)
# a method describe() that returns f"{self.name} has an area of {self.area()}"

class Shape:
    def __init__(self,name):
        self.name=name

    def area(self):
        return 0

    def describe(self):
        print(f"{self.name} has an area of {self.area()}")

# Part 2 — Multiple children (Hierarchical inheritance)

# Create Circle(Shape):

# __init__(self, radius) — call super() to set the name to "Circle", and store self.radius
# override area() to return 3.14 * radius ** 2
class Circle(Shape):
    def __init__(self, radius):
        super().__init__(type(self).__name__)
        self.radius=radius
    def area(self):
        return 3.14 * self.radius ** 2
        

# Create Rectangle(Shape):

# __init__(self, width, height) — call super() to set the name to "Rectangle", store self.width and self.height
# override area() to return width * height
class Rectangle(Shape):
    def __init__(self, width,height):
        super().__init__(type(self).__name__)
        self.width=width
        self.height=height
        
    def area(self):
        return  self.width * self.height
        


# Create Square(Rectangle) (multilevel inheritance):

# __init__(self, side) — call super() passing side as both width and height
# override the name to "Square" (think about where/how to change it — you already have self.name available from the chain)

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side,side)
        self.side=side



# Part 3 — Polymorphism

# Create a list of shapes: one Circle, one Rectangle, one Square, with values of your choice.
# Loop through the list and call .describe() on each — without checking the type anywhere.

shape=[Circle(5),Rectangle(3,7),Square(5)]
for s in shape:
    s.describe()

# Part 4 — Duck typing (bonus)

# Create a completely unrelated class Triangle (does not inherit from Shape) that also has area() and describe() methods defined independently (copy the same logic/pattern).
# Add a Triangle object to your list from step 5, and run the same loop — confirm it works via duck typing.

class Triangle:
    def area(self):
        return 0

    def describe(self):
        print(f"{type(self).__name__} has an area of {self.area()}")
        
shape.append(Triangle())

for s in shape:
    s.describe()





