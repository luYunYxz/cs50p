import re
name = input("what is your name ? ").strip()

matcher = re.search("(.+), *(.+)",name)

if matcher:
    first = matcher.group(1)
    second = matcher.group(2)
    name = f"{first} {second}"

print(f"hello {name}")
