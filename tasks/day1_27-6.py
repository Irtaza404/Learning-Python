# DAY 1 — PYTHON PRACTICE
# ════════════════════════

# EASY (1) — [Strings + Functions + f-strings]
# Write a function called format_name_card() that takes a first name,
# last name, and job title as parameters. It should return a formatted
# name card string. The name should be title-cased, and the total width
# of the card border should adapt to the longest line.

# Example:
# format_name_card("muhammad", "irtaza", "AI Engineer")
# →
# ┌─────────────────────┐
# │  Muhammad Irtaza    │
# │  AI Engineer        │
# └─────────────────────┘

def format_name_card(firstname,lastname,job):
    name=(firstname+" "+lastname)
    size=len(name) if len(name)> len(job) else len(job)
    size+=5
    print(f"┌{"".center(size,"─")}┐\n│{name.title().center(size)}│\n│{job.title().center(size)}│\n└{"".center(size,"─")}┘")

format_name_card("muhammad", "irtaza", "AI Engineer")
    

# EASY (2) — [Dictionaries + Loops + Conditionals]
# Write a function called grade_report() that takes a dictionary of
# {subject: score} pairs and returns a new dictionary with:
# - The letter grade (A/B/C/D/F) added for each subject
# - A "passed" key (True/False, passing = score >= 50)
# - An "average" key with the class average (rounded to 2 decimal places)

# Grading: A=90+, B=80+, C=70+, D=60+, F=below 60

# Example:
# grade_report({"Math": 92, "English": 74, "Physics": 55})
# →
# {
#   "Math":    {"score": 92, "grade": "A", "passed": True},
#   "English": {"score": 74, "grade": "C", "passed": True},
#   "Physics": {"score": 55, "grade": "F", "passed": True},
#   "average": 73.67
# }

def grade_report(pairs):
    report={}
    scores=0
    for subject,score in pairs.items():
        grade= "A"if score>=90 else "B" if score>=80 else"C"if score>=70 else "D"if score>=60 else"F"
        passing=True if score>=60 else False
        report[subject]={"score":score,"grade":grade,"passed":passing}
        scores+=score
    report["average"]=round(scores/len(report),2)
    print(report)
grade_report({"Math": 92, "English": 74, "Physics": 55})

# MEDIUM (1) — [Generators + Functions + Conditionals]
# Write a generator function called prime_gen() that yields prime numbers
# indefinitely starting from 2. Then write a function called
# first_n_primes_squared() that uses your generator, takes n as input,
# and returns a list of the first n primes — but only includes the square
# of the prime if it's odd-indexed (index 1, 3, 5...), otherwise the
# prime itself.

# Example:
# first_n_primes_squared(6)
# → [2, 9, 5, 49, 11, 169]
# # index 0→2, index 1→3²=9, index 2→5, index 3→7²=49 ...
def prime_gen():
    n=2
    while True:
        checker=True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                checker=False
                break
        if checker:
            yield n
        n+=1
# same and short
# def prime_gen():
#     n = 2
#     while True:
#         if all(n % i != 0 for i in range(2, int(n ** 0.5) + 1)):
#             yield n
#         n += 1

def first_n_primes_squared(N):
    gen=prime_gen()
    primes=[]
    for _ in range(N):
        prime=next(gen)
        if _ %2!=0:
            prime**=2
        primes.append(prime)
    return primes

print(first_n_primes_squared(6))      

# MEDIUM (2) — [Collections + map()/filter() + Lambda + Dictionaries]
# You're given a list of student records as tuples:
# (name, scores_list)

# Write a function called analyze_class() that:
# 1. Uses map() to compute each student's average score
# 2. Uses filter() to keep only students with average >= 60
# 3. Uses collections.Counter to count how many students fall into
#    each grade band (A/B/C/D) among the passing students
# 4. Returns a dict with "passed" (list of names) and "grade_dist" (Counter)

# Example:
# students = [("Ali", [90, 85, 92]), ("Sara", [40, 55, 45]),
#             ("Zain", [70, 68, 74]), ("Hina", [80, 79, 83])]

# analyze_class(students)
# → {
#     "passed": ["Ali", "Zain", "Hina"],
#     "grade_dist": Counter({"A": 1, "B": 1, "C": 1})
#   }
from collections import Counter
def analyze_class(students):
    average=list(map(lambda s:(s[0],sum(s[1])/len(s[1])) ,students))
    passed=list(filter(lambda avg : avg[1]>=60,average))
    grade_dist= Counter(map(lambda s: "A"if s[1]>=90 else "B" if s[1]>=80 else"C"if s[1]>=70 else "D"if s[1]>=60 else"F", passed))
    return {"Passed":[s[0]for s in passed],"grade_dist":grade_dist}

students = [("Ali", [90, 85, 92]), ("Sara", [40, 55, 45]),
            ("Zain", [70, 68, 74]), ("Hina", [80, 79, 83])]


print(analyze_class(students))


# HARD — [Functions + Recursion + Decorators + Generators + Collections + Datetime]
# Build a mini Task Scheduler CLI system with the following features:

# 1. A decorator called @log_call that logs every function call with
#    its timestamp (use datetime) and how many times it has been called
#    (use collections.Counter stored outside the function)

# 2. A recursive function flatten_tasks() that takes a nested task list
#    (tasks can contain sub-tasks as lists) and returns a flat list

# 3. A generator called task_stream() that yields one task at a time
#    from the flattened list, skipping any task that starts with "SKIP:"

# 4. A function run_scheduler() that:
#    - Accepts a nested task list
#    - Flattens it using flatten_tasks()
#    - Streams tasks using task_stream()
#    - Prints each task with its index number
#    - Is decorated with @log_call
#    - At the end prints total tasks processed and skipped count

# Example:
# tasks = ["Email client", ["SKIP: Update docs", "Fix bug"], 
#          ["Deploy app", ["SKIP: Write tests", "Code review"]]]
