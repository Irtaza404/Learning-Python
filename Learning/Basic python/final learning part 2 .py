# Functions — Parameters

# Basic:
# def greet(name, age):    # name, age are parameters
#     return f"{name} is {age}"

# greet("Irtaza", 20)      # "Irtaza", 20 are arguments

# Default parameters:
# def greet(name, age=20):  # age has default
#     return f"{name} is {age}"

# greet("Irtaza")           # → "Irtaza is 20"
# greet("Irtaza", 25)       # → "Irtaza is 25"
# ⚠️ Default parameters must come after non-defaults.

# Keyword arguments:
# greet(age=25, name="Irtaza")  # order doesn't matter

# Positional only /:
# def greet(name, age, /):  # must be passed positionally
#     return f"{name} is {age}"

# greet("Irtaza", 20)        # ✅
# greet(name="Irtaza", age=20)  # ❌ ERROR

# Keyword only *:
# def greet(*, name, age):  # must be passed as keyword
#     return f"{name} is {age}"

# greet(name="Irtaza", age=20)  # ✅
# greet("Irtaza", 20)            # ❌ ERROR


# *args & **kwargs

# *args — variable positional arguments:
# def total(*args):
#     return sum(args)

# total(1, 2, 3, 4)  # → 10
# args is just a tuple inside the function:
# def show(*args):
#     print(args)       # → (1, 2, 3)
#     print(type(args)) # → tuple

# **kwargs — variable keyword arguments:
# def show(**kwargs):
#     print(kwargs)

# show(name="Irtaza", age=20)
# # → {"name": "Irtaza", "age": 20}
# kwargs is just a dict inside the function.

# Both together:
# def show(*args, **kwargs):
#     print(args)    # tuple
#     print(kwargs)  # dict

# show(1, 2, 3, name="Irtaza", age=20)
# # → (1, 2, 3)
# # → {"name": "Irtaza", "age": 20}

# Order must be:
# def func(normal, *args, **kwargs):
# #         ↑        ↑        ↑
# #       first   second    last

# Unpacking with * and **:
# nums = [1, 2, 3]
# print(*nums)        # → 1 2 3

# data = {"name": "Irtaza", "age": 20}
# greet(**data)       # same as greet(name="Irtaza", age=20)



# Positional only / — must pass by position:
# def func(a, b, /):
#     pass

# func(1, 2)        # ✅
# func(a=1, b=2)    # ❌
# Keyword only * — must pass by keyword:
# def func(*, a, b):
#     pass

# func(a=1, b=2)    # ✅
# func(1, 2)        # ❌
# Both together:
# def func(a, b, /, c, *, d, e):
#     pass
# #   positional  normal  keyword
# #   only                only


# Scope
# Python uses LEGB rule to find variables:

# L — Local (inside current function)
# E — Enclosing (outer function if nested)
# G — Global (module level)
# B — Built-in (Python's built-ins like len, print)

# Example:
# x = "global"

# def outer():
#     x = "enclosing"
    
#     def inner():
#         x = "local"
#         print(x)    # → "local"
    
#     inner()
#     print(x)        # → "enclosing"

# outer()
# print(x)            # → "global"

# global keyword — modify global variable inside function:
# x = 10

# def change():
#     global x
#     x = 20

# change()
# print(x)  # → 20

# nonlocal keyword — modify enclosing variable:
# def outer():
#     x = 10
#     def inner():
#         nonlocal x
#         x = 20
#     inner()
#     print(x)  # → 20

# Without keywords — read only:
# x = 10
# def func():
#     print(x)   # ✅ can read
#     x = 20     # ❌ ERROR — can't modify without global

# so do we only have nonlocal and globe keywords

# Yes, only two:

# global → access/modify global variable
# nonlocal → access/modify enclosing function variable
# For local variables no keyword needed — they're automatically local.


# def func():
#     x = 10      # automatically local, no keyword needed

# Recursion
# A function that calls itself until a base case stops it.

# Two parts every recursive function needs:

# Base case — when to stop
# Recursive case — call itself with smaller problem


# Example — factorial:
# def    if n == 0:      # base case
#         return 1
#     return n * factorial(n - 1)  # recursive case

