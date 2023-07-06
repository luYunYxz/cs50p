
class Student:
     def __init__(self,name,house) :
        self.name = name
        self.house = house
    
     def __str__(self):
        return f"{self.name} from {self.house}"

     @property
     def house(self):
        return self._house

     @house.setter
     def house(self,house):
        if house not in ["Gryffindor","Hufflepuff","Ravenclaw"]:
            raise ValueError("Invalid house")
        self._house = house
    
     @property
     def name(self):
        return self._name

     @name.setter 
     def name(self,name):
        if not name:
            raise ValueError("name is invalid")
        self._name = name


     @classmethod 
     def get_student(cls):
        name = input("what is your name: ") 
        house = input("what is your house: ")
        return cls(name,house) 
   
    
    

def main():
    student = Student.get_student()
    if student.name == "Padma":
        student.house = "Ravenclaw"
    print(f"the {student.name} from {student.house}")


if __name__ == "__main__":
    main()

