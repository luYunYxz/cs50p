balance = 0

def main():
    print(f"the balance = {balance}")
    withdraw(100)
    deposit(50)
    print(f"the balance = {balance}")


def withdraw(n):
    global balance
    balance +=n

def deposit(n):
    global balance
    balance -= n

if __name__ == "__main__":
    main()

    