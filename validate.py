email = input("what is your name? ").strip()

first,second = email.split("@")

if "." in second:
    print("Valid")
else:
    print("Invalid")