# DAY 4 — PYTHON PRACTICE
# ════════════════════════

# EASY (1) — [List Comprehension + Conditionals]
# In one line, create a list of all numbers from 1 to 50 that are 
# divisible by both 3 and 5.

# Expected output: [15, 30, 45]
numbers=[i for i in range(1,50) if i%3==0 and i%5==0]
print(numbers)

# EASY (2) — [String Methods + List Comprehension]
# Given a list of words, return a new list with only the words that:
# - Are longer than 4 characters
# - Start with a vowel
# - Converted to uppercase

words = ["apple", "cat", "orange", "ant", "umbrella", "dog", "ink"]
# Expected output: ["APPLE", "ORANGE", "UMBRELLA"]
words=[w.upper() for w in words if len(w)>4 and w.upper().startswith(("A","E","I","O","U"))]
print(words)

# MEDIUM (1) — [Walrus Operator + Loops + Functions]
# Write a function called first_long_word() that takes a sentence and
# returns the first word longer than 5 characters using the walrus
# operator inside a loop. Return "None found" if no such word exists.

# Example:
# first_long_word("the cat sat on a beautiful mat")  → "beautiful"
# first_long_word("the cat sat on a mat")            → "None found"
def first_long_word(sen):
    for word in sen.split():
        if (n := len(word)) > 5: 
            return word
    return "None Found"
    

# MEDIUM (2) — [Dictionary + map() + filter() + Lambda]
# Given a list of products as tuples (name, price, in_stock):
# - Filter out products not in stock
# - Apply 10% discount to all remaining prices
# - Return a dict of {name: discounted_price}

products = [("Keyboard", 2000, True), ("Mouse", 1500, False),
            ("Monitor", 15000, True), ("USB Hub", 800, False),
            ("Headphones", 3000, True)]

# Expected output:
# {"Keyboard": 1800.0, "Monitor": 13500.0, "Headphones": 2700.0}
print(dict(map(lambda x: (x[0],(x[1]-(x[1]*0.1))),filter(lambda x: x[2],products))))


# MEDIUM (3) — [Unpacking + zip() + Functions]
# Write a function called pair_students() that takes two lists —
# students and scores — zips them together, unpacks each pair,
# and returns a dict of {student: grade} where:
# A=90+, B=80+, C=70+, D=60+, F=below 60

# Example:
# pair_students(["Ali","Sara","Zain","Hina"], [92, 74, 55, 83])
# → {"Ali": "A", "Sara": "C", "Zain": "F", "Hina": "B"}
def pair_students(students,scores):
    temp={}
    for student,score in zip(students,scores):
        grade="A" if score >=90 else "B" if score>=80 else "C" if score>=70 else "D" if score>=60 else "F"
        temp[student]=grade
    return temp
print(pair_students(["Ali","Sara","Zain","Hina"], [92, 74, 55, 83]))
