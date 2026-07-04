# # way to print outputs


# #1— Most Common
# print("------")


# # 2. sys.stdout.write() — Lower level print
# import sys
# sys.stdout.write("Hello\n")  # \n means new line
# # Difference: it doesn't add a new line automatically like print() does.


# # 3. logging — For professional/debug output
# import logging
# logging.warning("Something went wrong!")
# logging.info("Program started")
# # Used in real projects to track what's happening in a program.


# # 4. Exceptions / Errors — Output to error console
# # raise ValueError("This is an error message")
# # This prints to the error stream, not the normal output.


# #how string can be used 


# # 1 — Creating Strings
# s1 = "Hello"          # double quotes
# s2 = 'World'          # single quotes — both are the same
# s3 = """I am
# a multi-line
# string"""             # triple quotes — spans multiple lines

# print(s1)
# print(s2)
# print(s3)

# # 2 — String Concatenation (Joining)
# first = "Irtaza"
# last = "Khan"

# full = first + " " + last
# print(full)   # Irtaza Khan


# # 3 — String Repetition
# print("Ha" * 3)    # HaHaHa
# print("-" * 20)    # --------------------



# # task
# #1
# name=input("enter full name :")
# print(len(name))
# print(name.upper)
# print(name[::-1])

# #2
# sentence=input("enter full sentence : ")
# print(sentence.count('a'))
# print(sentence.replace(' ',''))
# print(sentence[:5])

# # 3
# name=input("name:")
# age=int(input("age:"))
# country=input("country:")
# print(f"Hi! I'm {name},{age} years old,from {country}")













