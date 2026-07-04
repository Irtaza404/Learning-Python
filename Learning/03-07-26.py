# DATETIME PRACTICE
# ════════════════════════

# TASK 1 — Basics
# Write a function called date_info() that prints:
# - Current date in this format: "Monday, January 15, 2024"
# - Current time in this format: "10:30 AM"
# - Current year and month separately
from datetime import datetime
def date_info():
    now=datetime.now()
    print(now.strftime("%A, %B %d, %Y "))
    print(now.strftime("%I:%M %p"))
    print(now.year)
    print(now.month)

date_info()

# TASK 2 — timedelta
# Write a function called days_until_birthday() that takes a
# birthday as a string "DD-MM" and returns how many days
# until the next birthday from today.

# Example:
from datetime import timedelta,date,datetime
def days_until_birthday(dates):
    today=date.today()
    dates=datetime.strptime(dates,"%d-%m")
    next_birthday=date(today.year,dates.month ,dates.day)
    next_birthday= next_birthday -today
    print(f"{next_birthday.days} days until your birthday")
days_until_birthday("13-7")# → "X days until your birthday!"


# TASK 3 — strptime + difference
# Write a function called age_calculator() that takes a
# birthdate string "DD-MM-YYYY" and returns the person's
# exact age in years.

# Example:
from datetime import datetime,date
def age_calculator(dates):
    today=date.today()
    print(today)
    dates=datetime.strptime(dates,"%d-%m-%Y")
    dates=date(dates.year,dates.month,dates.day)
    age=today-dates
    print(f"You are {age.days//365} years old")
    
age_calculator("15-01-2000") # → "You are 24 years old"