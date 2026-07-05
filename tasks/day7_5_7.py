# DAY 7 — PYTHON PRACTICE
# ════════════════════════

# EASY (1) — [Functions + Error Handling + String Methods]
# Write a function called safe_input() that takes a prompt string
# and an expected type ("int", "float", "str"). It keeps asking
# the user for input until they enter a valid value of that type,
# then returns it.


def safe_input(prompt,datatype):
    while True:
        try:
            value=input(prompt)
            if datatype=="int":
                value=int(value)
            elif datatype=="float":
                value=float(value)
            return value
        except ValueError:
            print(f"Invalid! Please enter a valid {datatype}")

# # Example:
# safe_input("Enter your age: ", "int")
# → Enter your age: abc
# → Invalid! Please enter a valid int
# → Enter your age: 25
# → returns 25


# EASY (2) — [random + Functions + List Comprehension]
# Write a function called lottery() that:
# - Generates 6 unique random numbers between 1 and 49
# - Sorts them in ascending order
# - Returns them as a formatted string

import random
def lottery():
    number=sorted(random.sample(range(1,50),6))
    return f"Your lucky numbers: {" - ".join(f"{n:02d}" for n in number)}"
    
# Example:
print(lottery())
# → "Your lucky numbers: 03 - 11 - 22 - 35 - 41 - 47"
# (each number padded to 2 digits)


# MEDIUM (1) — [Closures + Functions + Error Handling]
# Write a closure called make_validator() that takes a min_val
# and max_val and returns an inner function that:
# - Validates if a number is within range
# - Raises ValueError if out of range
# - Raises TypeError if input is not a number
# - Returns the number if valid
def make_validator(min_val,max_val):
    def inner(number):
        try:
            if not isinstance(number, (int, float)):
                raise TypeError(f"Expected a number, got{type(number).__name__}")
            if number<min_val or number>max_val:
                raise ValueError(f"{number} is out of range ({min_val}-{max_val})")   
            return number
        except (TypeError,ValueError) as e:
            print(e)
    return inner
# Example:
# validate_age = make_validator(0, 120)
# validate_age(25) #   → 25
# validate_age(150)  # → ValueError: "150 is out of range (0-120)"
# validate_age("abc")# → TypeError: "Expected a number, got str"


# MEDIUM (2) — [Generators + map() + filter() + Error Handling]
# Write a generator called safe_parse() that takes a list of mixed
# values, tries to convert each to float, yields the value if
# successful, and skips with a warning print if not.

# Then write a function called stats() that uses safe_parse() to
# compute min, max, and average of all successfully parsed values.

def safe_prase(data):
    for val in data:
        try:
            val=float(val)
            yield val
        except (ValueError,TypeError):
            print(f"Skipping invalid value: {val}")

def stats(data):
    values=list(safe_prase(data))
    return {"min":min(values),"max":max(values),"avg":sum(values)/len(values)}

# Example:
data = [1, "2.5", "abc", 4, "5.5", None, "7"]
stats(data)
# → Skipping invalid value: abc
# → Skipping invalid value: None
# → {"min": 1.0, "max": 7.0, "average": 4.0}