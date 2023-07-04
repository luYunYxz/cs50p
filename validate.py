import re

email = input("what is your name? ").strip()

if re.search("@",email):
    print("Valid")
else:
    print("Invalid")