# factorial(4)
# # → 4 * factorial(3)
# # → 4 * 3 * factorial(2)
# # → 4 * 3 * 2 * factorial(1)
# # → 4 * 3 * 2 * 1 * factorial(0)
# # → 4 * 3 * 2 * 1 * 1
# # → 24

# What happens in memory:
# factorial(4)  ←
#   factorial(3)  ←
#     factorial(2)  ←
#       factorial(1)  ←
#         factorial(0) → 1
# Each call waits for the one below it to return.

# Without base case → infinite recursion:
# def func(n):
#     return func(n-1)  # never stops → RecursionError

# Python's recursion limit:
# import sys
# sys.getrecursionlimit()  # → 1000 by default
# sys.setrecursionlimit(100)

# When to use recursion:

# Tree/nested structures
# Divide and conquer problems
# When problem naturally breaks into smaller same problems


# Decorators
# A function that wraps another function to add behavior without changing its code.

# Basic structure:
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         # before
#         result = func(*args, **kwargs)
#         # after
#         return result
#     return wrapper

# @decorator
# def my_func():
#     pass
# @decorator is just shorthand for:
# my_func = decorator(my_func)

# Simple example:
# def log(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling {func.__name__}")
#         result = func(*args, **kwargs)
#         print(f"Done")
#         return result
#     return wrapper

# @log
# def add(a, b):
#     return a + b

# add(2, 3)
# # → Calling add
# # → Done
# # → 5

# Decorator with arguments — extra layer:
# def repeat(n):          # outer — takes decorator args
#     def decorator(func):  # middle — takes function
#         def wrapper(*args, **kwargs):  # inner — takes call args
#             for _ in range(n):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorator

# @repeat(3)
# def greet():
#     print("Hello")

# greet()  # prints Hello 3 times

# Useful built-in decorators:
# @staticmethod   # method that doesn't need self
# @classmethod    # method that receives class not instance
# @property       # treat method as attribute

# Why decorators exist
# Imagine you have 3 functions and you want to print "calling..." before each one:
# Without decorator — repetitive:
# def add(a, b):
#     print("calling add")
#     return a + b

# def multiply(a, b):
#     print("calling multiply")
#     return a * b
# With decorator — write once, apply anywhere:
# def log(func):
#     def wrapper(*args, **kwargs):
#         print(f"calling {func.__name__}")
#         return func(*args, **kwargs)
#     return wrapper

# @log
# def add(a, b):
#     return a + b

# @log
# def multiply(a, b):
#     return a * b

# What actually happens step by step
# @log
# def add(a, b):
#     return a + b
# Python reads this as:
# add = log(add)
# So let's trace log(add):
# def log(func):          # func = add
#     def wrapper(*args, **kwargs):
#         print(f"calling {func.__name__}")
#         return func(*args, **kwargs)
#     return wrapper      # returns wrapper function
# Now add is no longer the original function — it's wrapper.
# When you call add(2, 3):
# python# actually calls wrapper(2, 3)
# # args = (2, 3)
# # prints "calling add"
# # then calls original add(2, 3)
# # returns 5

# Visual mental model
# Before decorator:
# add(2, 3) → [add function] → 5

# After decorator:
# add(2, 3) → [wrapper] → [add function] → 5
#               ↑
#          extra behavior here

# Why *args, **kwargs in wrapper?
# So the wrapper works with any function regardless of parameters:
# python@log
# def add(a, b): ...          # 2 args
# @log
# def greet(name): ...        # 1 arg
# @log
# def show(a, b, c=1): ...    # mixed
# Same wrapper handles all of them because *args catches any positional and **kwargs catches any keyword arguments.

# Decorator with arguments — the confusing part
# @repeat(3)
# def greet():
#     print("Hello")
# This is actually:
# greet = repeat(3)(greet)
# So repeat(3) must return a decorator:
# pythondef repeat(n):              # step 1 — called with 3
#     def decorator(func):    # step 2 — called with greet
#         def wrapper():      # step 3 — called when greet() is called
#             for _ in range(n):
#                 func()
#         return wrapper
#     return decorator
# Trace:
# repeat(3)         → returns decorator
# decorator(greet)  → returns wrapper
# greet()           → calls wrapper() → calls greet 3 times

