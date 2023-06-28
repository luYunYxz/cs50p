
def main():
    x = get_int()
    print(f"the x = {x}")


def get_int():
    while True:
        try:
            return int(input("what is the x ? "))
        except ValueError:
            print("the value is not integer")

main()