def main():
    x = int(input("what is x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")
        
def is_even(x):
    return True if x % 2 == 0 else False

main()