# Summary
# PartPurposeouter functionreceives the function to wrapwrapperreplaces the original function*args **kwargsmakes wrapper work with any functionreturn func(...)actually calls the original functionextra layeronly needed when decorator takes arguments


# repeat(3) — Step by Step
# Think of it as 3 nested functions, each with one job:
# repeat(3)      # job: remember n=3, return a decorator
# decorator(func) # job: receive the function, return wrapper  
# wrapper()       # job: actually run when greet() is called

# Trace every step:
# @repeat(3)
# def greet():
#     print("Hello")
# Step 1 — Python calls repeat(3):
# def repeat(n):      # n = 3
#     ...
#     return decorator  # returns decorator function
# Step 2 — Python calls decorator(greet):
# def decorator(func):  # func = greet
#     ...
#     return wrapper    # returns wrapper function
# Step 3 — greet is now wrapper. When you call greet():
# def wrapper():
#     for _ in range(3):  # n=3 remembered from step 1
#         func()          # calls original greet

# Why 3 layers?
# @repeat(3)  ← needs one layer just to receive "3"
#             ← then normal decorator layers
# Without argument → 2 layers
# With argument → 3 layers — that's the only difference.

# Multiple Decorators
# Just stack them:
# @decorator1
# @decorator2
# def func():
#     pass
# Order is bottom to top — decorator2 wraps first, then decorator1 wraps that:
# func = decorator1(decorator2(func))
# Example:
# def bold(func):
#     def wrapper():
#         return f"<b>{func()}</b>"
#     return wrapper

# def italic(func):
#     def wrapper():
#         return f"<i>{func()}</i>"
#     return wrapper

# @bold
# @italic
# def greet():
#     return "Hello"

# greet()  # → "<b><i>Hello</i></b>"
# Trace:
# italic wraps greet first  → <i>Hello</i>
# bold wraps that result    → <b><i>Hello</i></b>



# Closures
# A closure is a function that remembers variables from its enclosing scope even after the outer function has finished.

# Simple example:
# def outer(x):
#     def inner(y):
#         return x + y  # remembers x
#     return inner

# add5 = outer(5)   # outer finishes, but x=5 is remembered
# add5(3)           # → 8
# add5(10)          # → 13

# What's happening in memory:
# outer(5) finishes →  normally x would be deleted
#                   →  but inner still needs x
#                   →  so Python keeps x=5 alive
# This "keeping alive" is the closure.

# How to check if a function is a closure:
# add5.__closure__          # → closure object
# add5.__closure__[0].cell_contents  # → 5

# Real world use — counter:
# def make_counter():
#     count = 0
#     def counter():
#         nonlocal count
#         count += 1
#         return count
#     return counter

# c = make_counter()
# c()  # → 1
# c()  # → 2
# c()  # → 3

# c2 = make_counter()  # separate counter
# c2() # → 1  (independent from c)

# Difference from decorator:
# ClosureDecoratorRemembers variablesWraps a functionReturns inner functionReturns wrapper functionGeneral purposeSpecific purpose
# Every decorator uses closure — but not every closure is a decorator.

# Higher Order Functions
# A function that either:

# Takes a function as argument
# Returns a function


# You already know these — just a concept name:
# # takes function as argument
# map(lambda x: x*2, [1,2,3])
# filter(lambda x: x>2, [1,2,3])
# sorted([3,1,2], key=lambda x: x)

# # returns a function
# def make_adder(n):
#     return lambda x: x + n

# add5 = make_adder(5)
# add5(3)  # → 8

# Decorators are higher order functions:
# def log(func):      # takes function
#     def wrapper():
#         func()
#     return wrapper  # returns function

# Why useful:
# # instead of writing separate functions:
# def double(x): return x * 2
# def triple(x): return x * 3

# # write one higher order function:
# def multiplier(n):
#     return lambda x: x * n

# double = multiplier(2)
# triple = multiplier(3)


# Lambda
# A one line anonymous function — no name, no def.

# Syntax:
# lambda arguments: expression

# Normal function vs lambda:
# # normal
# def add(a, b):
#     return a + b

# # lambda
# add = lambda a, b: a + b

# add(2, 3)  # → 5

# Most common use — inside other functions:
# # sorted
# students = [("Ali", 92), ("Sara", 85), ("Zain", 78)]
# sorted(students, key=lambda x: x[1])
# # → [("Zain", 78), ("Sara", 85), ("Ali", 92)]

