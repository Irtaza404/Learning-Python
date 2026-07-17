# DAY 18 — EASY PRACTICE
# ════════════════════════

# EASY (1) — [Classes + __str__ + String Formatting]
# Create a Business Card class:
# - Attributes: name, title, company, email, phone
# - __str__ prints a formatted card:
# ┌─────────────────────────────┐
# │  Muhammad Irtaza            │
# │  AI Engineer                │
# │  Anthropic                  │
# │  irtaza@gmail.com           │
# │  0300-1234567               │
# └─────────────────────────────┘

class BusinessCard:
    def __init__(self,name,title,company,email,phone):
        self.name,self.title,self.company,self.email,self.phone=name,title,company,email,phone

    def __str__(self):
        return f"┌{"─"*32}┐\n| {self.name:<30}|\n| {self.title:<30}|\n| {self.company:<30}|\n| {self.email:<30}|\n| {self.phone:<30}|\n└{"─"*32}┘"

# EASY (2) — [Inheritance + @property]
# Create a Shape hierarchy:
# - Base: Shape with color attribute and @property area (returns 0)
# - Circle(Shape): radius, area property → π * r²
# - Rectangle(Shape): width, height, area property → w * h
# - Print each shape's color and area
class Shape:
    def __init__(self,color):
        self.color=color
    @property
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self,color,radius):
        super().__init__(color)
        self.radius=radius
    @property
    def area(self):
        return 3.14*self.radius**2
    
class Rectangle(Shape):
    def __init__(self,color,w,h):
        super().__init__(color)
        self.width=w
        self.height=h
        
    @property
    def area(self):
        return self.height*self.width

# Example:
# c = Circle("Red", 5)
# c.color  → "Red"
# c.area   → 78.5


# EASY (3) — [Collections + Regex + Functions]
# Write a function called extract_info() that takes a list
# of strings and returns a Counter of all valid emails,
# phone numbers and URLs found across all strings.
from collections import Counter
import re
def  extract_info(data):
    phone=email=urls=0
    for d in data:
        phone+=len(re.findall(r"\d{4}-\d{7}",d))
        email+= len(re.findall(r"[\w.-]+@[\w.-]+\.\w+",d))
        urls += len(re.findall(r"https?://[\w.-]+(?:\/[\w./?%&=~-]*)?", d))
    return Counter({"emails": email, "phones": phone, "urls": urls})

# Example:
data = ["email: ali@gmail.com, phone: 0300-1234567",
        "visit https://github.com or email sara@yahoo.com"]
print(extract_info(data))
# → Counter({"emails": 2, "phones": 1, "urls": 1})



# EASY (4) — [Datetime + Comprehension + Functions]
# Write a function called calendar_week() that takes any
# date string "DD-MM-YYYY" and returns a dict of all 7
# days of that week with their day names.
from datetime import datetime,timedelta
def calendar_week(da):
    da = datetime.strptime(da, "%d-%m-%Y").date()
    week={}
    for _ in range(7):
        week[da.strftime("%A")]=da.strftime("%d-%m-%Y")
        da=da + timedelta(days=1)
    return week

# Example:
calendar_week("13-07-2026")
# → {
#     "Monday": "15-01-2024",
#     "Tuesday": "16-01-2024",
#     ...
#     "Sunday": "21-01-2024"
#   }



# EASY (5) — [Dataclass + @classmethod + __str__]
# Create a Student dataclass:
# - Fields: name, age, gpa (default 0.0)
# - @classmethod from_string() that takes "Ali,20,3.8"
#   and creates a Student object
# - @classmethod from_dict() that takes
#   {"name":"Ali","age":20,"gpa":3.8}
# - __str__ → "Ali (20) — GPA: 3.8"

from dataclasses import dataclass
@dataclass
class Student:
    name:str
    age:int
    gpa:float = 0.0
    
    @classmethod
    def from_string(cls, s):
        name, age, gpa = s.split(",")
        return cls(name, int(age), float(gpa))
    
    @classmethod
    def from_dict(cls,d):
        return cls(d["name"], d["age"], d["gpa"])
    
    def __str__(self):
        return f"{self.name} ({self.age}) — GPA: {self.gpa}"
        
# Example:
# s1 = Student.from_string("Ali,20,3.8")
# s2 = Student.from_dict({"name":"Sara","age":21,"gpa":3.5})
# print(s1)  → "Ali (20) — GPA: 3.8"


