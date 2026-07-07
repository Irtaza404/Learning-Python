# Here are all topics:
# Core Basics

# Variables and data types
# String methods and f-strings
# String format specifiers
# String prefixes (f, r, b, u)
# Operators (arithmetic, comparison, logical, bitwise, augmented)
# Operator precedence

# Control Flow
# 7. Conditionals (if/elif/else)
# 8. match/case
# 9. Loops (for, while, break, continue, else)
# 10. range()
# 11. Walrus operator :=
# Data Structures
# 12. Lists (methods, comprehension, nested)
# 13. Tuples and Sets
# 14. Dictionaries
# Functions
# 15. Parameters, return, default args
# 16. *args and **kwargs
# 17. Positional only / keyword only parameters
# 18. Scope
# 19. Recursion
# 20. Decorators
# 21. Closures
# 22. Higher order functions
# 23. Lambda
# Built-in Tools
# 24. map() and filter()
# 25. Generators and yield
# 26. Generator expressions
# 27. zip() and enumerate()
# Error Handling
# 28. try/except/else/finally
# 29. raise and custom exceptions
# 30. Common exceptions
# Modules
# 31. random
# 32. math
# 33. time
# 34. datetime
# 35. collections
# 36. re (regex)

# 1.Variables & Data Types

# x = 10          # int
# x = 3.14        # float
# x = "Irtaza"    # str
# x = True        # bool
# x = None        # NoneType

# Check type with type() or isinstance():

# type(10)          # → int
# isinstance(10, int)  # → True

# None is not 0 or False — it means "nothing":

# print(bool(None)) #True

# bool is a subclass of int:

# True + True   # → 2
# True == 1     # → True
# False == 0    # → True

# 2.String Methods & f-strings
# Common string methods:

# s = "hello world"

# s.upper()          # → "HELLO WORLD"
# s.lower()          # → "hello world"
# s.title()          # → "Hello World"
# s.strip()          # → removes whitespace from both ends
# s.split()          # → ["hello", "world"]
# s.replace("hello", "hi")  # → "hi world"
# s.startswith("he") # → True
# s.endswith("ld")   # → True
# s.find("world")    # → 6 (index)
# s.count("l")       # → 3
# s.isdigit()        # → False
# s.isalpha()        # → False

# String is immutable — can't change in place:

# s = "hello"
# s[0] = "H"  # → ERROR
# s = "H" + s[1:]  # → correct way

# 3.String Format Specifiers
# Used inside f-strings with : to control how values look.

# # Numbers:
# x = 1234567.891

# print(f"{x:,.2f}")    # → "1,234,567.89"  (comma + 2 decimals)
# print(f"{x:.2f}" )    # → "1234567.89"    (2 decimals only)
# print(f"{x:e}"   )    # → "1.234568e+06"  (scientific)
# print(f"{877/1200:%}"   )    # → "123456789.10%" (percentage)


# s = "Irtaza"

# f"{s:<10}"    # → "Irtaza    "  (left)
# f"{s:>10}"    # → "    Irtaza"  (right)
# f"{s:^10}"    # → "  Irtaza  "  (center)
# f"{s:*^10}"   # → "**Irtaza**"  (center with fill char)

# Integers:
# n = 255

# f"{n:b}"      # → "11111111"  (binary)
# f"{n:x}"      # → "ff"        (hex)
# f"{n:o}"      # → "377"       (octal)
# f"{n:08b}"    # → "11111111"  (padded to 8 digits)

# Width + decimals together:
# pythonf"{'Item':<15} {'Price':>10}"
# print(f"{'Laptop':<15} {150000.5:>10.2f}")
# → "Laptop          150,000.50"

# The formula for any table:
# f"{value:{align}{width}{format}}"

# align → < left, > right, ^ center
# width → how many characters wide
# format → .2f, , etc.


# Rule 1 — decide column widths first:
# Product → 15 chars
# Price   → 10 chars  
# Qty     → 8 chars

# Rule 2 — header and rows use same widths:
# # header
# f"{'Product':<15} {'Price':>10} {'Qty':^8}"

