import csv
students = []

with open("student.csv") as file:
    reader = csv.DictReader(file)
    for line in reader:
        students.append({"name":line["name"],"house":line["house"]})

for student in sorted(students,key=lambda student : student["name"],reverse=True):
    print(f"{student['name']} is in {student['house']}")

