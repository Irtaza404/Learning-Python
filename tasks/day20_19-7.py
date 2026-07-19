# DAY 20 — HARD PRACTICE
# ════════════════════════

# HARD (1) — [OOP + Inheritance + Composition + Decorators + 
#             Generators + Error Handling + Collections]

# Build a Library Management System:

# 1. @log_calls decorator — logs every method call with
#    timestamp and call count using Counter

from abc import ABC, abstractmethod
from collections import Counter
import datetime
from functools import wraps
call_counts = Counter()
def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        call_counts[func.__name__] += 1
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[LOG] {timestamp} - Called '{func.__name__}' | Total calls: {call_counts[func.__name__]}")
        return func(*args, **kwargs)
    return wrapper
# 2. Abstract base class LibraryItem:
#    - Private: __id, __title, __available
#    - Properties: id, title, available
#    - Abstract methods: item_type(), display()
#    - __str__ → "LIB-001 | Book | Clean Code | Available"
from abc import ABC,abstractmethod
class LibraryItem(ABC):
    count=0
    def __init__(self,title):
        LibraryItem.count += 1
        self.__id=f"LIB-{LibraryItem.count:03}"
        self.__title=title
        self.__available=True
    @property
    def id(self):
        return self.__id
    
    @property
    def title(self):
        return self.__title
    
    @property
    def available(self):
        return self.__available    
    
    @available.setter
    def available(self,val):
        self.__available=val
    @abstractmethod
    def item_type(self):
        pass
    @abstractmethod
    def display(self):
        pass
    def __str__(self):
        return f"{self.id} | {self.item_type()} | {self.title} | {"Available" if self.available else "Not Available"}"

# 3. Book(LibraryItem):
#    - Extra: author, pages, genre
#    - item_type() → "Book"
#    - display() → full book details

class Book(LibraryItem):
    def __init__(self, title,author, pages, genre):
        super().__init__(title)
        self.author, self.pages, self.genre=author, pages, genre
    
    def item_type(self):
        return type(self).__name__
    def display(self):
        return f"{self.title} | {self.author} | {self.pages} | {self.genre}"
    
    
# 4. Magazine(LibraryItem):
#    - Extra: issue, publisher
#    - item_type() → "Magazine"
class Magazine(LibraryItem):
    def __init__(self, title,issue, publisher):
        super().__init__(title)
        self.issue, self.publisher=issue, publisher
    
    def item_type(self):
        return type(self).__name__
    def display(self):
        return f"{self.title} | {self.issue} | {self.publisher}"
    

# 5. Member class:
#    - Private: __id, __name, __borrowed (list)
#    - Properties: id, name, borrowed
#    - borrow(item) → adds to borrowed, marks item unavailable
#    - return_item(item) → removes from borrowed, marks available
#    - __str__ → "MEM-001 | Ali | 2 items borrowed"
class Member:
    count=0
    def __init__(self, name ):
        Member.count+=1
        self.__id=f"MEM-{Member.count:03}"
        self.__name=name
        self.__borrowed=[]

    def __str__(self):
        return f"{self.id} | {self.name} | {len(self.borrowed)} items Borrowed"

    @property
    def id(self):
        return self.__id
    @property
    def name(self):
        return self.__name
    @property
    def borrowed(self):
        return self.__borrowed
    def borrow(self,item):
        item.available=False
        self.borrowed.append(item)
    def return_item(self, item):
        if item not in self.__borrowed:
            raise ValueError("You didn't borrow this item")
        self.__borrowed.remove(item) 
        item._available = True         
    
