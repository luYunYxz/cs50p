import sys

def hello(name):
    print("hello, " + name)

def goodbye(name):
    print("bye bye ! " + name)


def main():
    if len(sys.argv) >=2:
        hello(sys.argv[1])
        goodbye(sys.argv[1])


main()