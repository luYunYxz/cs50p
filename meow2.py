
def meow(n: int) -> str:
    return "meow\n" * n

n : int = int(input("input the meow's num : "));
meows:str = meow(n)

print(meows,end="")