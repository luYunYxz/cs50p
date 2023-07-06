class Student:
      ...

def main():
    student = get_student()
    if student.name == "Padma":
        student.house = "Ravenclaw"
    print(f"the {student.name} from {student.house}")

def get_student():
    student = Student()
    student.name = input("what is your name: ") 
    student.house = input("what is your house: ")
    return student 

if __name__ == "__main__":
    main()

