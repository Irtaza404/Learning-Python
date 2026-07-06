# DAY 8 — PYTHON PRACTICE
# ════════════════════════

# EASY (1) — [collections + Functions + Loops]
# Write a function called text_analyzer() that takes a string and
# returns a dict with:
# - "words": total word count
# - "unique": number of unique words (case insensitive)
# - "most_common": top 3 most common words using Counter
# - "longest": the longest word in the text
from collections import Counter
def text_analyzer(text):
    words=len(text.split())
    unique= len(set(text.lower().split()))
    most=Counter(text.split()).most_common(3)
    longest=max(text.split(),key=len)
    return { 
            "words":words,
            "unique":unique ,
            "most":most,  
            "longest":longest
            }
    


# Example:
print(text_analyzer("the quick brown fox jumps over the lazy dog the fox"))
# → {
#     "words": 10,
#     "unique": 8,
#     "most_common": [("the", 3), ("fox", 2), ("quick", 1)],
#     "longest": "jumps"
#   }


# EASY (2) — [datetime + Functions + String Formatting]
# Write a function called time_greeting() that returns a different
# greeting based on the current hour and prints a formatted
# current datetime.

# - 5am–11am  → "Good Morning"
# - 12pm–4pm  → "Good Afternoon"  
# - 5pm–8pm   → "Good Evening"
# - 9pm–4am   → "Good Night"
from datetime import datetime,timedelta
def time_greeting():
    current=datetime.now()
    greeting=""
    match current.hour:
        case 5|6|7|8|9|10|11: greeting="Good Morning"
        case 12|13|14|15|16 : greeting="Good Afternoon" 
        case 17|18|19|20: greeting="Good Evening"
        case _: greeting="Good Night"
    return f"{greeting}, Irtaza!\ntoday is {current.strftime("%A, %B %d, %Y")}\ncurrent time {current.strftime("%I:%M %p")}"
    


# Example:
# print(time_greeting())
# → "Good Morning, Irtaza!
#    Today is Monday, July 08, 2024
#    Current time is 10:30 AM"


# MEDIUM (1) — [Generators + collections + Functions]
# Write a generator called fibonacci() that yields Fibonacci
# numbers indefinitely. Then write a function called fib_stats()
# that takes n, consumes the first n Fibonacci numbers and returns:
# - The list of first n Fibonacci numbers
# - Sum of all even Fibonacci numbers in that list
# - Most common digit across all numbers (use Counter on digits)
def fibonacci(n):
    a,b=0,1
    i=1
    while i <=n:
        yield a
        a,b=b,a+b
        i+=1

def fib_stats(n):
    fib=list(fibonacci(n))
    return {
        "sequence":fib,
        "even_sum":sum(filter(lambda x : x%2==0,fib)),
        "most_common_digit":max(fib,key=fib.count)
    }

# Example:
# print(fib_stats(10))
# → {
#     "sequence": [0,1,1,2,3,5,8,13,21,34],
#     "even_sum": 44,
#     "most_common_digit": "1"
#   }


# MEDIUM (2) — [Decorators + datetime + Functions + Error Handling]
# Write a decorator called @timer that measures and prints how long
# a function takes to run in milliseconds. Then write a function
# called heavy_search() that takes a list and a target, searches
# for the target, raises ValueError if not found, and returns
# its index if found.
def timer(func):
    def wrapper(searches,target):
        start = datetime.now()
        try:
            result = func(searches,target)
            print(f"{target} found at index {result}")
        except ValueError as e:
            print(e)
        finally:
            end = datetime.now()-start
            print(f"{func.__name__} heavy_search took {timedelta.total_seconds(end) * 1000}ms")
    return wrapper

@timer
def heavy_search(searches,target):
    if  target not in searches:
        raise ValueError(f"{target} not found in list ")
    return searches.index(target)

# Example:
# heavy_search(list(range(1000000)), 999999)
# → [TIMER] heavy_search took 45.23ms
# → 999999 found at index 999999

heavy_search(list(range(100)), 999)
# → [TIMER] heavy_search took 0.12ms
# → ValueError: 999 not found in list