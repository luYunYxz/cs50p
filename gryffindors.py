students = [
    {"name":"Hermione","house":"Gryffindoer"},
    {"name":"Harry","house":"Gryffindoer"},
    {"name":"Ron","house":"Gryffindoer"},
    {"name":"Draco","house":"Slytherin"}
]


gryfindoers = [
    student["name"] for student in students if student["house"] == "Gryffindoer"
]

for gryfindoer in sorted(gryfindoers):
    print(gryfindoer)