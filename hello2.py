
def main():
   name = input("What is you name?")
   out = hello(name)
   print(out)

def hello(to = "world"):
    return f"hello, {to}"


if __name__ == "__main__":
    main()
