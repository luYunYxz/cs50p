import sys

if len(sys.argv) == 1:
    print("meow")
elif len(sys.argv) == 3 and sys.argv[1] =="-n":
    for _ in range(int(sys.argv[2])):
        print("Meow")
else:
    print("meow\n"*3,end="")