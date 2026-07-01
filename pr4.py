import json

with open("students.json", "r", encoding="utf-8") as f:
    students = json.load(f)


katta_bal = max(students, key=lambda x: x["grade"])
kichik_bal = min(students, key=lambda x: x["grade"])
    
print(katta_bal["name"], katta_bal["grade"])
print(kichik_bal["name"], kichik_bal["grade"])


total = 0
for i in students:
    total += i["grade"]

print(total/len(students))