# DAY 13 — PYTHON PRACTICE
# ════════════════════════

# EASY (1) — [Functions + Regex + String Formatting]
# Write a function called parse_contacts() that takes a messy
# string of contacts and extracts name, phone, and email
# into a clean list of dicts.

# Example:
text = """
John Doe | 0300-1234567 | john@gmail.com
Sara Khan | 0311-9876543 | sara@yahoo.com
Invalid line here
Ali | 0333-1111111 | notanemail
"""
import re
def parse_contacts(text):
    data=re.findall(r"(.+)\s*\|\s*(03\d{2}-\d{7})\s*\|\s*(\w+\@\w+\.com)",text)
    contact=[]
    for name ,phone,email in data:
        contact.append({"name":name,"phone":phone,"email":email})
        
    print(contact)
    return contact
# parse_contacts(text)
# → [
#     {"name": "John Doe", "phone": "0300-1234567", "email": "john@gmail.com"},
#     {"name": "Sara Khan", "phone": "0311-9876543", "email": "sara@yahoo.com"}
#   ]


# EASY (2) — [collections + datetime + Functions]
# Write a function called activity_tracker() that takes a list
# of (activity, duration_minutes, date_string) tuples and returns:
# - Total time per activity
# - Most productive day (most total minutes)
# - Longest single session

from collections import Counter
def activity_tracker(logs):
    by_activity={}
    busiest_day={}
    for activity, duration_minutes, date_string in logs:
        if activity in by_activity:
            by_activity[activity]+=duration_minutes
        else:
            by_activity[activity]=duration_minutes
        
        if date_string in busiest_day:
            busiest_day[date_string]+=duration_minutes
        else:
            busiest_day[date_string]=duration_minutes
    
    return {
        "by_activity":by_activity,
        "busiest_day":max(busiest_day,key=busiest_day.get),
        "Longest_session":max(map(lambda x:(x[0],x[1]),logs),key=lambda x:x[1])
    }
# Example:
logs = [
    ("Study", 120, "15-01-2024"),
    ("Exercise", 45, "15-01-2024"),
    ("Study", 90, "16-01-2024"),
    ("Reading", 60, "16-01-2024"),
    ("Exercise", 30, "16-01-2024")
]
print(activity_tracker(logs))
# → {
#     "by_activity": {"Study": 210, "Exercise": 75, "Reading": 60},
#     "busiest_day": "15-01-2024",
#     "longest_session": ("Study", 120)
#   }


# MEDIUM (1) — [Generators + Regex + map() + filter()]
# Write a generator called log_reader() that takes a list of
# log strings and yields only ERROR and WARNING logs as dicts.
# Then write analyze_logs() that uses map() and filter() to:
# - Count errors vs warnings
# - Extract all mentioned file names (word ending in .py/.txt/.log)
# - Return summary dict
from itertools import chain
def log_reader(logs):
    for log in logs:
        if search:=re.search("^(ERROR|WARNING)",log):
            yield {"type": search.group(1), "message": log.split(": ", 1)[1]}

def analyze_logs(logs):
    log=list(log_reader(logs))
    error=filter(lambda x: x["type"] == "ERROR", log)
    warning=filter(lambda x: x["type"] == "WARNING", log)
    files = list(chain.from_iterable(map(lambda x: re.findall(r"\w+\.(?:py|txt|log)", x["message"]), log)))
    return {
    "errors": len(list(error)),
    "warnings": len(list(warning)),
    "files": files
    }
    
# Example:
logs = [
    "INFO: Server started",
    "ERROR: Failed to open config.txt",
    "WARNING: Low memory in app.py",
    "ERROR: Crash in main.log",
    "INFO: All good"
]
print(analyze_logs(logs))
# → {
#     "errors": 2,
#     "warnings": 1,
#     "files": ["config.txt", "app.py", "main.log"]
#   }


# MEDIUM (2) — [Decorators + Error Handling + datetime + Functions]
# Write a decorator called @rate_limit that allows a function
# to be called maximum n times per session. After limit is
# reached print "Rate limit exceeded" and block the call.
# Also log each call with timestamp.

# Then apply it to a function called send_message() that takes
# a message string and prints it.
from datetime import datetime
def rate_limit(n):
    def doc(func):
        count=1
        def wrapper(mess):
            nonlocal count
            if count<=n:
                print(f"[{datetime.now().strftime("%H:%M:%S")}]",end=" ")
                func(mess)
                print(f"({count}/{n})")
                count+=1    
            else:
                print(f"Rate limit exceeded ({n}/{n} used) ")
        return wrapper
    return doc
        
            

# Example:
@rate_limit(3)
def send_message(msg):
    print(f"Sent: {msg}",end=" ")

send_message("Hi")      #→ [10:30:02] Sent: Hi (2/3)
send_message("Hello")   #→ [10:30:01] Sent: Hello (1/3)
send_message("Hey")     #→ [10:30:03] Sent: Hey (3/3)
send_message("Yo")      #→ Rate limit exceeded (3/3 used)

