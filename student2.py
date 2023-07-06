
def main():
    student = get_student()
    print(f"the {student[0]} from {student[1]}")

def get_student():
    name = input("what is your name: ") 
    house = input("what is your house: ")
    return (name,house)

if __name__ == "__main__":
    main()

