# # task  if-elif-else
# # 1
# age=int(input("age:"))
# if age<=0:
#     pass
# elif age < 13:
#     print("child")
# elif age<=17:
#     print("teenager")
# elif age<=64:
#     print("Adult")
# else:
#     print("Senior")

# # 2
# num=int(input("Number:"))
# if num==0:
#     print("zero")
# elif num<0:
#     print("negitive")
# else:
#     print("positive")

# print("even" if num%2==0 else "odd")


# # 3
# username="Irtaza"
# password="python123"
# un=input()
# pas=input()
# if un.casefold()==username.casefold() and pas==password:
#     print("correct login")
# elif pas!=password:
#     print("wrong password")
# else:
#     print("wrong username")


# task loop
# 1
for i in range(10,0,-1):
    print(i)
print("Blast off! 🚀")


# 2
num=input()
sum=0
while num!="done":
    sum+=int(num)
    num=input()

print(sum)

# 3
for i in range(0,6):
    for j in range(0,i):
        print("*",end="")
    print()


# 4
import random

ran=random.randint(1,100)
num=int(input("num ="))
tries=1
while num !=ran:
    print("too high" if num > ran else "too low")
    num=int(input("num ="))
    tries+=1
print(f"You got it in {tries} tries!")
