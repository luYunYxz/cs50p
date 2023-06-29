import csv
students = []

with open("student.csv") as file:
    reader = csv.reader(file)
    for line in reader:
        students.append({"name":line[0],"house":line[1]})

for student in sorted(students,key=lambda student : student["name"],reverse=True):
    print(f"{student['name']} is in {student['house']}")

