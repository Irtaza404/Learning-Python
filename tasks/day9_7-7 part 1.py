# DAY 9 — PYTHON PRACTICE
# ════════════════════════

# EASY (1) — [Regex + Functions + String Methods]
# Write a function called extract_emails() that takes a block of
# text and returns a list of all valid email addresses found.
import re
def extract_emails(text):
    valid_emails=re.findall("\w+@\w+.\w+",text)
    print(valid_emails)
    return valid_emails
# Example:
# text = "Contact us at support@gmail.com or admin@company.org, invalid@@email, test@.com"
# extract_emails(text)
# → ["support@gmail.com", "admin@company.org"]


# EASY (2) — [Regex + Functions + Conditionals]
# Write a function called validate_password() that checks if a
# password is strong. A strong password must have:
# - At least 8 characters
# - At least one uppercase letter
# - At least one lowercase letter
# - At least one digit
# - At least one special character (!@#$%^&*)
# Return "Strong" or "Weak: " with the reason why it failed.
def validate_password(password):
    error=[]
    if not re.search(".{8,}",password):
        error.append("less than 8 character")
    if not re.search("[A-Z]",password):
        error.append("uppercase")
    if not re.search("[a-z]",password):
        error.append("lowercase")
    if not re.search("[0-9]",password):
        error.append("digit")
    if not re.search("[!@#$%^&*]",password):
        error.append(" special character")
    
    return "Strong" if len(error)==0 else "Weak: "+" and".join(error)
            
# Example:
# print(validate_password("Hello@123"))  #→ "Strong"
# print(validate_password("hello123"))#   → "Weak: missing uppercase and special character"


# EASY (3) — [Regex + Functions + String Formatting]
# Write a function called mask_data() that takes a string and:
# - Masks all but last 4 digits of any credit card number (16 digits)
# - Masks email addresses (keeps first 2 chars and domain)
# - Masks phone numbers (keeps last 4 digits)
def mask_data(text):
    text=re.sub(r"\d{16}",lambda x: ("*"*12)+x.group()[12:] ,text)
    text=re.sub("\w+@\w+.\w+",lambda x: x.group()[:2]+("*"*12)+x.group()[x.group().index("@"):] ,text)
    text=re.sub(r"\d{4}-\d{7}", lambda x: "****" + x.group()[-4:], text)
    print(text)


# # Example:
# text = "Card: 1234567890123456, Email: irtaza@gmail.com, Phone: 0300-1234567"
# mask_data(text)
# # → "Card: ************3456, Email: ir****@gmail.com, Phone: ****4567"



# MEDIUM (1) — [Regex + Functions + collections]
# Write a function called log_analyzer() that takes a server log
# string and extracts:
# - All IP addresses
# - All timestamps (format: DD/MM/YYYY HH:MM:SS)
# - All HTTP status codes (3 digit numbers after GET/POST)
# - Most common IP using Counter

from collections import Counter
def log_analyzer(log):
    ips=re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",log)
    timestamps=re.findall(r"\d{2}/\d{2}/\d{4}\s\d{2}:\d{2}:\d{2}",log)
    status_code=re.findall(r"\b(200|404)\b",log)
    most_common=Counter(ips).most_common(1)[0][0]
    return {
        "ips":ips,
        "timestamps":timestamps,
        "status_code":status_code,
        "most_common":most_common
    }
    

# Example:
# log = """
# 192.168.1.1 GET /index.html 200 12/01/2024 10:30:00
# 192.168.1.2 POST /login 404 12/01/2024 10:31:00
# 192.168.1.1 GET /about 200 12/01/2024 10:32:00
# """
# print(log_analyzer(log))
# → {
#     "ips": ["192.168.1.1", "192.168.1.2", "192.168.1.1"],
#     "timestamps": ["12/01/2024 10:30:00", ...],
#     "status_codes": ["200", "404", "200"],
#     "most_common_ip": "192.168.1.1"
#   }


# MEDIUM (2) — [Regex + Error Handling + Functions + datetime]
# Write a function called parse_dates() that takes a list of
# date strings in mixed formats and converts them all to
# "DD-MM-YYYY" format. Use regex to detect the format and
# raise ValueError for unrecognized formats.

# Formats to handle:
# - "2024/01/15"   → YYYY/MM/DD
# - "15-01-2024"   → DD-MM-YYYY (already correct)
# - "January 15, 2024" → Month DD, YYYY
# - "15 Jan 2024"  → DD Mon YYYY
from  datetime import datetime,date
def parse_dates(dates):
    format=[]
    for date in dates:
        try:
            if re.match("\d+/\d+/\d+",date):
                dt = datetime.strptime(date, "%Y/%m/%d")  
                format.append(dt.strftime("%d-%m-%Y"))
            elif re.match("\d+-\d+-d+",date):
                dt = datetime.strptime(date, "%d-%m-%Y")  
                format.append(dt)
            elif re.match("\w+\s\d+,\s\d+",date):
                dt = datetime.strptime(date, "%B %d, %Y")  
                format.append(dt.strftime("%d-%m-%Y"))
            elif re.match("\d+\s\w+\s\d+",date):
                dt = datetime.strptime(date, "%d %b %Y")  
                format.append(dt.strftime("%d-%m-%Y"))
            else:
                raise ValueError(f"Unrecognized date format: {date}") 
        except ValueError as e:
            print(e)
    print(format)        


# Example:
# parse_dates(["2024/01/15", "January 15, 2024", "15 Jan 2024", "bad date"])
# → ["15-01-2024", "15-01-2024", "15-01-2024"]
# → ValueError: "Unrecognized date format: bad date"


# MEDIUM (3) — [Regex + Generators + Functions + map()]
# Write a generator called extract_data() that takes a list of
# strings and yields tuples of (original, numbers_found, words_found)
# for each string. Then write a function called summarize() that
# uses map() on the generator results to return a list of dicts.
def extract_data(data):
    for d in data:
        yield (d,re.findall("\d+",d),re.findall("[A-Za-z]+",d))
def summarize(data):
    return list(map(lambda x: {"original":x[0],"numbers":x[1],"words":x[2]} ,extract_data(data)))    

# Example:
data = ["hello 123 world", "python3 is 100% cool", "no digits here"]
print(summarize(data))
# → [
#     {"original": "hello 123 world", "numbers": [123], "words": ["hello", "world"]},
#     {"original": "python3 is 100% cool", "numbers": [3, 100], "words": ["python", "is", "cool"]},
#     {"original": "no digits here", "numbers": [], "words": ["no", "digits", "here"]}
#   ]

# EASY (1) — [String Format Specifiers + Functions + Loops]
# Write a function called print_table() that takes a list of
# tuples (product, price, quantity) and prints a perfectly
# aligned table with:
# - Product name: left aligned, 15 chars wide
# - Price: right aligned, 10 chars wide, 2 decimal places, with comma
# - Quantity: center aligned, 8 chars wide
# - A total row at the bottom
