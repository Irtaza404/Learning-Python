# DAY 14 — PYTHON PRACTICE
# ════════════════════════

# EASY (1) — [Regex + Functions]
# Extract all URLs from a text string.
# URLs start with http:// or https://

text = "Visit https://google.com or http://github.com/Irtaza404 for more info. Invalid: www.test.com"
import re
urls=re.findall(r"(http://[\w\./]+|https://[\w\./]+)",text)
print(urls)

# → ["https://google.com", "http://github.com/Irtaza404"]



# EASY (2) — [collections + Functions]
# Given a sentence, return top 3 most common letters
# (ignore spaces, case insensitive).

from collections import Counter
text = "Muhammad Irtaza is learning Python".replace(" ","").lower()
common=Counter(text).most_common(3)
print(common)

# → [("a", 5), ("m", 3), ("i", 3)]


# EASY (3) — [datetime + Functions]
# Given a list of date strings, return only dates
# that fall on a weekend (Saturday or Sunday).

from datetime import datetime
dates = ["15-01-2024", "16-01-2024", "20-01-2024", "21-01-2024"]
weekday=[]
for date in dates:
    d=datetime.strptime(date,"%d-%m-%Y")
    if d.strftime("%A") in ("Saturday","Sunday"):
        weekday.append(date)    
print(weekday)
# → ["20-01-2024", "21-01-2024"]


# MEDIUM (1) — [Generators + collections + Functions]
# Write a generator called chunk_gen() that takes a list
# and chunk size n, yields list in chunks of n.
# Then write most_common_chunk() that finds which chunk
# has the most repeated element using Counter.

def chunk_gen(l,size):
    for i in range(0,len(l),size):
        yield l[i:i+size] 
print(list(chunk_gen([1,2,3,4,5,6,7,8,9], 3)))

# → yields [1,2,3] then [4,5,6] then [7,8,9]

def most_common_chunk(lst,n):
    best_chunk = None
    best_count = 0
    common=None
    for chunk in chunk_gen(lst, n):
        c=Counter(chunk)
        if c.most_common(1)[0][1]  > best_count:
            best_chunk=chunk
            best_count=c.most_common(1)[0][1] 
            common=c.most_common(1)[0][0]  # → 3  (element)

    return {"chunk":best_chunk,"most_common":common,"count":best_count}


# → 3  (count)
print(most_common_chunk([1,1,2,3,3,3,2,2,2,4], 3))
# → {"chunk": [2,2,2], "most_common": 2, "count": 3}


# MEDIUM (2) — [Decorators + Functions + Error Handling]
# Write a decorator called @memoize that caches function
# results — if same arguments called again, return cached
# result instead of recalculating. Print whether result
# was cached or calculated.
def memoize(func):
    cached={}
    def wrapper(n):
        nonlocal cached
        if cached.get(n,0):
            return f"Cached: {cached.get(n)}"
        cached[n]=func(n)
        return f"Calculated: {cached.get(n)}"
    return wrapper
@memoize
def heavy_calc(n):
    return sum(range(n))

print(heavy_calc(1000))#  → "Calculated: 499500"
print(heavy_calc(1000))#  → "Cached: 499500"
print(heavy_calc(500) )#  → "Calculated: 124750"
print(heavy_calc(500) )

# MEDIUM (3) — [Generators + map() + filter() + Regex]
# Write a generator called csv_reader() that takes a
# multiline CSV string and yields one row at a time
# as a dict using the first line as headers.
# Then write clean_csv() that:
# - Filters rows where age < 18
# - Maps names to uppercase
# - Returns cleaned list of dicts

def csv_reader(cvc):
    for line in re.finditer(r"(?P<name>[A-Za-z ]+),(?P<age>\d+),(?P<email>[\w.]+@\w+\.com)\n?",cvc):
        yield line.groupdict()
def clean_csv(csv):
    return list(map(lambda row: {**row, "name": row["name"].upper()},filter(lambda x:int(x["age"])>=18,list(csv_reader(csv)))))


csv = """name,age,email
ali,25,ali@gmail.com
sara,15,sara@yahoo.com
zain,30,zain@gmail.com
hina,16,hina@gmail.com"""

print(clean_csv(csv))
# → [
#     {"name": "ALI", "age": "25", "email": "ali@gmail.com"},
#     {"name": "ZAIN", "age": "30", "email": "zain@gmail.com"}
#   ]


