
def main():
    print_square(5)
def print_square(n):
    for _ in range(n):
        for _ in range(n):
            print("#",end="")
        print()
        
main()