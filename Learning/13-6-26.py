# task string,condition & loops
# # 1 
# checker=input("Enter string:")
# vov="AEIOUaeiou"
# total=0
# for i in checker:
#     if i in vov:
#         total+=1
# print(total)

# 2
# word=input()
# if word == word[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# 3
# sentence=input()
# for i in sentence.split():
#     if i.startswith("a") or i.startswith("A"):
#         print(i)

# 4
# word=input()
# checker=True
# nword=""
# for i in word:
#     if checker:
#         nword+=i.upper()
#         checker=False
#     else:
#         nword+=i.lower()
#         checker=True
# print(nword)

# # 5
# sentence=input()
# print(len(sentence.split()))

# 6
# data=input()
# ndata=""
# for i in data:
#     if i not in ndata:
#         ndata+=i
# print(ndata)

# 7
# data=input()
# for i in range(0,len(data)+1):
#     for j in range(0,i):
#         print(data[j],end="")
#     print()

# 8
# data=input()
# ndata=""
# for i in data.split():
#     ndata+= i[::-1]+" "
# print(ndata)

# 9
# sentence=input()
# alpalower='abcdefghijklmnopqrstuvwxyz'
# checker=True
# for i in alpalower:
#     if sentence.count(i)>=1 or sentence.count(i.upper())>=1:
#         pass
#     else: 
#         checker=False
#         break
# print ( "panagram" if checker else "Not a panagram")

# # 10
# message=input("Message=")
# shift=int(input("Shift="))
# encrpyt=""
# for i in message:
#     base= ord("A") if i.isupper() else ord("a")
#     encrpyt+= chr(((ord(i) - base+shift)%26+base))
# print(encrpyt)

# print(0.1+0.2==0.3+0.000004)
# i=1.1
# print(ord("c"))
# c='c'
# print(c.capitalize())
# t=True
# print(t)