# # map
# list(map(lambda x: x**2, [1,2,3,4]))
# # → [1, 4, 9, 16]

# # filter
# list(filter(lambda x: x%2==0, [1,2,3,4,5,6]))
# # → [2, 4, 6]

# Limitations:

# Only one expression — no multiple lines
# No statements like if/else blocks, loops
# Ternary operator is fine though:

# lambda x: "even" if x%2==0 else "odd"

# When to use:

# Short throwaway functions
# Inside map(), filter(), sorted()
# When function is used only once

# When NOT to use:

# Complex logic → use def instead
# When you need to reuse it → give it a name with def


# map() & filter()

# map() — apply function to every item:
# numbers = [1, 2, 3, 4, 5]

# result = map(lambda x: x**2, numbers)
# list(result)  # → [1, 4, 9, 16, 25]
# Think: "do this to every item"

# filter() — keep items where function returns True:
# numbers = [1, 2, 3, 4, 5, 6]

# result = filter(lambda x: x%2==0, numbers)
# list(result)  # → [2, 4, 6]
# Think: "keep only items that pass this condition"

# Both return iterators — wrap in list() to see results:
# map(...)     # → iterator object
# filter(...)  # → iterator object

# list(map(...))     # → actual list
# list(filter(...))  # → actual list

# Chaining together:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# result = list(map(lambda x: x**2,
#             filter(lambda x: x%2==0, numbers)))
# # → [4, 16, 36, 64, 100]
# # filter evens first → then square each

# map() with multiple iterables:
# a = [1, 2, 3]
# b = [4, 5, 6]

# list(map(lambda x, y: x+y, a, b))
# # → [5, 7, 9]

# List comprehension vs map/filter:
# # these are equivalent
# list(map(lambda x: x**2, numbers))
# [x**2 for x in numbers]

# # filter equivalent
# list(filter(lambda x: x>3, numbers))
# [x for x in numbers if x>3]
# Comprehensions are more Pythonic — use map/filter when chaining or passing as arguments.

# Generators & yield

# Problem with normal functions:
# pythondef get_numbers(n):
#     return [i for i in range(n)]  # creates entire list in memory
# If n = 10 million → 10 million items in memory at once.

# Generator — produces one item at a time:
# pythondef get_numbers(n):
#     for i in range(n):
#         yield i  # pauses here, returns i, resumes next call
# Only one item in memory at a time.

# How yield works:
# pythondef gen():
#     print("step 1")
#     yield 1
#     print("step 2")
#     yield 2
#     print("step 3")
#     yield 3

# g = gen()
# next(g)  # prints "step 1" → returns 1
# next(g)  # prints "step 2" → returns 2
# next(g)  # prints "step 3" → returns 3
# next(g)  # → StopIteration error
# Function pauses at each yield and resumes from same point.

# 3 ways to consume:
# pythong = get_numbers(5)

# # 1. next()
# next(g)  # one at a time

# # 2. for loop
# for n in get_numbers(5):
#     print(n)

# # 3. list()
# list(get_numbers(5))  # converts all to list

# Generator expression — one liner:
# python# normal generator function
# def squares(n):
#     for i in range(n):
#         yield i**2

# # generator expression
# squares = (i**2 for i in range(5))  # note: () not []

# Key difference — list vs generator:
# python[i**2 for i in range(5)]   # list → all in memory
# (i**2 for i in range(5))   # generator → one at a time

# 3 — Passing data into a generator
# Two ways:
# Way 1 — pass as parameter (most common):
# pythondef gen(numbers):       # pass list in
#     for n in numbers:
#         yield n * 2

# g = gen([1, 2, 3, 4])
# list(g)  # → [2, 4, 6, 8]
# Way 2 — pass via send() (rare):
# pythondef gen():
#     while True:
#         x = yield          # receives sent value
#         print(f"got {x}")

# g = gen()
# next(g)        # start the generator
# g.send(10)     # → "got 10"
# g.send(20)     # → "got 20"
# send() is rarely used — just know it exists.

# 4 — Chaining generators
# Each generator feeds into the next like a pipeline:
# pythondef get_numbers(n):
#     for i in range(n):
#         yield i

