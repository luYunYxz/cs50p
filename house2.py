students = [
    {"name":"Hermione","house":"Gryffindor"},
    {"name":"Harry","house":"Gryffindor"},
    {"name":"Ron","house":"Gryffindor"},
    {"name":"Draco","house":"Slytherin"},
    {"name":"Padma","house":"Ravenclaw"},
]

house = set()

for student in students:
    house.add(student["house"])

for h in sorted(house):
    print(h)