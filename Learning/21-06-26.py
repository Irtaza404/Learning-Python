# # def ar(*key):
# #     total=0
# #     for a in key:
# #         total+=a
# #     return total

# # print(ar(1,2,3,4,5))

# # Task function
# # 1
# # def calculator(a,b,op):
# #     if op=='+':
# #         return a+b
# #     elif op=='-':
# #         return a-b
# #     elif op=='*' or op.lower() =='x' :
# #         return a*b
# #     elif op=='/':
# #         return a/b
# #     else:
# #         return "invalid operator"

# # print(calculator(int(input("a=")),int(input("b=")),input("op=")))

# # # 2
# # def allrounder(numbers):
# #     total=0
# #     min=max=numbers[0]
# #     for num in numbers:
# #         total+=num
# #         if min>num:
# #             min=num
# #         if max<num:
# #             max=num
# #     return total,total/len(numbers),max,min

# # sum,avg,max,min=allrounder([int(num) for num in input().split()])
# # print(f'sum = {sum} ,average = {avg} ,max = {max} ,min ={ min}')

# # 3
# # def is_palindrome(word):
# #     if word==word[::-1]:
# #         return True
# #     return False
# # words = ["racecar","hello","level","world","madam","python"]
# # only=[word for word in words if is_palindrome(word)]
# # print(only)

# # 4
# def fibonacci(n):
#     if n<=0:
#         return 0
#     elif n==1:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
# n_terms = 10
# for i in range(n_terms):
#     print(fibonacci(i), end=" ")

# # 5
# def build_profile(**details):


#  learning
# gues=["rock","paper","siecesser",None]
# player=None
# while player not in gues:
#     player=input("hghg")
name="fnjafh dfgg fsfs"
# print(name.replace("f","x"))
# print(name.title())
# x="you"
# def c():
#     global x
#     x="me"
#     print(x)

# c()

# print(x)

# # Problem
# path = "C:\new\text\files"  # \n and \t get interpreted!
# print(path)
# # C:
# # ew	ext\files   ← WRONG

# # Solution — raw string with r prefix
# path = r"C:\new\text\files"
# print(path)                 # C:\new\text\files ✅

# x=2.9+0.1
# y=3
# print(id(x))
# print(1.1 + 0.1== 1.2)
# a=10000
# b=10000
# print(a is b)

# while True:
#     a,b=float(input("A=")),float(input("B="))
#     match input("Operator :").lower():
#         case "add":
#             print(a+b)
#         case "sub":
#             print(a-b)
#         case "mul":
#             print(a*b)
#         case "div":
#             print(a/b)
#         case "quit":
#             break
#         case _:
#             print("Unkown")
        
# task match
# 1
# match int(input("month number :")):
#     case 1: print("Jan")
#     case 2: print("feb")
#     case 3: print("mar")
#     case 4: print("apr")
#     case 5: print("may")
#     case 6: print("jun")
#     case 7: print("jul")
#     case 8: print("aug")
#     case 9: print("sep")        
#     case 10: print("oct")
#     case 11: print("nov")
#     case 12: print("dec") 
#     case _: print("invalid")

# 2
# match input(" string :"): 
#     case "True"|"False": print("Boolean")
#     case _: print("invalid")

# # 3
# match got:=tuple(input().split()):
#     case ("monday", "morning"):print(f"good {got[0]}{got[1]}!")
#     case ("friday", "evening"):print(f" TGIF {got[1]}!")
#     case (*r, "morning"):print(f" Good {got[-1]}!")
#     case (*r, "evening"):print(f" good {got[-1]}!")

# 4
# match input().upper():
#     case "GET"    : print("Fetching data")
#     case "POST"   : print("Creating data")
#     case "PUT"    : print("Updating data")
#     case "DELETE" : print("Deleting data")    

# # 5
# match input().split():
#     case []:print("empty")
#     case [x]:print(f"One item: {x}")
#     case [x,y]:print(f"two item: {x} {y}")
#     case [x,y,z]:print(f"three item: {x} {y} {z}")
#     case [*d]:print("more then 3")
    
# # 6
# while output:=input()!="quit":
#     match input():
#         case "red": print("Stop")
#         case "yellow":print("get ready")
#         case "green":print("go")

# 8
# import math
# dit={"shape": "circle", "radius": 5}
# match dit.get("shape"):
#     case "circle":print(math.pi*dit.get("radius")**2)
#     case "rectangle":print(dit.get("width")*dit.get("height"))
#     case "square":   print(dit.get("side")**2) 
    

# #9
# match tuple(input().split()):
#     case ("admin",  "admin123") : print( "Admin login")
#     case ("irtaza", "python123"): print( "User login")
#     case ("guest",  "guest")    : print( "Guest login")
#     case _                       :print( "Access denied")


# 10
rooms = {
    "hall"   : {"north": "kitchen", "east": "bedroom", "south": None, "west": None},
    "kitchen": {"north": None, "east": "dining", "south": "hall", "west": None},
    "bedroom": {"north": "bathroom", "east": None, "south": None, "west": "hall"},
    "dining" : {"north": None, "east": None, "south": None, "west": "kitchen"},
    "bathroom":{"north": None, "east": None, "south": "bedroom", "west": None},
}

descriptions = {
    "hall"    : "You are in the hall. Doors to the north and east.",
    "kitchen" : "You are in the kitchen. Something smells good!",
    "bedroom" : "You are in the bedroom. A bed and a wardrobe.",
    "dining"  : "You are in the dining room. A big table here.",
    "bathroom": "You are in the bathroom. Clean and bright.",
}

current_room = "hall"

while (movement:=input())!="quit":
    match movement:
        case "north"|"south"|"east"|"west" if rooms.get(current_room).get(movement) is not None :current_room=rooms.get(current_room).get(movement) 
        case "look":print(descriptions.get(current_room))

