# def square(numbers):
#     for n in numbers:
#         yield n ** 2

# def filter_even(numbers):
#     for n in numbers:
#         if n % 2 == 0:
#             yield n
# Chain them:
# pythonnumbers = get_numbers(10)    # 0,1,2,3,4,5,6,7,8,9
# squared = square(numbers)    # 0,1,4,9,16,25,36,49,64,81
# evens = filter_even(squared) # 0,4,16,36,64

# list(evens)  # → [0, 4, 16, 36, 64]
# Key thing — nothing runs until you consume the final generator. It's lazy — each item flows through the whole pipeline one at a time:
# 0 → square → 0  → filter → 0  ✓
# 1 → square → 1  → filter → ✗
# 2 → square → 4  → filter → 4  ✓
# 3 → square → 9  → filter → ✗

# zip() & enumerate()

# zip() — pair up two or more iterables:
# pythonnames = ["Ali", "Sara", "Zain"]
# scores = [92, 85, 78]

# list(zip(names, scores))
# # → [("Ali", 92), ("Sara", 85), ("Zain", 78)]
# Unpack directly in loop:
# pythonfor name, score in zip(names, scores):
#     print(f"{name} scored {score}")
# Stops at shortest list:
# pythona = [1, 2, 3, 4, 5]
# b = [10, 20, 30]

# list(zip(a, b))  # → [(1,10), (2,20), (3,30)]
# # 4 and 5 are ignored
# Unzip:
# pythonpairs = [("Ali", 92), ("Sara", 85)]
# names, scores = zip(*pairs)
# # names  → ("Ali", "Sara")
# # scores → (92, 85)

# enumerate() — get index and value together:
# pythonnames = ["Ali", "Sara", "Zain"]

# for i, name in enumerate(names):
#     print(i, name)
# # → 0 Ali
# # → 1 Sara
# # → 2 Zain
# Start from any number:
# pythonfor i, name in enumerate(names, start=1):
#     print(i, name)
# # → 1 Ali
# # → 2 Sara
# # → 3 Zain

# Both together:
# pythonfor i, (name, score) in enumerate(zip(names, scores), start=1):
#     print(f"#{i} {name} → {score}")
# # → #1 Ali → 92
# # → #2 Sara → 85
# # → #3 Zain → 78

# 28. try/except/else/finally
# pythontry:
#     x = 10 / 2
# except ZeroDivisionError:
#     print("error")
# else:
#     print("no error, runs if try succeeded")  # → runs
# finally:
#     print("always runs")

# except: runs on error
# else: runs only if no error
# finally: always runs (cleanup)

# Clear? Or move to 29 (raise/custom exceptions)?not like this show all  important things in that topicStrategized comprehensive coverage of remaining topics thoroughlyStrategized comprehensive coverage of remaining topics thoroughly28. try/except/else/finally
# pythontry:
#     risky()
# except ValueError as e:          # catch specific type
#     print(e)
# except (TypeError, KeyError):    # catch multiple types
#     pass
# except Exception as e:           # catch-all (broad, avoid overusing)
#     print(e)
# else:
#     print("runs only if no exception")
# finally:
#     print("always runs (cleanup, closing files)")
# Key points:

# Multiple except blocks checked top to bottom — put specific ones first.
# else runs only if try succeeded (no error).
# finally always runs, even if there's a return in try/except.
# Can catch multiple exceptions in one line: except (TypeError, ValueError):
# Bare except: catches everything (even KeyboardInterrupt) — bad practice.


# 29. raise and custom exceptions
# python# raise built-in
# if age < 0:
#     raise ValueError("age can't be negative")

# # re-raise inside except
# try:
#     do_something()
# except Exception as e:
#     raise  # re-raises same exception

# # custom exception
# class InsufficientFundsError(Exception):
#     def __init__(self, balance):
#         self.balance = balance
#         super().__init__(f"Balance too low: {balance}")

# raise InsufficientFundsError(50)

# # exception chaining
# raise RuntimeError("failed") from original_error
# Key points:

# Custom exceptions inherit from Exception (or a more specific built-in).
# raise alone (inside except) re-raises the caught exception.
# raise X from Y shows chained cause in traceback.


