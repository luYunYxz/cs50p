import re

url = input("URL: ").strip()
if matcher:= re.match("^https?://(www\.)?twitter\.com/(.+)$",url):
    print(f"Username: {matcher.group(2)}")