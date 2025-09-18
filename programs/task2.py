
#Write a program to display all employee names and their departments.

employees = {
    "E001": {"name": "Alice", "department": "Finance"},
    "E002": {"name": "Bob", "department": "IT"},
    "E003": {"name": "Charlie", "department": "HR"}
}


for item in employees.values():
    print(item['name'], item['department'])

print("---------------------------")

for key,item in employees.items():
    print(item['name'],item['department'])

print("---------------------------")

for key in employees.keys():
    print(employees[key]['name'] , employees[key]['department'] )