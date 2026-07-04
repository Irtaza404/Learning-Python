# DAY 2 — PYTHON PRACTICE
# ════════════════════════

# EASY — [Strings + Functions + Loops]
# Write a function called word_frequency() that takes a sentence string
# and returns a dictionary of each word and how many times it appears.
# - Ignore case (treat "The" and "the" as same)
# - Ignore punctuation (. , ! ? only)
# - Sort the result by frequency (highest first)

# Example:
# word_frequency("the cat sat on the mat. The cat!")
# → {"the": 3, "cat": 2, "sat": 1, "on": 1, "mat": 1}
from collections import Counter
def word_frequency(sentence):
    return dict(Counter(sentence.translate("".maketrans("", "", ".!?")).lower().split()))
print(word_frequency("the cat sat on the mat. The cat!"))
# MEDIUM — [Generators + Recursion + Functions]
# Write a recursive function called flatten() that takes a deeply nested
# list and returns a flat list. Then wrap it in a generator called
# flat_gen() that yields one item at a time, skipping any item that
# is negative.

# Then write a function called running_total() that uses flat_gen() and
# yields the running sum as each item is consumed.

# Example:
# data = [1, [2, [-3, 4]], [5, [-6, [7, 8]]]]

# list(running_total(data))
# → [1, 3, 7, 12, 19, 27]
# # -3 and -6 skipped, running sum: 1, 1+2, 1+2+4, ...
# def flatten(numbers):
#     result = []
#     for item in numbers:
#         if isinstance(item, list):
#             result += flatten(item)  # recurse and add returned list
#         else:
#             result.append(item)      # plain number, collect it
#     return result
# def flat_gen(numbers):
#     numbers=flatten(numbers)
#     for number in numbers:
#         if number>0:
#             yield number
# def running_total(data):
#     total = 0
#     for item in flat_gen(data):  # pull from flat_gen
#         total += item
#         yield total
# gen=running_total([1, [2, [-3, 4]], [5, [-6, [7, 8]]]])
# print(next(gen))


# HARD — [Dictionaries + Functions + Decorators + datetime + Collections]
# Build a mini Expense Tracker with the following:

# 1. A decorator @validate that checks if the amount is a positive number
#    before allowing the function to run — if not, print "Invalid amount"
#    and block the call

# 2. A function add_expense() decorated with @validate that takes:
#    (category, amount, note="") and stores it in a list of dicts with
#    a datetime timestamp

# 3. A function summary() that returns:
#    - Total spent
#    - Spending by category (use Counter or dict)
#    - Most expensive single expense
#    - Expenses grouped by date (just the date, not time)

# 4. A function monthly_report() that prints a clean formatted report
    
# Example:
# add_expense("Food", 500, "Lunch")
# add_expense("Transport", 200)
# add_expense("Food", 300, "Dinner")
# add_expense("Food", -100)        # blocked by validator

# monthly_report()
# →
# ════════════════════════════
#       EXPENSE REPORT
# ════════════════════════════
# Total Spent   : Rs. 1000
# Most Expensive: Rs. 500 (Food - Lunch)

# By Category:
#   Food        : Rs. 800
#   Transport   : Rs. 200

# By Date:
#   2024-01-15  : 3 expense(s)
# ════════════════════════════


# data=[]

# def validate(add_expense):
#     def runner(*args,**kwargs):
#         if args[1]>0:
#             add_expense(*args,**kwargs)
#         else:
#             print("Invalid amount")
#     return runner

# from datetime import datetime

# @validate
# def add_expense(category, amount, note=""):
#     data.append({"category":category,"amount":amount,"note":note,"date_time":datetime.now()})

# def summary():
#     total=0
#     for single in data:
#         total+=single.get("amount")
#     mostExp=max(data, key=lambda x: x["amount"])
#     Category={}
#     date={}
#     for c in data:
#         if c.get("category") in Category:
#             Category[c.get("category")]+=c.get("amount")
#         else:
#             Category[c.get("category")]=c.get("amount")
#         date[str((c.get("date_time").date()))] = date.get(str((c.get("date_time").date())), 0) + 1
    
#     return total,mostExp,Category,date

# def monthly_report():
#     total,mostExp,Category,date=summary()
#     print("════════════════════════════")
#     print("EXPENSE REPORT".center(30))
#     print("════════════════════════════")
#     print(f"Total Spent   : Rs. {total}")
#     print(f"Most Expensive: Rs. {mostExp.get("amount")} ({mostExp.get("category")} - {mostExp.get("note")})")
#     print("By Category:")
#     for category,amount in Category.items():
#         print(F"{category} : Rs. {amount}")
#     print("By Date:")
#     for sdate,exp in date.items():
#         print(F"{sdate} : {exp} expense(s)")
#     print("════════════════════════════")

# add_expense("Food", 500, "Lunch")
# add_expense("Transport", 200)
# add_expense("Food", 300, "Dinner")
# add_expense("Food", -100)        # blocked by validator

# monthly_report()