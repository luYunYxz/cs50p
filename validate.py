email = input("What is you emial? ").strip()

if "@" in email and "." in email:
    print("Valid")
else:
    print("InValid")