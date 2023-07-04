
name = input("what is your name ? ").strip()

if "," in name:
    first,second = name.split(", ")
    name = f"{first} {second}"

print("hello",name)