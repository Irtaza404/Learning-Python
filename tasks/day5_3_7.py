# DAY 5 — PYTHON PRACTICE
# ════════════════════════

# EASY (1) — [Sets + List Comprehension]
# Given two lists, find:
# - Common elements (intersection)
# - Elements only in list1 (difference)
# - All unique elements combined (union)
# Return all three as a dict.

list1 = [1, 2, 3, 4, 5, 2, 3]
list2 = [3, 4, 5, 6, 7, 4, 5]

# Expected output:
# {
#   "common": {3, 4, 5},
#   "only_in_list1": {1, 2},
#   "all_unique": {1, 2, 3, 4, 5, 6, 7}
# }
list1=set(list1)
list2=set(list2)
solution={
    "Common":list1 & list2 ,
    "only_in_list1":list1-list2,
    "all_unique":list1^list2
}
print(solution)

# EASY (2) — [Tuples + Functions + Unpacking]
# Write a function called min_max_avg() that takes any number of
# numbers using *args and returns a tuple of (min, max, average).
# Then unpack and print the result in one line.

# Example:
# min_max_avg(4, 7, 1, 9, 3, 6)
# → (1, 9, 5.0)

def min_max_avg(*a):
    return min(a),max(a),sum(a)/len(a)
mn, mx, avg = min_max_avg(4, 7, 1, 9, 3, 6)
print(f"Min: {mn} | Max: {mx} | Avg: {avg}")
# → Min: 1 | Max: 9 | Avg: 5.0


# MEDIUM (1) — [Dictionary + Sorting + Lambda]
# Write a function called top_scorers() that takes a dict of
# {player: scores_list} and returns a new dict of top 3 players
# sorted by their average score (highest first).
# Include the average in the result rounded to 1 decimal.

def top_scorers(players):
    for player,scores in players.items():
        players[player]=round(sum(scores)/len(scores),1)
    
    players=sorted(players.items(),key=lambda x:x[1],reverse=True)
    return dict(players[:3])
# Example:
players = {
    "Ali":  [88, 92, 79],
    "Sara": [95, 98, 100],
    "Zain": [70, 65, 80],
    "Hina": [85, 90, 88],
    "Omar": [60, 55, 70]
}
print(top_scorers(players))
# → {
#     "Sara": 97.7,
#     "Hina": 87.7,
#     "Ali":  86.3
#   }



# MEDIUM (2) — [enumerate() + zip() + List Comprehension]
# Write a function called merge_ranked() that takes two lists of
# names, zips them into pairs, and returns a list of strings showing
# the rank, name from list1 and name from list2 side by side.

# Example:
# merge_ranked(["Ali", "Sara", "Zain"], ["Hina", "Omar", "Nida"])
# → [
#     "#1 | Ali vs Hina",
#     "#2 | Sara vs Omar",
#     "#3 | Zain vs Nida"
#   ]

def merge_ranked(list1,list2):
    list3=[]
    for i,name in enumerate(zip(list1,list2),start=1):
        list3.append(f"#{i} | {name[0]} vs {name[1]}")
    print(list3)
    return list3
merge_ranked(["Ali", "Sara", "Zain"], ["Hina", "Omar", "Nida"])

# MEDIUM (3) — [*args + **kwargs + Decorators]
# Write a decorator called @debug that prints the function name,
# the arguments it received, and the result it returned — every
# time the function is called.

# Then apply it to a simple function called calculate() that takes
# two numbers and an operation (add/sub/mul/div) as a keyword arg.
    
def debug(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} calculate called with args={args} kwargs={kwargs}")
        result = func(*args, **kwargs)  
        print(f"{func.__name__} calculate returned: {result}")
        return result
    return wrapper

@debug
def calculate(*args,**kwargs):
    match kwargs.get("operation"):
        case "add": return args[0]+args[1]
        case "sub": return args[0]-args[1]
        case "mul": return args[0]*args[1]
        case "div": return args[0]/args[1]
        case _:return "invalid operation"



# Example:
calculate(10, 5, operation="add")
# → [DEBUG] calculate called with args=(10, 5) kwargs={'operation': 'add'}
# → [DEBUG] calculate returned: 15
# → 15