# # row (same widths, different alignment)
# f"{'Laptop':<15} {150000.5:>10,.2f} {3:^8}"

# Rule 3 — separator line matches total width:
# total_width = 15 + 10 + 8 + spaces
# "═" * total_width

# Rule 4 — borders with ║:
# f"║ {'Product':<15} ║ {'Price':>10} ║ {'Qty':^8} ║"

# That's literally it — pick widths, keep them consistent across header/rows/total, add border chars if needed.

# r — raw string
# Ignores escape characters like \n, \t. Used mainly in regex and file paths:

# print("\n")    # → new line
# print(r"\n")   # → literally \n

# path = r"C:\Users\Irtaza\Documents"  # no need to escape backslashes
# pattern = r"\d+\.\d+"  # regex pattern

# b — bytes string
# Used for binary data, networking, file I/O:

# x = b"hello"
# type(x)        # → bytes not str
# x[0]           # → 104 (ASCII value not character)

# # convert between bytes and str
# print("hello".encode())# str → bytes
# print(x[0])
# b"hello".decode()    # bytes → str

# rb"\d+"   # raw bytes — used in binary regex
# Operators
# You know most of these from Java — I'll focus on Python-specific ones.

# Arithmetic — same as Java:
# python10 + 3   # 13
# 10 - 3   # 7
# 10 * 3   # 30
# 10 / 3   # 3.333  (always float in Python)
# 10 // 3  # 3      (floor division)
# 10 % 3   # 1      (modulo)
# 10 ** 3  # 1000   (power — no Math.pow needed)

# Comparison — same as Java:
# python==, !=, >, <, >=, <=

# Logical — different from Java:
# python# Java: &&, ||, !
# # Python:
# and, or, not

# Identity & Membership — Python only:
# pythonx is None      # checks same object in memory
# x is not None
# "a" in "Irtaza"    # → True
# 5 in [1,2,3,4,5]   # → True
# 5 not in [1,2,3]   # → True

# Bitwise — same as Java:
# python&   # AND
# |   # OR
# ^   # XOR
# ~   # NOT
# <<  # left shift
# >>  # right shift

# Walrus := — Python only:
# Assign and use in same expression:
# pythonif (n := len(data)) > 10:
#     print(f"Too long: {n}")

# Augmented assignment:
# pythonx += 1
# x -= 1
# x **= 2
# x //= 3
# x &= 0b1111

# In Python, these objects are always the same in memory:

# None — only one exists:
# pythonx = None
# y = None
# x is y  # → True always

# True and False:
# pythonx = True
# y = True
# x is y  # → True always

# Small integers (-5 to 256) — Python caches these:
# pythona = 100
# b = 100
# a is b  # → True (cached)

# a = 1000
# b = 1000
# a is b  # → False (not cached, new object each time)

# Short strings — Python caches simple strings:
# pythona = "hello"
# b = "hello"
# a is b  # → True (cached)

# a = "hello world!"
# b = "hello world!"
# a is b  # → False (not guaranteed)

# Rule of thumb:

# Always use is for None, True, False
# Always use == for comparing values like numbers and strings

# python# correct
# if x is None: ...
# if x is True: ...

# # correct
# if x == 10: ...
# if x == "Irtaza": ...

# why and how  they are sameGreat question. It's about how Python manages memory.

# Python uses a concept called "interning"
# Instead of creating a new object every time, Python reuses the same object in memory for certain values.

# How it works:
# When Python starts up, it pre-creates objects for:

# None — only one None object ever exists
# True and False — only one of each ever exists
# Integers -5 to 256 — pre-created at startup
# Simple strings — created once and reused


# Visual example:
# pythona = 100
# b = 100
# Memory looks like this:
# a ──→ [100]  ← same object
# b ──→ [100]  ←
# pythona = 1000
# b = 1000
# Memory looks like this:
# a ──→ [1000]  ← different objects
# b ──→ [1000]  ←

# Why -5 to 256?
# Python creators decided these numbers are used so frequently in everyday code that pre-creating them saves memory and speeds things up. Beyond 256 it's not worth it.

