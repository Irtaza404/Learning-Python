# DAY 15 — OOP PRACTICE
# ════════════════════════

# TASK 1 — [Class + __init__ + Methods]
# Create a Calculator class with:
# - Instance variable: history = [] (stores all calculations)
# - Methods: add(), subtract(), multiply(), divide()
# - Each method stores result in history
# - Method show_history() prints all past calculations
# - Validate division by zero

class Calculator:
    def __init__(self):
            self.history=[]
    def solve(self,a,b,op):
        result=None
        match op:
            case "+":result=a+b
            case "-":result=a-b
            case "*":result=a*b
            case "/":result=a/b
        self.history.append(f"{a} {op} {b} = {result}")
        return result
        
    def add(self,a,b):
        return self.solve(a,b,"+")
    def subtract(self,a,b):
        return self.solve(a,b,"-")
    def multiply(self,a,b):
        return self.solve(a,b,"*")
    def divide(self,a,b):
        if b!=0:
            return self.solve(a,b,"/")
        print("Cannot divide by 0")
        
    def show_history(self):
        for h in self.history:
            print(h)        


# Example:
# c = Calculator()
# c.add(10, 5)  #      → 15
# c.subtract(10, 3) #  → 7
# c.divide(10, 0)    # → ValueError
# c.show_history()
# # → 10 + 5 = 15
# # → 10 - 3 = 7


# TASK 2 — [Class + __init__ + __str__ + __repr__ + Methods]
# Create a Student class with:
# - Class variable: school = "BIIT", total_students = 0
# - Instance variables: name, age, scores (list)
# - Auto generate student_id (BIIT-1, BIIT-2 etc.)
# - Method average() → returns average of scores
# - Method grade() → returns letter grade
# - __str__ → "Ali | BIIT-1 | Avg: 89.0 | Grade: A"
# - __repr__ → "Student('Ali', 20, [90, 85, 92])"

class Student:
    school="BIIT"
    total_students=0
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
        Student.total_students+=1
        self.student_ID= Student.school+str(Student.total_students)
        self.avg=self.average()
        self.Grade=self.grade()
    
    def average(self):
        return sum(self.score)/len(self.score)
    def grade(self):
        return "A" if self.avg>85 else "B" if self.avg >75 else "C" if self.avg>65 else "D" if self.avg>50 else "F"
    def __str__(self):
        return f"{self.name} | {self.student_ID} | Avg: {self.avg} | Grade: {self.Grade}"
    def __repr__(self):
        return f"Student({self.name},{self.age},{self.score})"
    
# Example:
# s1 = Student("Ali", 20, [90, 85, 92])
# s2 = Student("Sara", 21, [78, 82, 80])
# print(s1)         #  → "Ali | BIIT-1 | Avg: 89.0 | Grade: A"
# Student.total_students #→ 2




# TASK 3 — [Class + __init__ + Methods + Error Handling]
# Create an Inventory class with:
# - Class variable: total_items = 0
# - Instance variables: name, price, stock
# - Validate price > 0 and stock >= 0
# - Methods:
#   - restock(amount) → adds to stock
#   - sell(amount) → reduces stock, raise error if insufficient
#   - total_value() → price * stock
# - __str__ → "Keyboard | Stock: 10 | Value: Rs.20,000"

class Inventory():
    total_items=0
    def __init__(self,name,price,stock):
        if price<=0:
            raise ValueError("price cannot be equal or lower than zero")
        if stock<0:
            raise ValueError("stock cannot be lower than zero")        
        self.name=name
        self.price=price
        self.stock=stock
        Inventory.total_items+=1
    def restock(self,amount):
        if amount<=0:
            raise ValueError("restock  amount cannot be equal or lower than zero")
        self.stock+=amount
    def sell(self,amount):
        if amount>self.stock:
            raise ValueError("Insufficient stock")
        self.stock+=amount
    def total_value(self):
        return  self.price * self.stock

    def __str__(self):
        return f"{self.name} | Stock: {self.stock} | Value: Rs.{self.total_value()}"
    
# Example:
# item = Inventory("Keyboard", 2000, 10)
# item.sell(3)        → stock = 7
# item.restock(5)     → stock = 12
# item.sell(20)       → ValueError: "Insufficient stock"
# print(item)         → "Keyboard | Stock: 12 | Value: Rs.24,000"


# TASK 4 — [Class + __init__ + Methods + datetime]
# Create a TodoList class with:
# - Instance variable: tasks = []
# - Each task stored as dict:
#   {task, priority, created_at, done}
# - Methods:
#   - add_task(task, priority="low")
#   - complete_task(task) → marks as done
#   - pending_tasks() → returns incomplete tasks
#   - show_all() → prints all tasks formatted
from datetime import datetime
class ToDoList:
    def __init__(self):
        self.tasks=[]
    
    def add_task(self,task, priority="low"):
        self.tasks.append({
            "task": task,
            "priority": priority,
            "created_at": datetime.now(),  # datetime
            "done": False                # bool
        })
    def complete_task(self,task):
        for t in self.tasks:
            if t["task"] == task:
                t["done"] = True
    def pending_tasks(self):
        return [t["task"] for t in self.tasks if not t["done"]]
    def show_all(self):
        for t in self.tasks:
            if t["done"]:
                print(f"[✓] {t["task"]} ({t["priority"]}) -{t["created_at"]} ")
            else:
                print(f"[✗] {t["task"]} ({t["priority"]}) -{t["created_at"]} ")
    
# Example:
# todo = TodoList()
# todo.add_task("Study OOP", "high")
# todo.add_task("Push to GitHub", "low")
# todo.complete_task("Study OOP")
# todo.pending_tasks() → ["Push to GitHub"]
# todo.show_all()
# → [✓] Study OOP (high) - 2024-01-15
# → [ ] Push to GitHub (low) - 2024-01-15A
