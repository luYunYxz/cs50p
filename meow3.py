import argparse

parser = argparse.ArgumentParser(description="number of moew ")
parser.add_argument("-n",default = 1,type = int,help="number of times to meow")
parser.add_argument("-a",default = 1,type = int,help="number of times to meow")

args= parser.parse_args()

for _ in range(args.n):
    print("meow")

print(args.a)