# 30. Common exceptions
# ExceptionWhenValueErrorright type, wrong value (int("abc"))TypeErrorwrong type (1 + "a")KeyErrormissing dict keyIndexErrorlist index out of rangeAttributeErrorattribute/method doesn't existZeroDivisionErrordivide by zeroFileNotFoundErrormissing fileStopIterationnext() on exhausted iteratorImportError/ModuleNotFoundErrorbad importNameErrorundefined variable



# Yes. finally always executes, even if try or except has a return, break, or continue.
# pythondef test():
#     try:
#         return "from try"
#     finally:
#         print("finally runs")  # prints BEFORE returning

# test()
# # → finally runs
# # → returns "from try"
# Even trickier — if finally also has a return, it overrides the try's return:
# pythondef test():
#     try:
#         return "from try"
#     finally:
#         return "from finally"   # this wins!

# test()  # → "from finally"
# Same with loops:
# pythonfor i in range(3):
#     try:
#         if i == 1:
#             break
#     finally:
#         print(f"cleanup {i}")   # runs even on break
# Only thing that skips finally: if the program crashes hard (e.g. os._exit()) or the process is killed.

# Thought for 8s
# Thought for 8s
# 28. try/except/else/finally

# python
# try:
#     x = 10 / 2
# except ZeroDivisionError:
#     print("error")
# else:
#     print("no error, runs if try succeeded")  # → runs
# finally:
#     print("always runs")
# except: runs on error
# else: runs only if no error
# finally: always runs (cleanup)
# Clear? Or move to 29 (raise/custom exceptions)?

# not like this show all  important things in that topic


# Strategized comprehensive coverage of remaining topics thoroughly
# Strategized comprehensive coverage of remaining topics thoroughly
# 28. try/except/else/finally

# python
# try:
#     risky()
# except ValueError as e:          # catch specific type
#     print(e)
# except (TypeError, KeyError):    # catch multiple types
#     pass
# except Exception as e:           # catch-all (broad, avoid overusing)
#     print(e)
# else:
#     print("runs only if no exception")
# finally:
#     print("always runs (cleanup, closing files)")
# Key points:

# Multiple except blocks checked top to bottom — put specific ones first.
# else runs only if try succeeded (no error).
# finally always runs, even if there's a return in try/except.
# Can catch multiple exceptions in one line: except (TypeError, ValueError):
# Bare except: catches everything (even KeyboardInterrupt) — bad practice.
# 29. raise and custom exceptions

# python
# # raise built-in
# if age < 0:
#     raise ValueError("age can't be negative")

# # re-raise inside except
# try:
#     do_something()
# except Exception as e:
#     raise  # re-raises same exception

# # custom exception
# class InsufficientFundsError(Exception):
#     def __init__(self, balance):
#         self.balance = balance
#         super().__init__(f"Balance too low: {balance}")

# raise InsufficientFundsError(50)

# # exception chaining
# raise RuntimeError("failed") from original_error
# Key points:

# Custom exceptions inherit from Exception (or a more specific built-in).
# raise alone (inside except) re-raises the caught exception.
# raise X from Y shows chained cause in traceback.
# 30. Common exceptions

# Exception	When
# ValueError	right type, wrong value (int("abc"))
# TypeError	wrong type (1 + "a")
# KeyError	missing dict key
# IndexError	list index out of range
# AttributeError	attribute/method doesn't exist
# ZeroDivisionError	divide by zero
# FileNotFoundError	missing file
# StopIteration	next() on exhausted iterator
# ImportError/ModuleNotFoundError	bad import
# NameError	undefined variable
# Want me to continue with 31. random?

# you said finally always run even when there a return or break right


# Clarified finally block behavior with return and break statements
# Clarified finally block behavior with return and break statements
# Yes. finally always executes, even if try or except has a return, break, or continue.

# python
# def test():
#     try:
#         return "from try"
#     finally:
#         print("finally runs")  # prints BEFORE returning

# test()
# # → finally runs
# # → returns "from try"
# Even trickier — if finally also has a return, it overrides the try's return:

# python
# def test():
#     try:
#         return "from try"
#     finally:
#         return "from finally"   # this wins!

# test()  # → "from finally"
# Same with loops:

# python
# for i in range(3):
#     try:
#         if i == 1:
#             break
#     finally:
#         print(f"cleanup {i}")   # runs even on break
# Only thing that skips finally: if the program crashes hard (e.g. os._exit()) or the process is killed.

