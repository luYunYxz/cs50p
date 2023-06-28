name = input("what is your name? ")

match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffinodr")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")