# Check memory address yourself with id():
# pythona = 100
# b = 100
# print(id(a) == id(b))  # → True (same address)

# a = [0 for _ in range(6) ]
# b = [1,2,3]
# print(a)
# print(id(a[0]))
# print(id(a[5]))
# print(id(a) == id(b))  # → False (different address)
# id() returns the memory address of an object — if two variables have the same id() they point to the same object.


# how man if these object are created once then how we use them on different place . and if we change it for one variable then by it not change for other as well

# Great thinking — this is the key concept.

# Variables are just labels, not boxes

# In Java you think of variables as boxes that hold values.
# In Python variables are just labels pointing to objects.

# python
# a = 100
# b = 100
# a ──→ [100 object in memory]
# b ──→ [100 object in memory]
# Both labels point to the same object.

# When you "change" a variable you just move the label:

# python
# a = 100
# b = a
# a = 200  # a's label moves to new object
# a ──→ [200]  ← moved here
# b ──→ [100]  ← still here, unchanged
# b didn't change because you only moved a's label. The 100 object itself never changed.

# This is why it works — objects never change, labels move

# None, True, False, small integers — these objects are immutable (can never be modified). So sharing them is completely safe.

# If you could modify 100 itself then yes, it would affect everyone pointing to it. But you can't — you can only move your label to a different object.

# Mutable objects behave differently:

# python
# a = [1, 2, 3]
# b = a          # both point to same list
# a.append(4)    # modifies the actual object
# print(b)       # → [1, 2, 3, 4]  ← b is affected!
# Here the list IS modified in place so b sees the change.

# Summary:

# Immutable (int, str, bool, None) → safe to share, labels just move
# Mutable (list, dict, set) → shared object, changes affect everyone pointing to it

# # Java: x > 0 && x < 10
# # Python:
# if 0 < x < 10:  # cleaner!
#     print("in range")

# # These are all False:
# False, None, 0, 0.0, "", [], {}, set()

# # Everything else is True

# match command:
#     case "start":
#         print("starting")
#     case "stop":
#         print("stopping")
#     case "pause" | "wait":  # multiple values
#         print("pausing")
#     case _:                 # default
#         print("unknown")

# match day:
#     case 1 | 2 | 3 | 4 | 5: print("Weekday")
#     case 6 | 7:              print("Weekend")


# match age:
#     case age if age < 18: print("Minor")
#     case age if age < 65: print("Adult")
#     case _:               print("Senior")


# match items:
#     case []:           print("empty")
#     case [x]:          print(f"one: {x}")
#     case [x, y]:       print(f"two: {x},{y}")
#     case [x, *rest]:   print(f"first:{x} rest:{rest}")

# match command.split():
#     case ["go", direction]:
#         print(f"Going {direction}")
#     case ["go", direction, speed]:
#         print(f"Going {direction} at {speed}")
#     case ["stop"]:
#         print("Stopping")

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# match point:
#     case Point(x=0, y=0): print("Origin")
#     case Point(x=0, y=y): print(f"Y axis {y}")
#     case Point(x=x, y=0): print(f"X axis {x}")
#     case Point(x=x, y=y): print(f"Point {x},{y}")

# match command:
#     case ("go" | "move") as action:
#         print(f"Moving action: {action}")
#     case ("stop" | "halt") as action:
#         print(f"Stop action: {action}")

# match response:
#     case {"status": 200, "data": {"user": name}}:
#         print(f"Found user: {name}")
#     case {"status": 404}:
#         print("Not found")
#     case {"status": status} if status >= 500:
#         print(f"Server error: {status}")

# match response:
#     case {"status": 200, "data": {"user": name}}:
#         print(f"Found user: {name}")
#     case {"status": 404}:
#         print("Not found")
#     case {"status": status} if status >= 500:
#         print(f"Server error: {status}")

# Loops — Quick Review

# for:
# pythonfor i in range(5):      print(i)
# for item in list:       print(item)
# for i, v in enumerate(list): print(i, v)
# for k, v in dict.items():    print(k, v)

