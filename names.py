names = []

with open("names.txt") as file:
    for line in file:
        names.append(line)

for name in sorted(names):
    print(f"hello, ",name.rstrip())