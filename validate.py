import re

email = input("what is your name? ").strip()

if re.search("^\w+@\w+\.(gov|edu|com)$",email):
    print("Valid")
else:
    print("Invalid")