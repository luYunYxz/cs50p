
def main():
    name = get_name();
    house = get_house()
    print(f"the {name} from {house}")

def get_name():
    name = input("what is your name: ")
    return name
def get_house():
    house = input("what is your house: ")
    return house

if __name__ == "__main__":
    main()

