# DAY 3 — PYTHON PRACTICE
# ════════════════════════

# EASY — [Dictionaries + Functions + String Methods]
# Write a function called contact_book() that manages a simple contact
# list. It takes two arguments: an action ("add", "remove", "search")
# and a contact dict with "name" and "phone". 
# - "add" → adds contact, no duplicates by name (case insensitive)
# - "remove" → removes by name (case insensitive)
# - "search" → returns the contact dict if found, else "Not Found"
# - Always return the current total count of contacts after add/remove

# Example:
# contact_book("add", {"name": "Ali", "phone": "0300-1234567"})
# → "Added. Total contacts: 1"

# contact_book("add", {"name": "ali", "phone": "0311-9999999"})
# → "Already exists. Total contacts: 1"

# contact_book("search", {"name": "Ali", "phone": ""})
# → {"name": "Ali", "phone": "0300-1234567"}

# contact_book("remove", {"name": "ALI", "phone": ""})
# → "Removed. Total contacts: 0"
contacts=[]
def contact_book(action,contact):
    match action.lower():
        case "add":
            for c in contacts:
                if contact["name"].casefold()==c["name"].casefold():
                    print(f"Already exists. Total contacts: {len(contacts)}")
                    return
            contact["name"]=contact["name"].lower()
            contacts.append(contact)
            print(f"Added. Total contacts: {len(contacts)}")
        case "remove":
            for c in contacts:
                if contact["name"].casefold()==c["name"].casefold():
                    contact["name"]=contact["name"].lower()
                    contact["phone"]=c.get("phone")
                    print(f"Removed. Total contacts: {len(contacts)-1}")
                    contacts.remove(contact)
                    break
            
        case "search":
            for c in contacts:
                if contact["name"].casefold()==c["name"].casefold():
                    print(c)
                    return
        case _:
            print("invalid action")
            
contact_book("add", {"name": "Ali", "phone": "0300-1234567"})
contact_book("add", {"name": "ali", "phone": "0311-9999999"})
contact_book("search", {"name": "Ali", "phone": ""})
contact_book("remove", {"name": "ALI", "phone": ""})


# MEDIUM — [Generators + Functions + map() + filter() + Dictionaries]
# Write a function called pipeline() that takes a list of numbers and
# processes them through these steps in order:
# 1. Filter out numbers not divisible by 3
# 2. Square each remaining number
# 3. Use a generator to yield only values greater than 100
# 4. Return a dict with:
#    - "results": list of final values
#    - "count": how many values made it through
#    - "sum": total sum of final values

# Example:
# pipeline([3, 6, 9, 12, 15, 18, 2, 7, 21])
# → {
#     "results": [144, 225, 324, 441],
#     "count": 4,
#     "sum": 1134
#   }
# # 3→9 (not >100, dropped), 6→36 (dropped), 9→81 (dropped)
# # 12→144 ✓, 15→225 ✓, 18→324 ✓, 21→441 ✓
def gen(numbers):
    for n in numbers:
        if n>100:
            yield n

def pipeline(numbers):
    numbers=list(gen((map(lambda x :x**2,filter(lambda x :x%3==0,numbers)))))
    return {
    "results": numbers,
    "count": len(numbers),
    "sum": sum(numbers)
    }
print(pipeline([3, 6, 9, 12, 15, 18, 2, 7, 21]))


# HARD — [Classes concepts using Functions + Decorators + Generators + 
#         Collections + datetime + Recursion]

# Build a mini Library Management System using only functions
# (no classes — use dicts and lists to represent data):

# 1. A decorator @require_admin that takes a role argument —
#    only allows the function to run if role == "admin",
#    otherwise prints "Access Denied" and blocks

# 2. A function add_book() decorated with @require_admin that
#    takes (role, title, author, copies=1) and adds to the library

# 3. A recursive function search_books() that takes a keyword and
#    a list of books, returns all books where keyword appears in
#    title or author (case insensitive)

# 4. A generator called available_books() that yields only books
#    with copies > 0, one at a time

# 5. A function borrow_book() that takes a title, reduces copies
#    by 1 (minimum 0), and logs the borrow with datetime

# 6. A function library_report() that prints:
#    - Total unique titles
#    - Most borrowed book (use Counter on borrow log)
#    - List of unavailable books (copies == 0)
#    - All available books using available_books() generator

# Example:
# add_book("admin", "Clean Code", "Robert Martin", 3)
# add_book("admin", "Python Crash Course", "Eric Matthes", 2)
# add_book("user", "Hacking", "Some Author")  # blocked

# borrow_book("Clean Code")
# borrow_book("Clean Code")

# library_report()
# →
# ════════════════════════════
#       LIBRARY REPORT
# ════════════════════════════
# Total Titles  : 2
# Most Borrowed : Clean Code (2 times)
# Unavailable   : None
# Available Books:
#   - Clean Code (1 copy)
#   - Python Crash Course (2 copies)
# ════════════════════════════