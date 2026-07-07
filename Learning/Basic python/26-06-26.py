import random

# # 1
# print("Welcome to rolling dice game")
# PLAYER1=PLAYER2=0
# for i in range(1,4):
#     print("-"*20)
#     print(f"ROUND {i}")
#     print("-"*20)
#     for j in range(1,3):
#         print(f"Player {j},press any character to roll =:>",end="")
#         input()
#         while (a:=random.randint(1,6)) == (b:=random.randint(1,6)):
#             print(a," ",b)
#             print("double roll again=:> ",end="")
#             input()
#         print(a," ",b)
#         match j:
#             case 1:PLAYER1+=a+b
#             case 2:PLAYER2+=a+b
#     print("-"*20)

# print(f"Player 1 =:> {PLAYER1}")
# print(f"Player 1 =:> {PLAYER2}")
# print("Equal" if PLAYER1==PLAYER2 else ("Player 1" if PLAYER1>PLAYER2 else "Player 2" +" win"))


# # 2
value=["A","J","Q","K","2","3","4","5","6","7","8","9","10"]
suits=["♠","♦","♣","♥"]
cards=[]
for i in suits:
    for j in value:
        cards.append(j+i)    
print(cards)

PLAYER1=random.choices(cards,k=5)

PLAYER2=random.choices(cards,k=5)
while PLAYER2 in PLAYER1:
    PLAYER2=random.choices(cards,k=5)
print(f"Player 1 : {PLAYER1}")
print(f"Player 2 : {PLAYER2}")


# 3
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers   = "0123456789"
symbols   = "!@#$%^&*"
length=int(input("Enter Length:"))
uc,n,s=input("Include upper Case :"),input("Include numbers :"),input("Include symbol :")
password=""
while True:
    i=random.choice(lowercase+uppercase+numbers+symbols)
    if len(password)==length:
        break
    if i in uppercase and uc!="y":
        continue
    elif i in numbers and n!="y":
        continue
    elif i in symbols and s!="y":
        continue
    else:
        password+=i

print(f"Generated Password :{password}")    





























