import sys
from saying import hello

def main():
    if len(sys.argv) >= 2:
        hello(sys.argv[1])

main()