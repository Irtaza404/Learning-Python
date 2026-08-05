import csv

with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age", "Grade"])   # header row
    writer.writerow(["Ali", 20, "A"])
    writer.writerow(["Sara", 22, "B"])
    
import csv

with open("students.csv", "r", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

import csv

with open("students.csv", "r", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
        print(row["Name"], row["Age"])
        
import json

data = {
    "name": "Ali",
    "age": 20,
    "courses": ["Math", "CS"]
}

with open("student.json", "w") as f:
    json.dump(data, f)
    
    
# Copy an image file byte-for-byte
with open("C:\\Users\\Muhammad Irtaza\\Downloads\\economic-transactions-summary.xlsx", "rb") as f:
    data = f.read()

with open("photo_copy.xlsx", "wb") as f:
    f.write(data)