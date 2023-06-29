with open("student.csv","r") as file:
    for line in file:
        name,rom=lineg.rstrip().split(",")
        print(f"{name} is in {rom}")