# Clear? Continue to 31. random?

# time for dinner i will be back in half an hours

# Sounds good — enjoy your dinner! I'll be here when you're back. We'll pick up at 31. random.

# lets start


# Pivoted toward introducing random module concepts
# Pivoted toward introducing random module concepts
# 31. random

# python
# import random

# random.random()          # float between 0.0 and 1.0
# random.randint(1, 10)    # int, inclusive both ends → 1 to 10
# random.uniform(1, 10)    # float between 1 and 10

# random.choice([1,2,3])         # pick one item
# random.choices([1,2,3], k=2)   # pick with replacement (can repeat)
# random.sample([1,2,3,4], 2)    # pick without replacement (no repeats)

# nums = [1,2,3,4]
# random.shuffle(nums)     # shuffles in place, returns None

# random.seed(42)          # makes randomness reproducible
# Key points:

# randint(a, b) is inclusive on both ends.
# choices() can repeat items; sample() cannot.
# shuffle() modifies the list in-place — doesn't return a new list.
# seed() is important for testing/debugging — same seed → same "random" results.

# More on random
# pythonimport random

# # Weighted choices
# random.choices(["a", "b", "c"], weights=[1, 1, 10], k=5)
# # "c" is 10x more likely to be picked than "a" or "b"

# # Random float in a range with step-like control
# random.randrange(0, 100, 5)   # like range(): 0,5,10...95 → picks one

# # Getting a random item from a dict (via keys)
# d = {"x": 1, "y": 2}
# random.choice(list(d.keys()))

# # Cryptographically secure random (for passwords, tokens)
# import secrets
# secrets.token_hex(16)     # secure random hex string
# secrets.choice([1,2,3])   # secure random choice
# Key extra points:

# random module is not secure for passwords/tokens/crypto — it's predictable if seed is known. Use secrets module instead for security-sensitive stuff.
# randrange(start, stop, step) works just like range() but returns one random value from that sequence.
# choices() lets you bias probability with weights=.
# Every random.X() call under the hood uses the same global state — that's why seed() affects all subsequent calls, not just the next one.

# pythonrandom.seed(1)
# print(random.randint(1,10))  # always same value
# print(random.randint(1,10))  # always same next value (deterministic sequence)
# Common use cases:

# shuffle() → shuffling a deck of cards, quiz questions
# sample() → picking unique winners from a raffle
# choice() → random enemy spawn, dice roll simulation
# seed() → unit testing code that uses randomness

# 32. math
# pythonimport math

# math.sqrt(16)        # 4.0
# math.pow(2, 3)        # 8.0 (returns float, unlike 2**3)
# math.floor(4.7)       # 4
# math.ceil(4.2)        # 5
# math.trunc(4.7)       # 4 (chops decimal, no rounding)

# math.pi               # 3.14159...
# math.e                # 2.71828...

# math.log(8, 2)        # log base 2 of 8 → 3.0
# math.log10(100)       # 2.0
# math.log(math.e)      # 1.0 (natural log, base e)

# math.factorial(5)     # 120

# math.gcd(12, 18)       # 6
# math.isqrt(17)         # 4 (integer square root, floors result)

# math.inf               # infinity
# math.nan               # not a number
# math.isnan(math.nan)   # True

# math.degrees(math.pi)  # 180.0
# math.radians(180)      # 3.14159...
# math.sin(math.radians(90))  # 1.0
# Key points:

# math.sqrt() only works on non-negative numbers — raises error on negatives (use cmath for complex).
# math.pow() always returns float; ** can return int if inputs are ints.
# // (floor division) differs from math.floor() — floor division works on any two numbers, math.floor() rounds one number down.
# math.isqrt() is exact integer math (no float rounding errors) — better than int(math.sqrt(x)) for large numbers.

# import math

# # Rounding / precision
# math.floor(4.7)       # 4
# math.ceil(4.2)        # 5
# math.trunc(4.9)       # 4
# round(4.567, 2)        # 4.57 (built-in, not math module)

# # Powers & roots
# math.sqrt(16)          # 4.0
# math.isqrt(17)         # 4 (integer sqrt)
# math.pow(2, 3)         # 8.0
# math.exp(1)             # e^1 → 2.718...
# math.cbrt(27)           # 3.0 (cube root, Python 3.11+)