# while:
# pythonwhile condition:
#     # runs while condition is True

# while True:             # infinite loop
#     if condition:
#         break

# break, continue, else:
# python# break — exit loop
# for i in range(10):
#     if i == 5: break    # stops at 5

# # continue — skip iteration
# for i in range(10):
#     if i == 5: continue # skips 5

# # else — runs if loop finished WITHOUT break
# for i in range(5):
#     if i == 10: break
# else:
#     print("No break hit")   # runs ✅

# 1 — enumerate()
# Returns index AND value together:
# pythonnames = ["Irtaza", "Ali", "Sara"]

# # without enumerate
# for i in range(len(names)):
#     print(i, names[i])

# # with enumerate — cleaner
# for i, name in enumerate(names):
#     print(i, name)

# # Output:
# # 0 Irtaza
# # 1 Ali
# # 2 Sara

# Custom start index:
# pythonfor i, name in enumerate(names, start=1):  # start from 1
#     print(i, name)
# # 1 Irtaza
# # 2 Ali
# # 3 Sara

# 2 — Loop else — ONLY runs when no break hit
# python# break hit — else SKIPPED
# for i in range(5):
#     if i == 3:
#         break
# else:
#     print("runs")   # ❌ doesn't run

# # no break — else RUNS
# # for i in range(5):
# #     if i == 10:     # never true
# #         break
# # else:
# #     print("runs")   # ✅ runs

# # Nothing else skips it — only break:
# # python# continue — else still runs
# # for i in range(5):
# #     if i == 3:
# #         continue    # skip 3
# # else:
# #     print("runs")   # ✅ still runs!

# # # return inside function — else skipped
# # def test():
# #     for i in range(5):
# #         if i == 3:
# #             return  # exits function
# #     else:
# #         print("runs")   # ❌ doesn't run

# # Real world use — search pattern:
# # python# Classic use — searching
# # users = ["Ali", "Sara", "Khan"]

# # for user in users:
# #     if user == "Irtaza":
# #         print("Found!")
# #         break
# # else:
# #     print("Not found!")     # only runs if never found

# Walrus Operator := — Quick Review

# Assign AND use in same expression:
# python# without walrus — two lines
# data = input()
# while data != "quit":
#     data = input()

# # with walrus — one line
# while (data := input()) != "quit":
#     print(data)

# Other uses:
# python# in if
# if (n := len(name)) > 5:
#     print(f"Long name: {n} chars")

# # in list comprehension
# results = [y for x in range(10) if (y := x**2) > 25]

# # in while with processing
# while chunk := file.read(1024):
#     process(chunk)

# Key rule:
# Always wrap in () when used in condition
# while (x := input()) != "quit"  ✅
# while x := input() != "quit"    ❌ wrong precedence


# Walrus Operator := — Quick Review

# Assign AND use in same expression:
# python# without walrus — two lines
# data = input()
# while data != "quit":
#     data = input()

# # with walrus — one line
# while (data := input()) != "quit":
#     print(data)

# Other uses:
# python# in if
# if (n := len(name)) > 5:
#     print(f"Long name: {n} chars")

# # in list comprehension
# results = [y for x in range(10) if (y := x**2) > 25]

# # in while with processing
# while chunk := file.read(1024):
#     process(chunk)

# Key rule:
# Always wrap in () when used in condition
# while (x := input()) != "quit"  ✅
# while x := input() != "quit"    ❌ wrong precedence

# Lists — Quick Review

# Creating:
# pythonnumbers = [1, 2, 3, 4, 5]
# mixed   = [1, "hello", 3.14, True]
# empty   = []
# nested  = [[1,2], [3,4], [5,6]]

# Indexing & Slicing:
# pythonlst = [1, 2, 3, 4, 5]
# lst[0]      # 1
# lst[-1]     # 5
# lst[1:3]    # [2, 3]
# lst[::-1]   # [5, 4, 3, 2, 1]

