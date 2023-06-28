import cowsay
import sys

if len(sys.argv) != 2:
    sys.exit("args to few")

cowsay.milk("hello " + sys.argv[1]) 