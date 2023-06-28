
def main():
    print_square(5)

def print_square(n):
    for _ in range(n):
        print_row(n)

def print_row(n):
    print("#"*n)

main()