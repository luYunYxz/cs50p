students = [
    {"name":"Hermione","house":"Gryffindor"},
    {"name":"Harry","house":"Gryffindor"},
    {"name":"Ron","house":"Gryffindor"},
    {"name":"Draco","house":"Slytherin"},
    {"name":"Padma","house":"Ravenclaw"},
]

house = []

for student in students:
    if student["house"] not in house:
        house.append(student["house"])

for h in sorted(house):
    print(h)