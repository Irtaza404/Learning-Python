# f=open("test.txt","w")
# f.write("Hello baby\n my baby")
# f.close()


# f = open("test.txt", "r")
# content = f.read()
# print(content)
# f.close()

# f = open("test.txt", "r")
# line = f.readline()   # reads just ONE line
# print(line)
# f.close()

# f = open("test.txt", "r")
# line = f.readlines()   # reads just ONE line
# print(line)
# f.close()

# with open("test.txt", "r") as f:
#     content = f.read()
# print(content)

# with open("test.txt", "r") as f:
#     content = f.read()
# print(content)

# with open("test.txt", "a") as f:
#     f.write("\nAnother line")

with open("test.txt", "r") as f:
    for line in f:
        print(line)


with open("test.txt", "r") as f:
    for line in f:
        print(line.strip())

lines = ["apple", "banana", "cherry"]

# Option A: writelines() — takes a list, but does NOT add \n for you
with open("fruits.txt", "w") as f:
    f.writelines(lines)

with open("fruits.txt", "r") as f:
    for line in f:
        print(line)


import os

if os.path.exists("test.txt"):
    with open("test.txt", "r") as f:
        print(f.read())
else:
    print("File doesn't exist")


try:
    with open("missing.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File doesn't exist")


import os
os.mkdir("data")          # creates ONE folder — fails if parent path doesn't exist
os.makedirs("data/sub")   # creates the folder AND any missing parent folders
