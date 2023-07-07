class Account:
    def __init__(self):
        self._balance = 0;
    
    @property
    def balance(self):
        return self._balance;

    @balance.setter 
    def balance(self,balance):
        self._balance = balance
    
    def __str__(self):
        return f"{self._balance}"
    
    def withdraw(self,n):
        self._balance += n
    
    def deposite(self,n):
        self._balance -= n
    
def main():
    account = Account()
    print(f"the account {account}")
    account.withdraw(100) 
    print(f"the account {account}")
    account.deposite(30)
    print(f"the account {account}")

if __name__ == "__main__":
    main()
        
