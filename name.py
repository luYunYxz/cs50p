import sys

if len(sys.argv) < 2:
    sys.exit("the args to few")

for areg in sys.argv[1:]:
    print("hello ,",areg)