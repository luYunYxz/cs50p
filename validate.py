import re

email = input("what is your name? ").strip()

if re.search("^(\w|\s)+@\w+\.(gov|edu|com)$",email,re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")