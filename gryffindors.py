students = [
    {"name":"Hermione","house":"Gryffindoer"},
    {"name":"Harry","house":"Gryffindoer"},
    {"name":"Ron","house":"Gryffindoer"},
    {"name":"Draco","house":"Slytherin"}
]



gryfindoers = filter(lambda s:s["house"] == "Gryffindoer",students) 


for gryfindoer in sorted(gryfindoers,key=lambda s:s["name"]):
    print(gryfindoer["name"])