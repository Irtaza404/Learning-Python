# def hello():
#     print("you")
    
# def hello():
#     pass
    
# print(hello())

# def introduce(name,age,job,city="London"):
#         print(f"Hi ! I\'m {name}, {age} years old , from {city}, working as a {job}")
# introduce(job="AI Eng",name="Irtaza",age=25,)

# def my_function(name, /):
#   print("Hello", name)

# my_function(name = "Emil")



# def calculate_bmi(weight,height):
#     bmi=weight/height**2
#     return "underweight" if bmi < 18.5 else "Normal" if bmi<25 else "overweight" if bmi <30 else "obese"


# def create_profile(name, age, city="Unknown", role="user", active=True):
#     return {
#         "name"  : name,
#         "age"   : age,
#         "city"  : city,
#         "role"  : role,
#         "active": active
#     }

# print(create_profile("Irtaza", 25))
# print(create_profile("Irtaza", 25, "London"))
# print(create_profile("Irtaza", 25, "London", active=False, role="admin"))

# age=16
# if age>=18 or "":
#     print("allowed")
# else:
#     print("not Allowed")

# x=int("5")
# y=int("5.0")
# # print(x+y)
# print(int())


# f,*_,last=(1,2,3,4,5)
# print(f," ",last)
# print(type(_))



# def calculate(op,*num):
#     result=None
#     match op:
#         case "add":
#             result=0
#             for n in num:
#                 result+=n
#         case "mul":
#             result=1
#             for n in num:
#                 result*=n
#         case "min":
#             result=num[0]
#             for n in num:
#                 if result>n: 
#                     result=n           
#         case "max":
#             result=num[0]
#             for n in num:
#                 if result<n: 
#                     result=n           
#     return result
# print(calculate("add", 1, 2, 3, 4))   # 10
# print(calculate("mul", 2, 3, 4))   # 24
# print(calculate("max", 5, 1, 8, 3))   # 8
# print(calculate("min", 5, 1, 8, 3))   # 1

# def build_sentence(template,**kwargs):
#     print(template.format(**kwargs))
    
# build_sentence(
#     "My name is {name}, I am {age} and I live in {city}",
#     name="Irtaza",
#     age=25,
#     city="London"
# )
# # My name is Irtaza, I am 25 and I live in London

# def add(a,b,c,*_):
#     return _

# number1=[1,2,3,4,5]
# number2=(6,7,8,9,10)
# number=[*number1,*number2]
# print(add(*number))

y="global"
def outer():
    x="outer"
    y=""
    def inner():
        nonlocal y
        y="inner"
        print(y)
        
    inner()
    print(x)
    print(y)

outer()
    



