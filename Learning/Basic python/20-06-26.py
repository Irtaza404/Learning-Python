# task Dictionary
# # 1
# data={}
# for i in range(5): 
#     country,capital=input().split()
#     data[country]=capital

# print("Country".center(20,"-"))
# for country in data.keys():
#     print(country)
# print("".center(20,"-"))
# print("Capitals".center(20,"-"))
# for Capitals in data.values():
#     print(Capitals)
# print("".center(20,"-"))

# key=input("Enter country :")
# print(data.get(key,"Not found"))

# # 2
# sentence=input()
# frequencey={}
# for word in sentence.split():
#     frequencey[word]=frequencey.get(word,0)+1
# don't know how to print most to least

# 3
# students = {
#     "Irtaza" : [85, 90, 78, 92, 88],
#     "Ali"    : [70, 65, 80, 75, 85],
#     "Sara"   : [95, 98, 92, 96, 99]
# }

# for student,number in students.items():
#     print(student.center(20,"-"))
#     total=0
#     for num in number:
#         total+=num
#     average=total/len(number)
#     print(f"Average = {average}")
#     print(f"Higest = {max(number)} , lowest = {min(number)} ")
#     print("pass" if average>=75 else "Fail")

# 4
contact={}
while True:
    print("Menu".center(20,"-"))
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Show all Contact")
    print("0. Quit")
    choice=int(input("=:>"))
    if choice==0:
        print("Thanks for use this Program, have a great day")
        print("Exiting....")
        break
    elif choice==1:
        name=input("Ënter name :")
        if contact.get(name) is None:
            contact[name]=input("Enter Contact :")
            print("Added")
        else:
            print(f"{name} already exist")
    elif choice==2:
        print(f"contact = {contact.get(input("name = "),"Not exist")}")
    elif choice==3:
        name=input("Ënter name :")
        if contact.get(name) is not None:
            if input("are you sure to detele it?Press d to delete=4").lower()=="d":
               contact.pop(name)
               print("Deleted")
        else:
            print(f"{name} not exist")
    elif choice==4:
        print("".center(30,"-"))

        for name,number in contact.items():
            print(f"{name} =:> {number}")
        print("".center(30,"-"))
    else:
        print("Invalid Choice")














