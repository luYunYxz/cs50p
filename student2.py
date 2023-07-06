class Student:
      ...

def main():
    student = get_student()
    if student.name == "Padma":
        student.house = "Ravenclaw"
    print(f"the {student.name} from {student.house}")

def get_student():
    name = input("what is your name: ") 
    house = input("what is your house: ")
    student = Student(name,house)
    return student 

if __name__ == "__main__":
    main()

