# tuple & set 
# 1
# cites=tuple(input().split())
# a,b,c,d,e=cites
# print(f"{a} {b} {c} {d} {e}")

# # 2
# number= [int(i) for i in input().split()]
# unique=set(number)
# print(len(unique))
# if len(unique)==len(number):
#     print("no duplicate")
# else:
#     print("duplicates are :")
#     for n in unique:
#         if number.count(n)>1:
#             print(n,end=" ")

# 3
python_students = {"Irtaza", "Ali", "Sara", "Khan", "Zara"}
java_students   = {"Ali", "Khan", "Ahmed", "Bilal", "Zara"}
print(python_students & java_students)
print(python_students - java_students)
print(python_students ^ java_students)
print((python_students | java_students)-(python_students & java_students))



# 4
words = ["apple","banana","apple","mango","banana","apple","kiwi"]
unique=set(words)

if len(unique)==len(words):
    print("each word appears only one times")
else:
    print("word count :")
    for i in unique:
        counter=len([w for w in words if w == i])
        print(f"{i} = {counter}")







