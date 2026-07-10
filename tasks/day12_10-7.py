# DAY 12 — PYTHON PRACTICE
# ════════════════════════

# EASY (1) — [collections + Functions + Loops]
# Write a function called inventory_manager() that takes a list
# of (item, quantity) tuples, some items may repeat. Merge
# duplicates by summing quantities, return top 3 items by
# quantity using Counter.

from collections import Counter
def inventory_manager(items):
    new_items={}
    for item in items:
        if item[0] in new_items:
            new_items[item[0]]+=item[1]
        else:
            new_items[item[0]]=item[1]
    return Counter(new_items).most_common(3)
# Example:
items = [("apple",5),("banana",3),("apple",2),
        ("orange",8),("banana",4),("mango",1)]

# inventory_manager(items)
# → [("orange",8), ("banana",7), ("apple",7)]


# EASY (2) — [Regex + String Methods + Functions]
# Write a function called clean_text() that takes a messy string:
# - Removes extra whitespace (multiple spaces → one)
# - Removes special characters except . , ! ?
# - Capitalizes first letter of each sentence
# - Returns word count and cleaned text as tuple

import re 
def clean_text(text):
    text=re.sub(r'\s+', ' ', text)
    return(len(text.split(" ")),text.title())
    
# Example:
# print(clean_text("hello!!  world...  this   is  python!!!"))
# → (5, "Hello!! world... This is python!!!")


# MEDIUM (1) — [*args + **kwargs + Decorators + String Formatting]
# Write a function called styled_print() that takes:
# - *args as the content to print
# - **kwargs for style options:
#   - width (default 40)
#   - align ("left"/"right"/"center", default "center")
#   - border (default "═")
#   - title (default "")
def styled_print(*args,**kwargs,):
    width=kwargs.get("width",40)
    align=kwargs.get("align","center")
    border=kwargs.get("border","=")
    title=kwargs.get("title","")
    symbol = "^" if align == "center" else "<" if align == "left" else ">"
    print(border*width)
    print(f"{title:{symbol}{width}}")
    print(border*width)
    for i in args:
        print(f"{i:{symbol}{width}}")
    print(border*width)
    

# Example:
# styled_print("Irtaza", "Python Dev", "BIIT",
#             title="PROFILE", width=30, align="center")
# →
# ══════════════════════════════
#            PROFILE
# ══════════════════════════════
#             Irtaza
#         Python Dev
#               BIIT
# ══════════════════════════════


# MEDIUM (2) — [Generators + Error Handling + map() + filter()]
# Write a generator called file_simulator() that simulates
# reading a "file" line by line from a list of strings,
# raises StopIteration when done, skips empty lines.
# Then write process_file() that:
# - Uses filter() to keep lines with numbers
# - Uses map() to extract all numbers from each line
# - Returns dict with line count and all numbers found
def file_simulator(lines):
    for line in lines:
        if line.strip():
            yield line

from itertools import chain
def process_file(lines):
    lines=list(file_simulator(lines))
    number_lines=list(filter(lambda text:bool(re.search(r'\d', text)),lines))
    numbers = list(chain.from_iterable(map(lambda x: [int(n) for n in re.findall(r'\d+', x)], number_lines)))
    return {
        "total_lines": len(lines),
        "number_lines": len(number_lines),                     
        "all_numbers": numbers
    }
# Example:
lines = ["hello 123", "", "world", "age 25 score 98", "  ", "test 7"]
process_file(lines)
# → {
#     "total_lines": 4,
#     "number_lines": 3,                     
#     "all_numbers": [123, 25, 98, 7]
#   }




