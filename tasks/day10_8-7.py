

# # Here are 10 easy practice tasks covering topics 1–32:

# # 1.(Variables/strings) Create a variable name and age, then print: "My name is X and I am Y years old" using an f-string.
# name="Irtaza"
# age=200
# print(f"My name is {name} and I am {age} years old")

# # 2.(Operators) Write a program that checks if a number is even or odd using the % operator.

# if int(input("num"))%2==0:
#     print("even")
# else:
#     print("odd")

# # 3.(match/case) Write a match/case that takes a day number (1–7) and prints the day name.
# match int(input("day:")):
#     case 1:print("Monday")
#     case 2:print("Tuesday")
#     case 3:print("Wednesday")
#     case 4:print("Thursday")
#     case 5:print("Friday")
#     case 6:print("Saturday")
#     case 7:print("Sunday")
#     case _:print("invalid")

# # 4.(Loops) Print all numbers from 1 to 20 that are divisible by 3, using a for loop and range().
# for num in range(1,21):
#     if num%3==0:
#         print(num,end=" ")

# # 5.(Lists) Given nums = [5, 2, 9, 1, 7], use a list comprehension to create a new list with only numbers greater than 3.
# nums = [5, 2, 9, 1, 7]
# greater3=[i for i in nums if i>3]
# print(greater3)


# # 6.(Dictionaries) Create a dictionary of 3 students with their marks, then print each name and mark using a loop.
# student={
#     "Ali":20,
#     "Irtaza":20,
#     "Moiz":50
# }
# for name,score in student.items():
#     print(f"name={name} score ={score}")

# # 7.(Functions) Write a function greet(name, greeting="Hello") that returns f"{greeting}, {name}!" — test it with and without the second argument.
# def greet(name,greeting="Hello"):
#     return f"{greeting} {name}! "
# print(greet("Irtaza","HI"))
# print(greet("ALi"))


# # 8.**(*args/kwargs) Write a function total(*nums) that returns the sum of any number of arguments passed in.
# def total(*num):
#     return sum(num)

# # 9.(Lambda + map/filter) Given nums = [1,2,3,4,5,6], use filter() + lambda to get only even numbers, then use map() + lambda to square them.
# nums = [1,2,3,4,5,6]
# nums=list(map(lambda sq:sq**2,filter(lambda x: x%2==0,nums)))
# print(nums)

# # 10.(Generators) Write a generator function countdown(n) that yields numbers from n down to 1.
# def countdown(n):
#     if n<0:
#         n*=-1
#     for c in range(n,0,-1):
#         yield c



# medium
#1 (Nested lists/comprehension) Given matrix = [[1,2,3],[4,5,6],[7,8,9]], use a nested list comprehension to flatten it into [1,2,3,4,5,6,7,8,9].
matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix=[j for i in matrix for j in i]
print(matrix)

# (Sets) Given a = [1,2,2,3,4,4,5] and b = [3,4,5,6,7], find elements common to both lists using sets (no loops).
a = set([1,2,2,3,4,4,5])
b = set([3,4,5,6,7])
print(list(a & b))

# **(*args/kwargs) Write a function describe(**info) that takes any keyword arguments and prints them like key: value on separate lines.
def describe(**info):
    for (key,value) in info.items():
        print(f"{key}:{value}")

describe(ali="pass",score=20)
# (Positional/keyword-only) Write a function divide(a, b, /, *, round_to=2) — a and b must be positional-only, round_to must be keyword-only. Return a/b rounded to round_to decimals.

def divide(a, b, /, *, round_to=2):
    if b==0:
        return "can't divide by zero "
    else :
        return round(a/b,round_to)
print(divide(5,0,round_to=3))

# (Recursion) Write a recursive function factorial(n) (no loops allowed).
def factorial(n):
    if n<=1:
        return 1
    return n * factorial(n-1)

# print(factorial(int(input("num:"))))

# (Closures) Write a function make_multiplier(x) that returns a function which multiplies any number by x. Test: double = make_multiplier(2) then double(5) → 10.
def make_multiplier(x):
    def fun(y):
        return x*y
    return fun
double=make_multiplier(5)
print(double(10))

# (Decorators) Write a decorator @timer that prints how long a function takes to run (use time).
import time
def timer(fun):
    def wrapper():
        start=time.time()
        fun()
        end=time.time()
        print(f"{end-start} seconds")
    return wrapper
@timer
def add():
    print(20+1)

add()


# (Higher order functions) Write a function apply_twice(func, value) that applies func to value two times. Test with apply_twice(lambda x: x*2, 3) → should give 12.
def apply_twice(func,value):
    for _ in range(2):
        value=func(value)
    print(value)
apply_twice(lambda x: x*2, 3)


# (Generators) Write a generator fibonacci(n) that yields the first n Fibonacci numbers (0, 1, 1, 2, 3, 5...).
def fibonacci(n):
    i=0
    a,b=0,1
    while i<n:
        yield a
        a,b=b,a+b
        i+=1

print(list(fibonacci(5)))

# (Error handling + custom exception) Create a custom exception NegativeNumberError. Write a function square_root(n) that raises this exception if n is negative, otherwise returns n ** 0.5. Wrap a call in try/except and print a friendly message on error.

class NegativeNumberError(Exception):
    pass

def square_root(n):
    if n<0:
        raise NegativeNumberError("Negitive number")
    return n**0.5

try:
    value=square_root(-1)
except NegativeNumberError as e:
    print(e)














