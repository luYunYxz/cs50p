class Cat:
    MEOW = 2
    def meow(self):
        for _ in range(Cat.MEOW):
            print("meow")

def main():
    cat = Cat()
    cat.meow()

if __name__ == "__main__":
    main()