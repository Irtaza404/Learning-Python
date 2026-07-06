# DAY 6 — PYTHON PRACTICE
# ════════════════════════

# EASY (1) — [String Format Specifiers + Functions]
# Write a function called format_invoice() that takes a list of
# tuples (item, price, quantity) and prints a formatted invoice.

# Example:
items = [("Keyboard", 2000.5, 2), ("Mouse", 1500.0, 1), ("USB Hub", 800.75, 3)]
def format_invoice(items):
    
    print(f"{"="*33}\nItems{"Price".center(23)}Qty\n{"="*33}")
    total=0
    for Item,Price,Qty in items:
        print(f"{Item}{Price:^25}{Qty}")
        total+=Price
    print("="*33)
    print(f"Total{total:^23}")
format_invoice(items)
# →
# ════════════════════════════════════
# Item                Price       Qty
# ════════════════════════════════════
# Keyboard         Rs.4,001.00     2
# Mouse            Rs.1,500.00     1
# USB Hub          Rs.2,402.25     3
# ════════════════════════════════════
# Total            Rs.7,903.25


# EASY (2) — [Error Handling + Functions]
# Write a function called safe_divide() that:
# - Takes two inputs from the user (use input())
# - Handles ValueError if non-numeric input is given
# - Handles ZeroDivisionError if dividing by zero
# - Uses else to print the result if no error
# - Uses finally to always print "Operation complete"
# def safe_drive():
#     try:
#         a=int(input("Enter numerator:"))
#         b=int(input("Enter denominator:"))
#         result=a/b
#     except ValueError:
#         print("Invalid input — numbers only")
#     except ZeroDivisionError:
#         print("Cannot divide by zero")
#     else:
#         print(result)
#     finally:
#         print("Operation complete")
# safe_drive()
# Example:
# Enter numerator: 10
# Enter denominator: 0
# → Error: Cannot divide by zero
# → Operation complete

# Enter numerator: abc
# → Error: Invalid input — numbers only
# → Operation complete


# MEDIUM (1) — [Custom Exceptions + Error Handling + Functions]
# Create a custom exception called InsufficientFundsError.
# Write a function called withdraw() that takes a balance and
# withdrawal amount — raises InsufficientFundsError if amount
# exceeds balance, raises ValueError if amount is negative,
# otherwise returns the new balance.
class InsufficientFundsError(Exception):
    pass

def withdraw(balance,withdrawal_amount):
    if withdrawal_amount<0:
        raise ValueError("Withdrawal amount cannot be negative")
    if withdrawal_amount>balance:
        raise InsufficientFundsError(f"Insufficient funds. Balance: Rs.{balance}, Requested: Rs.{withdrawal_amount}")
    print(balance-withdrawal_amount)

try:
    withdraw(1000,500)
    withdraw(1000, 1500)
    withdraw(1000, -100)
except (InsufficientFundsError,ValueError) as e:
    print(e)

# Example:
# withdraw(1000, 500)   → 500
# withdraw(1000, 1500)  → InsufficientFundsError: "Insufficient funds. Balance: Rs.1000, Requested: Rs.1500"
# withdraw(1000, -100)  → ValueError: "Withdrawal amount cannot be negative"



# MEDIUM (2) — [random + Decorators + Error Handling]
# Write a decorator called @retry that retries a function up to
# 3 times if it raises an exception, with a 0 second wait.
# Then write a function called risky_operation() that generates
# a random number 1-10 and raises ValueError if it's less than 8
# (simulating a flaky operation). Print attempt number each try.

def retry(func):
    def wrapper(*args, **kwargs):
        for i in range(1,4):
            try:
                result=func()
                print (f"Attempt {i} success! got {result}")
                return result
            except ValueError:
                print (f"Attempt {i} failed")
    return wrapper
import random

@retry
def risky_operation():
    number=random.randint(1,10)
    if number <8:
        raise ValueError()
    return number




# Example:
risky_operation()
# → Attempt 1 failed...
# → Attempt 2 failed...
# → Attempt 3: Success! Got 9