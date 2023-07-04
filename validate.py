import re

email = input("what is your name? ").strip()

if re.search("^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.com$",email):
    print("Valid")
else:
    print("Invalid")