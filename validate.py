import re

email = input("what is your name? ").strip()

if re.search("^\w+@\w+\.com$",email):
    print("Valid")
else:
    print("Invalid")