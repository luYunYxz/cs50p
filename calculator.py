def main():
    x = float(input("waht is x?"))
    sqr = square(x)
    print("the square = : ",sqr)

def square( x):
    return pow(x ,2)


main()