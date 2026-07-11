# # random module
# # import random

# # random.random()           # float between 0.0 and 1.0
# # random.randint(1, 10)     # int between 1 and 10 (inclusive)
# # random.randrange(0, 10, 2) # like range() but random → 0,2,4,6,8
# # random.uniform(1.5, 5.5)  # float between 1.5 and 5.5

# # lst = [1, 2, 3, 4, 5]
# # random.choice(lst)        # one random item
# # random.choices(lst, k=3)  # 3 random items (with repetition)
# # random.sample(lst, 3)     # 3 random items (no repetition)
# # random.shuffle(lst)       # shuffles in place → returns None

# # random.seed(42)           # makes random reproducible
# # random.gauss(0, 1)        # gaussian distribution (mean, std)

# # Quick reference:
# # FunctionUserandom()float 0-1randint(a,b)int inclusiveuniform(a,b)float inclusivechoice(lst)one itemchoices(lst,k=n)n items with repeatssample(lst,n)n items no repeatsshuffle(lst)shuffle in placeseed(n)reproducible results





# # import math

# # # Rounding
# # math.floor(3.7)     # → 3 (round down)
# # math.ceil(3.2)      # → 4 (round up)
# # math.trunc(3.9)     # → 3 (remove decimal)

# # # Power & roots
# # math.sqrt(16)       # → 4.0
# # math.pow(2, 10)     # → 1024.0
# # math.log(100, 10)   # → 2.0 (log base 10)
# # math.log2(8)        # → 3.0
# # math.log10(1000)    # → 3.0

# # # Trig
# # math.sin(math.pi/2) # → 1.0
# # math.cos(0)         # → 1.0
# # math.degrees(math.pi) # → 180.0
# # math.radians(180)   # → 3.14...

# # # Constants
# # math.pi             # → 3.14159...
# # math.e              # → 2.71828...
# # math.inf            # → infinity
# # math.nan            # → not a number

# # # Other
# # math.factorial(5)   # → 120
# # math.gcd(12, 8)     # → 4
# # math.isnan(x)       # → True/False
# # math.isinf(x)       # → True/False
# # math.fabs(-5)       # → 5.0 (absolute float)



# # import time

# # # Current time
# # time.time()           # → seconds since 1970 (epoch) as float
# #                       # → 1705312200.123456

# # # Pause execution
# # time.sleep(2)         # pause for 2 seconds
# # time.sleep(0.5)       # pause for 500ms

# # # Measure execution speed
# # start = time.time()
# # # ... code ...
# # end = time.time()
# # print(f"Took {end - start:.2f}s")

# # # More precise measurement
# # start = time.perf_counter()
# # # ... code ...
# # end = time.perf_counter()
# # print(f"Took {end - start:.4f}s")

# # time() vs perf_counter():
# # Usetime.time()real world timestampstime.perf_counter()measuring code speed (more precise)

# # Quick example:
# # pythonimport time

# # def slow_function():
# #     time.sleep(1.5)
# #     return "done"

# # start = time.perf_counter()
# # slow_function()
# # end = time.perf_counter()
# # print(f"Took {end-start:.2f}s")  # → Took 1.50s


# # from datetime import datetime, date, timedelta

# # # Current
# # datetime.now()        # date + time
# # date.today()          # date only

# # # Access parts
# # now.year, now.month, now.day
# # now.hour, now.minute, now.second

# # # Format
# # now.strftime("%d-%m-%Y %I:%M %p")  # → "15-01-2024 10:30 AM"

# # # Parse string → datetime
# # datetime.strptime("15-01-2024", "%d-%m-%Y")

# # # Arithmetic
# # date.today() + timedelta(days=7)   # next week
# # date.today() - timedelta(days=30)  # 30 days ago

# # # Difference
# # d1 - d2  # → timedelta object
# # (d1 - d2).days  # → number of days


# # The difference
# # pythonimport time
# # from datetime import datetime, date, timedelta
# # These are two separate modules with different purposes:
# # time moduledatetime modulePurposemeasuring time, pausingworking with dates and timesMain usesleep(), timing codecalendars, schedules, formattingReturnsfloat (seconds)datetime objects

# # time module — think of it as a stopwatch
# # pythonimport time

# # # pause
# # time.sleep(2)          # wait 2 seconds

# # # measure speed
# # start = time.perf_counter()
# # # your code here
# # end = time.perf_counter()
# # print(end - start)     # how long it took
# # That's literally all you use it for.

# # datetime module — think of it as a calendar
# # Three things inside it:
# # date — only date, no time:
# # pythonfrom datetime import date
# # today = date.today()   # → 2024-01-15
# # today.day              # → 15
# # today.month            # → 1
# # today.year             # → 2024
# # datetime — date AND time together:
# # pythonfrom datetime import datetime
# # now = datetime.now()   # → 2024-01-15 10:30:45
# # now.hour               # → 10
# # now.minute             # → 30
# # timedelta — a duration, used for arithmetic:
# # pythonfrom datetime import date, timedelta
# # today = date.today()
# # next_week = today + timedelta(days=7)
# # yesterday = today - timedelta(days=1)

# # # difference between two dates
# # d1 = date(2024, 1, 1)
# # d2 = date(2024, 1, 15)
# # diff = d2 - d1
# # diff.days   # → 14