# 6. Library class (composition):
#    - Holds items and members
#    - add_item(item) decorated with @log_calls
#    - register_member(member) decorated with @log_calls
#    - search(keyword) → generator, yields matching items
#    - available_items() → generator
#    - report() → formatted summary
class Library:
    def __init__(self):
        self.items = []
        self.members = []  
        
    @log_calls
    def add_item(self, item):
        self.items.append(item)
        
    @log_calls
    def register_member(self, member):
        self.members.append(member)
        
    def search(self, keyword):
        for item in self.items:
            if keyword.lower() in item.title.lower():
                yield item
                
    def available_items(self):
        for item in self.items:
            if item.available:
                yield item
                
    def report(self):
        total_items = len(self.items)
        available = sum(1 for item in self.items if item.available)
        total_members = len(self.members)
        active_borrows = sum(len(m.borrowed) for m in self.members)
        
        print("\n════════════════════════════════════")
        print("          LIBRARY REPORT")
        print("════════════════════════════════════")
        print(f"Total Items    : {total_items}")
        print(f"Available      : {available}")
        print(f"Total Members  : {total_members}")
        print(f"Active Borrows : {active_borrows}")
        print("════════════════════════════════════")
        print("ITEMS:")
        for item in self.items:
            status = "Available" if item.available else "Borrowed"
            print(f"  {item.id} | {item.item_type():<10} | {item.title:<11} | {status}")
        print("════════════════════════════════════")
        print("MEMBERS:")
        for m in self.members:
            plural = "s" if len(m.borrowed) != 1 else ""
            print(f"  {m.id} | {m.name:<11} | {len(m.borrowed)} item{plural} borrowed")
        print("════════════════════════════════════\n")
# Example:
# lib = Library()
# lib.add_item(Book("Clean Code", "Robert Martin", 464, "Programming"))
# lib.add_item(Magazine("TIME", "Issue 45", "Time Inc"))
# m = Member("Ali")
# lib.register_member(m)
# m.borrow(lib.search("Clean Code").__next__())
# lib.report()
# →
# ════════════════════════════════════
#          LIBRARY REPORT
# ════════════════════════════════════
# Total Items    : 2
# Available      : 1
# Total Members  : 1
# Active Borrows : 1
# ════════════════════════════════════
# ITEMS:
#   LIB-001 | Book       | Clean Code  | Borrowed
#   LIB-002 | Magazine   | TIME        | Available
# ════════════════════════════════════
# MEMBERS:
#   MEM-001 | Ali        | 1 item borrowed
# ════════════════════════════════════


# HARD (2) — [OOP + Regex + datetime + Generators + 
#             Decorators + Collections + Error Handling]

# Build a Student Grade Management System:

# 1. @validate decorator — validates all inputs before
#    any method runs, raises TypeError for wrong types

# 2. @dataclass Grade:
#    - subject, score, date, letter_grade (auto calculated)
#    - __post_init__ validates score 0-100
#    - letter grade: A=90+, B=80+, C=70+, D=60+, F

# 3. Student class:
#    - Private: __id, __name, __grades (list of Grade)
#    - Properties: id, name, grades
#    - add_grade(subject, score) decorated with @validate
#    - average() → overall average
#    - best_subject() → highest scoring subject
#    - worst_subject() → lowest scoring subject
#    - grade_report() → generator yielding one grade at a time
#    - __str__ → "STU-001 | Ali | Avg: 89.5 | Grade: A"

# 4. GradeBook class (composition):
#    - Holds list of Student objects
#    - add_student(name) decorated with @validate
#    - get_student(name) → search by name using regex
#    - top_students(n) → returns top n by average
#    - class_statistics() → mean, highest, lowest, Counter of grades
#    - report() → full formatted report

# Example:
# gb = GradeBook()
# gb.add_student("Ali")
# gb.add_student("Sara")
# gb.get_student("ali").add_grade("Math", 92)
# gb.get_student("ali").add_grade("Python", 88)
# gb.get_student("sara").add_grade("Math", 75)

# gb.report()
# →
# ════════════════════════════════════
#         GRADE BOOK REPORT
# ════════════════════════════════════
# Students : 2
# Class Avg: 85.0
# ════════════════════════════════════
# STU-001 | Ali  | Avg: 90.0 | A
#   Math   : 92 (A) — 15-01-2024
#   Python : 88 (B) — 15-01-2024
# ────────────────────────────────────
# STU-002 | Sara | Avg: 75.0 | C
#   Math   : 75 (C) — 15-01-2024
# ════════════════════════════════════
# TOP STUDENTS:
#   1. Ali  — 90.0
#   2. Sara — 75.0
# ════════════════════════════════════

from dataclasses import dataclass, field
from datetime import date
from collections import Counter
import re
import inspect
from functools import wraps

# 1. @validate decorator
def validate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        
        for name, value in bound_args.arguments.items():
            expected_type = sig.parameters[name].annotation
            if expected_type is not inspect._empty and name != 'self':
                if not isinstance(value, expected_type):
                    raise TypeError(f"Argument '{name}' must be of type {expected_type.__name__}, got {type(value).__name__}")
        return func(*args, **kwargs)
    return wrapper

