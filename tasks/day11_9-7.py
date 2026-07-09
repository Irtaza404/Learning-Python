# DAY 11 — PYTHON PRACTICE
# ════════════════════════

# EASY (1) — [random + Functions + List Comprehension]
# Write a function called dice_simulator() that simulates
# rolling 2 dice n times and returns:
# - Total rolls
# - How many times sum was 7
# - Highest sum rolled
# - Results as a list of tuples (die1, die2, sum)

import random
def dice_simulator(n):
    results=[]
    seven,highest=0,0
    for _ in range(n):
        a,b=random.randint(1,6),random.randint(1,6)
        sum=a+b
        highest=max(highest,sum)
        match sum:
            case 7:seven+=1
        results.append((a,b,sum))
    
    return {
        "rolls": n,
        "sevens": seven,
        "highest": highest,
        "results": results
    }
        
# Example:
# print(dice_simulator(5))
# → {
#     "rolls": 5,
#     "sevens": 2,
#     "highest": 11,
#     "results": [(3,4,7), (2,5,7), (6,5,11), ...]
#   }


# EASY (2) — [datetime + String Formatting + Functions]
# Write a function called schedule_builder() that takes a list
# of (event, duration_minutes) tuples and a start time string
# "HH:MM", builds a schedule by adding durations one after
# another and returns a formatted schedule.

# Example:
# events = [("Breakfast", 30), ("Study", 120), ("Lunch", 45)]
# print(schedule_builder(events, "08:00"))
# →
# 08:00 - 08:30 | Breakfast
# 08:30 - 10:30 | Study
# 10:30 - 11:15 | Lunch
from datetime import datetime, timedelta

def schedule_builder(events, start_time_str):
    built = []
    current_time = datetime.strptime(start_time_str, "%H:%M")
    for event, minute in events:
        start_str = current_time.strftime("%H:%M")
        current_time = current_time + timedelta(minutes=minute)
        end_str = current_time.strftime("%H:%M")
        built.append(f"{start_str} - {end_str} | {event}")
    return built

# Example Execution:
events = [("Breakfast", 30), ("Study", 120), ("Lunch", 45)]
print(schedule_builder(events, "08:00"))


# MEDIUM (1) — [Closures + Decorators + Error Handling]
# Write a closure called make_retry() that takes max_attempts
# and returns a decorator that retries the decorated function
# up to max_attempts times on failure, with attempt tracking.

def make_retry(n):
    def deco(fun):
        def wrapper():
            for i in range(1,n+1):
                try:
                    res=fun()
                    print(f"Attempt {i}:{res}")
                except ValueError as e:
                    print(f"Attempt {i} failed:{e}")
        return wrapper
    return deco
# Example:
@make_retry(3)
def risky():
    import random
    if random.random() < 0.7:
        raise ValueError("Failed!")
    return "Success"

risky()
# → Attempt 1 failed: Failed!
# → Attempt 2 failed: Failed!
# → Attempt 3: Success!


# MEDIUM (2) — [Generators + zip() + enumerate() + map()]
# Write a generator called number_facts() that takes a list
# of numbers and yields a dict of facts for each number:
# - value, square, cube, is_even, digit_sum

# Then use map() and enumerate() to print each fact with
# its index number.
def number_facts(num):
    for n in num:
        yield {"value":n, "square":n**2, "cube":n**3, "is_even":(n & 1) == 0, "digit_sum":sum(int(digit) for digit in str(abs(n)))}
# Example:
print(list(number_facts([3, 7, 12])))
# → [
#     {"value":3, "square":9, "cube":27, "is_even":False, "digit_sum":3},
#     {"value":7, "square":49, "cube":343, "is_even":False, "digit_sum":7},
#     {"value":12, "square":144, "cube":1728, "is_even":True, "digit_sum":3}
#   ]