# # Logs
# math.log(8, 2)          # log base 2
# math.log2(8)             # 3.0
# math.log10(1000)         # 3.0
# math.log1p(0)             # log(1+x), useful for small x precision

# # Trig
# math.sin(x), math.cos(x), math.tan(x)
# math.asin(x), math.acos(x), math.atan(x)
# math.atan2(y, x)          # angle from origin to point (y,x)
# math.degrees(rad)          # rad → deg
# math.radians(deg)          # deg → rad
# math.hypot(3, 4)            # 5.0 (Pythagorean distance)

# # Number theory
# math.gcd(12, 18)              # greatest common divisor
# math.lcm(4, 6)                 # least common multiple (3.9+)
# math.factorial(5)               # 120
# math.comb(5, 2)                  # combinations (5 choose 2) → 10
# math.perm(5, 2)                   # permutations → 20

# # Special values
# math.inf, -math.inf, math.nan
# math.isnan(x), math.isinf(x), math.isfinite(x)

# # Constants
# math.pi, math.e, math.tau  # tau = 2*pi
# Key points:

# math.comb/math.perm are super handy for probability/combinatorics problems.
# math.hypot() is a clean way to get distance between two points.
# math.isclose(a, b) is the correct way to compare floats (avoids 0.1+0.2 == 0.3 issues).

# No worries, let's slow down. Think of time module as having just 3 jobs:
# 1. "What time is it right now?"
# pythonimport time
# now = time.time()
# print(now)   # 1751980800.0  (just a big number = seconds since Jan 1, 1970)
# This number by itself is useless to read — it's mainly for math, not display.
# 2. "How long did my code take?"
# This is the #1 real use of time.
# pythonstart = time.time()

# # do something
# for i in range(1000000):
#     pass

# end = time.time()
# print(end - start)   # → "it took 0.05 seconds"
# That's it. Start clock → do stuff → stop clock → subtract.
# (For serious benchmarking, swap time.time() for time.perf_counter() — same idea, just more accurate.)
# 3. "Pause for a bit"
# pythonprint("Loading...")
# time.sleep(3)   # program freezes here for 3 seconds
# print("Done!")
# Useful for delays, retry loops, simulations.

# That's genuinely 90% of what you'll ever use time for:
# Want to...UseMeasure how long code takestime.time() or time.perf_counter() before/afterPause the programtime.sleep(seconds)Show a readable date/clockActually use datetime instead (next topic!)
# The confusing "struct_time / ctime" stuff is rarely used — I only showed it for completeness. You can basically forget it.


# 34. datetime
# Think of it as 3 jobs too:
# 1. "What's today's date / right now?"
# pythonfrom datetime import datetime, date

# datetime.now()     # → 2026-07-08 14:32:10.123456 (date + time)
# date.today()        # → 2026-07-08 (just date)
# 2. "Build a specific date"
# pythonfrom datetime import datetime

# d = datetime(2025, 12, 25)          # Dec 25, 2025
# d = datetime(2025, 12, 25, 9, 30)   # + 9:30 AM
# 3. "Do math with dates" (this is where it gets useful)
# pythonfrom datetime import datetime, timedelta

# today = datetime.now()
# tomorrow = today + timedelta(days=1)
# next_week = today + timedelta(weeks=1)
# past = today - timedelta(hours=5)

# # difference between two dates
# d1 = datetime(2026, 1, 1)
# d2 = datetime(2026, 7, 8)
# diff = d2 - d1
# print(diff.days)    # → 188 (number of days between)
# 4. Formatting (making it readable / parsing text into dates)
# pythonnow = datetime.now()
# now.strftime("%Y-%m-%d")        # → "2026-07-08"   (date → string)
# now.strftime("%d/%m/%Y %H:%M")  # → "08/07/2026 14:32"

# datetime.strptime("2026-07-08", "%Y-%m-%d")  # string → date object
# Common format codes:
# CodeMeaning%Yyear (2026)%mmonth (07)%dday (08)%Hhour (24h)%Mminute%Ssecond

# Quick memory trick: strftime = "string FROM time", strptime = "string PARSED to time".


















