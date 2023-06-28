
def main():
    x = get_int("what is x? ")
    print(f"the x = {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
main()