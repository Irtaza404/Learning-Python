# import json

# data = {
#     "name"    : "Irtaza",
#     "age"     : 25,
#     "hobbies" : ["coding", "gaming"],
#     "active"  : True,
#     "score"   : None
# }

# # Step 1 — convert to JSON string
# json_string = json.dumps(data)
# print(json_string)

# # Step 2 — convert back to Python
# back_to_python = json.loads(json_string)
# print(back_to_python)
# print(type(back_to_python))

# # Step 3 — access like normal dict
# print(back_to_python["name"])
# print(back_to_python["hobbies"][0])


from datetime import date

today = date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.weekday())

birthday = date(1999, 5, 15)
print(birthday)

print(True+True-False)