# # strftime vs strptime — the confusing ones
# # strftime — datetime → string (f = format):
# # pythonnow = datetime.now()
# # now.strftime("%d-%m-%Y")    # → "15-01-2024"
# # now.strftime("%I:%M %p")    # → "10:30 AM"
# # strptime — string → datetime (p = parse):
# # pythondatetime.strptime("15-01-2024", "%d-%m-%Y")  # → datetime object
# # Memory trick:

# # format → datetime to string
# # parse → string to datetime


# # Format codes — only the useful ones
# # CodeMeaningExample%Yfull year2024%mmonth number01%dday number15%Bmonth nameJanuary%Aday nameMonday%Hhour 24h14%Ihour 12h02%Mminutes30%pAM/PMPM

# # String → datetime → arithmetic → string
# # pythonfrom datetime import datetime, timedelta

# # # Step 1 — convert strings to datetime
# # d1 = datetime.strptime("15-01-2024", "%d-%m-%Y")
# # d2 = datetime.strptime("20-01-2024", "%d-%m-%Y")

# # # Step 2 — subtract to get difference
# # diff = d2 - d1
# # diff.days   # → 5

# # # Step 3 — add duration
# # new_date = d1 + timedelta(days=10)

# # # Step 4 — convert back to string
# # new_date.strftime("%d-%m-%Y")  # → "25-01-2024"

# # Full example:
# # pythonbirthday = "25-12-2000"
# # b = datetime.strptime(birthday, "%d-%m-%Y")

# # today = datetime.now()

# # # how many days since birthday
# # diff = today - b
# # print(diff.days)   # → some number of days

# # # next birthday
# # next_b = b.replace(year=today.year)
# # days_until = next_b - today
# # print(days_until.days)  # → days until next birthday

# # Key thing — you can only do arithmetic on datetime objects, not strings. So always:

# # Parse string → datetime with strptime
# # Do arithmetic
# # Format back → string with strftime if needed


# # DATETIME PRACTICE
# # ══════════════════
# from  datetime  import datetime,timedelta
# # TASK 1
# # Given two date strings, find difference in days:
# d1 = "10-03-2024"
# d2 = "25-07-2024"
# diff=datetime.strptime(d2,"%d-%m-%Y")-datetime.strptime(d1,"%d-%m-%Y")
# print(diff.days)

# # TASK 2
# # Add 45 days to a given date string and return
# # result as string in same format:
# date = "15-01-2024" #→ "01-03-2024"
# date=datetime.strptime(date,"%d-%m-%Y")
# date=date+timedelta(days=45)
# date=date.strftime("%d-%m-%Y")
# print(date)

# # TASK 3
# # Given a birthday string "25-12-2000", print:
# # - Age in years
# # - Days until next birthday
# # - Day name of birthday (Monday/Tuesday etc)
# from datetime import datetime,date 
# bdate=datetime.strptime("13-7-2005","%d-%m-%Y")
# today=datetime.now()
# years=today.year-bdate.year
# print(years)
# day= bdate.replace(year=today.year)- today
# print(day.days)
# print(bdate.strftime("%A"))

# regex — re module
# pythonimport re

# # Main functions
# re.search(pattern, text)    # first match anywhere
# re.match(pattern, text)     # match at start only
# re.findall(pattern, text)   # list of all matches
# re.sub(pattern, repl, text) # replace matches
# re.split(pattern, text)     # split by pattern

# Common patterns
# python\d      # digit
# \w      # letter/digit/underscore
# \s      # whitespace
# .       # any character
# ^       # start of string
# $       # end of string
# [abc]   # a or b or c
# [^abc]  # not a, b or c

# Quantifiers
# python+       # one or more
# *       # zero or more
# ?       # zero or one
# {3}     # exactly 3
# {2,5}   # between 2 and 5

# Groups
# python(abc)         # capture group
# (?:abc)       # non-capture group
# r"(\d+)-(\d+)" # multiple groups

# match.group(0)  # entire match
# match.group(1)  # first group
# match.group(2)  # second group

# Quick examples
# pythonre.findall(r"\d+", "age 25 score 98")
# # → ["25", "98"]

# re.sub(r"\s+", " ", "hello   world")
# # → "hello world"

# re.match(r"\d{4}-\d{2}-\d{2}", "2024-01-15")
# # → match object


# REGEX PRACTICE
# ══════════════
import re
# 1. Extract all hashtags from:
#    "Love #python and #coding, hate #bugs"
#    → ["#python", "#coding", "#bugs"]
print(re.findall(r"#\w+","Love #python and #coding, hate #bugs"))

# 2. Validate a Pakistani phone number:
#    Must be: 03XX-XXXXXXX
#    "0300-1234567" → Valid
#    "123-456"      → Invalid
print("valid" if re.findall(r"03\d{2}-\d{7}","123-456") else "Invalid") 

# 3. Extract name and age from:
#    "Ali is 25 years old, Sara is 30 years old"
#    → [("Ali", "25"), ("Sara", "30")]
print(re.findall(r"(\w+) is (\d+) ","Ali is 25 years old, Sara is 30 years old")) 


# 4. Replace all prices with "PKR X":
#    "Item costs $25 and $30 and $100"
#    → "Item costs PKR X and PKR X and PKR X"
print(re.sub(r"\$\d+","PKR X ","Item costs $25 and $30 and $100")) 

# 5. Extract domain from emails:
#    "ali@gmail.com and sara@yahoo.com"
#    → ["gmail.com", "yahoo.com"]

print(re.findall(r"@(\w+\.com)","ali@gmail.com and sara@yahoo.com")) 

