# 2. @dataclass Grade
@dataclass
class Grade:
    subject: str
    score: float
    date_recorded: date = field(default_factory=date.today)
    letter_grade: str = field(init=False)

    def __post_init__(self):
        if not (0 <= self.score <= 100):
            raise ValueError("Score must be between 0 and 100")
        
        if self.score >= 90: self.letter_grade = 'A'
        elif self.score >= 80: self.letter_grade = 'B'
        elif self.score >= 70: self.letter_grade = 'C'
        elif self.score >= 60: self.letter_grade = 'D'
        else: self.letter_grade = 'F'

# 3. Student class
class Student:
    count = 0
    def __init__(self, name: str):
        Student.count += 1
        self.__id = f"STU-{Student.count:03}"
        self.__name = name
        self.__grades = []

    @property
    def id(self): return self.__id
    
    @property
    def name(self): return self.__name
    
    @property
    def grades(self): return self.__grades

    @validate
    def add_grade(self, subject: str, score: float | int):
        self.__grades.append(Grade(subject=subject, score=float(score)))

    def average(self):
        if not self.__grades:
            return 0.0
        return sum(g.score for g in self.__grades) / len(self.__grades)

    def best_subject(self):
        if not self.__grades: return None
        return max(self.__grades, key=lambda g: g.score).subject

    def worst_subject(self):
        if not self.__grades: return None
        return min(self.__grades, key=lambda g: g.score).subject

    def grade_report(self):
        for grade in self.__grades:
            yield grade

    def __str__(self):
        avg = self.average()
        # Derive general grade from average using Grade class logic
        overall = Grade("Overall", avg).letter_grade if self.__grades else "N/A"
        return f"{self.id} | {self.name:<4} | Avg: {avg:<4.1f} | {overall}"

# 4. GradeBook class (composition)
class GradeBook:
    def __init__(self):
        self.students = []

    @validate
    def add_student(self, name: str):
        self.students.append(Student(name))

    def get_student(self, name: str):
        pattern = re.compile(f"^{name}$", re.IGNORECASE)
        for student in self.students:
            if pattern.match(student.name):
                return student
        raise ValueError(f"Student '{name}' not found.")

    def top_students(self, n: int):
        sorted_students = sorted(self.students, key=lambda s: s.average(), reverse=True)
        return sorted_students[:n]

    def class_statistics(self):
        all_grades = [g for s in self.students for g in s.grades]
        if not all_grades:
            return None
        
        mean = sum(g.score for g in all_grades) / len(all_grades)
        highest = max(all_grades, key=lambda g: g.score)
        lowest = min(all_grades, key=lambda g: g.score)
        grade_counter = Counter(g.letter_grade for g in all_grades)
        
        return mean, highest, lowest, grade_counter

    def report(self):
        all_grades = [g for s in self.students for g in s.grades]
        class_avg = (sum(g.score for g in all_grades) / len(all_grades)) if all_grades else 0.0

        print("════════════════════════════════════")
        print("         GRADE BOOK REPORT")
        print("════════════════════════════════════")
        print(f"Students : {len(self.students)}")
        print(f"Class Avg: {class_avg:.1f}")
        print("════════════════════════════════════")
        
        for idx, student in enumerate(self.students):
            print(student)
            for grade in student.grade_report():
                date_str = grade.date_recorded.strftime("%d-%m-%Y")
                print(f"  {grade.subject:<6} : {grade.score:g} ({grade.letter_grade}) — {date_str}")
            
            if idx < len(self.students) - 1:
                print("────────────────────────────────────")
                
        print("════════════════════════════════════")
        print("TOP STUDENTS:")
        top = self.top_students(min(3, len(self.students)))
        for i, student in enumerate(top, 1):
            print(f"  {i}. {student.name:<4} — {student.average():.1f}")
        print("════════════════════════════════════\n")


# --- GradeBook Example Execution ---
gb = GradeBook()
gb.add_student("Ali")
gb.add_student("Sara")
gb.get_student("ali").add_grade("Math", 92)
gb.get_student("ali").add_grade("Python", 88)
gb.get_student("sara").add_grade("Math", 75)

gb.report()