# Methods:
# pythonlst.append(6)       # add to end
# lst.insert(0, 99)   # add at index
# lst.remove(3)       # remove first occurrence
# lst.pop()           # remove last
# lst.pop(0)          # remove at index
# lst.sort()          # sort in place
# lst.reverse()       # reverse in place
# lst.index(4)        # find index
# lst.count(2)        # count occurrences
# lst.copy()          # make copy
# lst.clear()         # empty list
# lst.extend([7,8])   # add another list

# Comprehension:
# pythonsquares = [x**2 for x in range(10)]
# evens   = [x for x in range(10) if x%2==0]


# Tuples & Sets — Quick Review

# Tuples:
# pythont = (1, 2, 3)       # immutable
# t[0]                # indexing ✅
# t[0] = 99           # ❌ cannot modify

# # unpacking
# a, b, c = t
# first, *rest = t

# # only 2 methods
# t.count(1)
# t.index(2)

# Sets:
# pythons = {1, 2, 3, 3, 2}    # {1, 2, 3} — no duplicates
# s = set()               # empty set — NOT {}

# # methods
# s.add(4)
# s.remove(1)             # error if missing
# s.discard(1)            # safe — no error
# s.pop()                 # random item

# # operations
# a | b       # union
# a & b       # intersection
# a - b       # difference
# a ^ b       # symmetric difference

# When to use:
# List  → ordered, changeable, duplicates ok
# Tuple → fixed data, faster, dict key
# Set   → unique items, fast lookup, math ops

# Anything to go deeper on? 👇

# Dictionaries — Quick Review

# Creating:
# pythonperson = {"name": "Irtaza", "age": 25}
# empty  = {}

# Accessing:
# pythonperson["name"]              # ❌ KeyError if missing
# person.get("name")          # ✅ None if missing
# person.get("phone", "N/A")  # ✅ default if missing

# Adding & Modifying:
# pythonperson["city"] = "London"   # add new
# person["age"]  = 26         # modify existing

# Methods:
# pythonperson.keys()       # all keys
# person.values()     # all values
# person.items()      # key-value pairs
# person.update({})   # merge another dict
# person.pop("age")   # remove and return
# person.copy()       # make copy
# person.clear()      # empty dict
# person.setdefault("city", "Unknown")  # get or set default

# Looping:
# pythonfor key in person:              # keys
# for val in person.values():     # values
# for k, v in person.items():     # both

# Comprehension:
# pythonsquares = {x: x**2 for x in range(5)}

# Nested:
# pythonusers = {
#     "user1": {"name": "Irtaza", "age": 25},
#     "user2": {"name": "Ali",    "age": 30}
# }
# users["user1"]["name"]      # Irtaza

# Yes! This is called Pass by Reference for mutable objects:
# pythondef add_item(lst):
#     lst.append(99)

# numbers = [1, 2, 3]
# add_item(numbers)
# print(numbers)      # [1, 2, 3, 99] — MODIFIED! 😱

# Why?
# When you pass a list — you're passing the memory address not a copy:
# numbers → 0x100 → [1, 2, 3]

# add_item(numbers)
#     lst → 0x100 → same list!
#     lst.append(99) → modifies 0x100
    
# numbers → 0x100 → [1, 2, 3, 99]  ← changed!

# Immutable — safe, original never changes:
# pythondef change(x):
#     x += 10         # creates NEW object
#     print(x)        # 15

# num = 5
# change(num)
# print(num)          # 5 — unchanged ✅

# How to protect original — pass a copy:
# python# Method 1 — slice copy
# add_item(numbers[:])

# # Method 2 — .copy()
# add_item(numbers.copy())

# # Method 3 — list()
# add_item(list(numbers))

# Same applies to dict and set:
# pythondef modify(d):
#     d["new"] = 99

# person = {"name": "Irtaza"}
# modify(person)
# print(person)   # {"name": "Irtaza", "new": 99} — modified! 😱

# # protect with copy
# modify(person.copy())
# print(person)   # {"name": "Irtaza"} — safe ✅

# Simple Rule:
# Mutable   (list, dict, set)  → passed by reference → original changes
# Immutable (int, str, tuple)  → passed by value     → original safe


























































































