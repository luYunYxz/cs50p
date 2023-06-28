import sys

if len(sys.argv) < 2:
    sys.exit("the args to few")
elif len(sys.argv) >2:
    sys.exit("the args to log")
else:
    print("Hello , ",sys.argv[1])