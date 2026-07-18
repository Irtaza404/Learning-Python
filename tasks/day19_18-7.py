# DAY 19 — MEDIUM PRACTICE
# ════════════════════════

# MEDIUM (1) — [OOP + Inheritance + @property + Encapsulation]
# Build a Bank System:
# - Abstract base Account: __account_no, __balance (private)
#   - @property balance, account_no (read only)
#   - abstract methods: deposit(), withdraw(), account_type()
#   - __str__ → "ACC-001 | Savings | Rs.10,000"

from abc import ABC,abstractmethod
class Account(ABC):
    count=0
    def __init__(self,name,balance):
        Account.count+=1
        self.__account_no=f"ACC-{Account.count:03}"
        self.name=name
        self._balance=balance
        
    def __str__(self):
        return f"{self.__account_no} | {self.account_type()} | Rs.{self.balance}"
    @property
    def balance(self):
        return self._balance
    
    @property
    def account_no(self):
        return self.__account_no
    
    @abstractmethod
    def deposit(self,amount):
        pass
    @abstractmethod
    def withdraw(self,amount):
        pass
    @abstractmethod
    def account_type(self):
        pass
    
# - SavingsAccount(Account):
#   - Extra: interest_rate (default 5%)
#   - deposit() → adds amount
#   - withdraw() → minimum balance Rs.1000 must remain
#   - add_interest() → adds interest to balance
#   - account_type() → "Savings"
class SavingsAccount(Account):
    def __init__(self, name, balance,interest_rate=0.05):
        super().__init__(name, balance)
        self.interest_rate=interest_rate
    
    def deposit(self, amount):
        if amount<0:
            raise ValueError("amount cannot be in negitive")
        self._balance+=amount

    def withdraw(self, amount):
        if amount<0:
            raise ValueError("amount cannot be in negitive")
        if self.balance - amount < 1000:
            raise ValueError("minimum balance Rs.1000 must remain")
        self._balance-=amount
    
    def add_interest(self):
        interest_amount=self._balance*self.interest_rate
        self._balance+=interest_amount
        return f"balance ={self.balance} ({self.interest_rate*100})"
    
    def account_type(self):
        return type(self).__name__
    
    
# - CurrentAccount(Account):
#   - Extra: overdraft_limit (default 5000)
#   - withdraw() → can go negative up to overdraft limit
#   - account_type() → "Current"
class CurrentAccount(Account):
    def __init__(self, name, balance,overdraft_limit=5000):
        super().__init__(name, balance)
        self.overdraft_limit=overdraft_limit
    
    def deposit(self, amount):
        if amount<0:
            raise ValueError("amount cannot be in negitive")
        self._balance+=amount

    def withdraw(self, amount):
        if self.balance - amount < -self.overdraft_limit:
            raise ValueError("Overdraft limit exceeded")
        self._balance -= amount
    def account_type(self):
        return type(self).__name__
    


# Example:
s = SavingsAccount("Ali", 10000)
s.withdraw(14500)   #→ ValueError: minimum balance Rs.1000
s.deposit(5000)     #→ balance = 15000
s.add_interest()    #→ balance = 15750 (5%)
print(s)            #→ "ACC-001 | Savings | Rs.15,750"


# MEDIUM (2) — [Composition + Operator Overloading + @dataclass]
# Build a Shopping Cart system:

# @dataclass Product: name, price, quantity
#   - __str__ → "Keyboard x2 — Rs.4,000"
#   - __mul__ → multiplies price by quantity
#   - __eq__ → compares by name

from dataclasses import dataclass
@dataclass(eq=False)
class Product:
    name:str
    price:int
    quantity:int
    def __str__(self):
        return f"{self.name} x{self.quantity} - Rs.{self.__mul__()}"
    def __mul__(self, other):  # ← correct signature
        return self.price * self.quantity
    def __eq__(self, other):
        return self.name == other.name
    
# ShoppingCart class (composition):
#   - holds list of Product objects
#   - __add__ → adds product to cart
#   - __sub__ → removes product by name
#   - __len__ → number of items
#   - __str__ → prints all items formatted
#   - total() → sum of all (price * quantity)
#   - apply_discount(percent) → reduces all prices

class ShoppingCart:
    def __init__(self):
        self.cart=[]
    def __add__(self, other):
        self.cart.append(other)
        return self
    def __sub__(self, name):
        self.cart = [p for p in self.cart if p.name != name]
        return self
    def total(self):
        return sum(p.__mul__() for p in self.cart)
    def apply_discount(self, percent):
        for p in self.cart:
            p.price -= p.price * percent / 100
    def __len__(self):
        return len(self.cart)
    
    
# Example:
cart = ShoppingCart()
cart + Product("Keyboard", 2000, 2)
cart + Product("Mouse", 1500, 1)
cart.total()          #→ 5500
cart.apply_discount(10)
cart.total()          #→ 4950
cart - "Mouse"
len(cart)             #→ 1


# MEDIUM (3) — [Generators + Decorators + OOP + datetime]
# Build a Task Manager system:
import time
from datetime import datetime
from dataclasses import dataclass,field
def log_time(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"[{func.__name__}] took {(end-start)*1000:.2f}ms")
        return result
    return wrapper

# - @log_time decorator that measures execution time
# - Task dataclass: title, priority, created_at, done=False
# - TaskManager class:
#   - tasks: list of Task objects
#   - add_task(title, priority) — decorated with @log_time
#   - complete_task(title)
#   - generator pending_tasks() — yields incomplete tasks
#   - generator tasks_by_priority(priority) — yields filtered
#   - report() — prints formatted summary
@dataclass
class Task:
    title: str
    priority: str
    created_at: datetime = field(default_factory=datetime.now)
    done: bool = False

class TaskManager:
    def __init__(self):
        self.tasks = []
    @log_time
    def add_task(self, title, priority):
        self.tasks.append(Task(title, priority))
    
    def complete_task(self, title):
        for t in self.tasks:
            if t.title == title:
                t.done = True
    def pending_tasks(self):
        for t in self.tasks:
            if not t.done:
                yield t
    def tasks_by_priority(self, priority):
        for t in self.tasks:
            if t.priority == priority and not t.done:
                yield t
    def report(self):
        completed = sum(1 for t in self.tasks if t.done)
        pending = len(self.tasks) - completed
        print("═" * 26)
        print(f"{'TASK MANAGER':^26}")
        print("═" * 26)
        print(f"  Total    : {len(self.tasks)}")
        print(f"  Completed: {completed}")
        print(f"  Pending  : {pending}")
        print("═" * 26)
        for t in self.tasks:
            symbol = "✓" if t.done else " "
            print(f"  [{symbol}] {t.title} ({t.priority})")
        print("═" * 26)
# Example:
# tm = TaskManager()
# tm.add_task("Study OOP", "high")
# tm.add_task("Push GitHub", "low")
# tm.add_task("Practice Regex", "high")
# tm.complete_task("Study OOP")

# list(tm.pending_tasks())
# → [Task("Push GitHub"), Task("Practice Regex")]

# list(tm.tasks_by_priority("high"))
# → [Task("Practice Regex")]

# tm.report()
# → ════════════════════════
#       TASK MANAGER
#   ════════════════════════
#   Total    : 3
#   Completed: 1
#   Pending  : 2
#   ════════════════════════
#   [✓] Study OOP (high)
#   [ ] Push GitHub (low)
#   [ ] Practice Regex (high)
#   ════════════════════════

