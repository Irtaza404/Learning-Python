# import time

# def timer(func):
#     def wrapper():
#         start = time.time()
#         func()
#         print(f"{func.__name__} took {time.time()-start:.2f} seconds")
#     return wrapper

# @timer
# def slow():
#     time.sleep(1)
#     print("Done!")

# slow()
# # Done!
# # slow took 1.00 seconds

# def repeat(n):
#     def decorator(func):
#         def wrapper():
#             for _ in range(n):
#                 func()
#         return wrapper
#     return decorator

# @repeat(3)
# def greet():
#     print("Hello!")

# greet()     # Hello! x3 ✅
# greet()     # Hello! x3 ✅ — works every time!


# def sum(num):
#     if num==1:
#         return 1
#     return num +  sum(num-1)

# print(sum(5))

# def reverse(word):
#     if word=="":
#         return ""
#     return reverse(word[1:])+word[0]
# print(reverse("hello"))

# def is_palindrome(word):
#     return word==reverse(word)

# print(is_palindrome("racecar"))
# print(is_palindrome("hello"))

# # 1
# students = [("Irtaza", 95), ("Ali", 80), ("Sara", 99)]
# students.sort(key= lambda s:s[1])
# print(students)
# # 2
# names = ["Irtaza", "Ali", "Sara", "Muhammad"]
# names.sort(reverse=True,key= lambda n:len(n))
# print(names)
# # 3
# people = [
#     {"name": "Irtaza", "age": 25},
#     {"name": "Ali",    "age": 30},
#     {"name": "Sara",   "age": 20}
# ]
# people.sort(key= lambda p:p.get("age"))
# print(people)


# # 1
# numbers = ["1", "2", "3", "4", "5"]
# numbers=list(map(int,numbers))
# print(type(numbers[0]))
# # 2
# celsius = [0, 20, 37, 100]
# # formula: (c * 9/5) + 32
# fahrenheit=list(map(lambda c: (c*9/5)+32,celsius))
# print(fahrenheit)
# # 3
# names = ["irtaza khan", "ali ahmed", "sara malik"]
# names=list(map(str.title,names))
# print(names)

# # 1
# numbers = [-5, -3, 0, 2, 4, -1, 8, -2]
# numbers=list(filter(lambda x: x>0,numbers))
# print(numbers)

# # 2
# words = ["hi", "hello", "python", "ok", "world", "cat"]
# words=list(filter(lambda x : len(x)>4,words))
# print(words)

# # 3
# people = [
#     {"name": "Irtaza", "age": 25},
#     {"name": "Ali",    "age": 15},
#     {"name": "Sara",   "age": 20},
#     {"name": "Ahmed",  "age": 12}
# ]
# people=list(filter(lambda x: x.get("age")>=18,people))
# print(people)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # Expected: [4, 16, 36, 64, 100]
# numbers=list(map(lambda x:x**2,filter(lambda x:x%2==0,numbers)))
# print(numbers)

# 1
def fibonnacci(n):
    a,b,c=0,1,0
    while c<n:
        yield a
        a,b=b,a+b
        c+=1
for n in fibonnacci(10):
    print(n)

# 2
def div3(num):
    for n in num:    
        if n%3==0:
            yield n

numbers = [1,2,3,4,5,6,7,8,9,10,11,12]

for n in div3(numbers):
    print(n)


def get_numbers(start,end):
    for i in range(start,end):
        yield i

def square(numbers):
    for n in numbers:
        yield n ** 2

def only_odd(numbers):
    for n in numbers:
        if n % 2 != 0:
            yield n
            
for n in square(only_odd(get_numbers(1,20))):
    print(n,end=" ")






import mytools

print(mytools.greet("Irtaza"))  # Hello Irtaza!
print(mytools.add(5, 3))        # 8
print(mytools.PI)               # 3.14159









