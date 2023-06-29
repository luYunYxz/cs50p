students = []

with open("student.csv") as file:
    for line in file:
        name,house = line.strip().split(",")
        students.append({"name":name,"house":house})

def get_name(student):
    return student["name"]

for student in sorted(students,key=lambda student : student["name"],reverse=True):
    print(f"{student['name']} is in {student['house']}")

