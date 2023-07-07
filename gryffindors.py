students = [
    {"name":"Hermione","house":"Gryffindoer"},
    {"name":"Harry","house":"Gryffindoer"},
    {"name":"Ron","house":"Gryffindoer"},
    {"name":"Draco","house":"Slytherin"}
]


def is_gryfindoer(student):
    return student["house"] == "Gryffindoer"

gryfindoers = filter(is_gryfindoer,students) 


for gryfindoer in sorted(gryfindoers,key=lambda s:s["name"]):
    print(gryfindoer["name"])