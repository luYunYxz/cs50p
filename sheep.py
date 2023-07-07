
count = int(input("what is the num? "))

def sheep(n):
    sheeps = []
    for _ in range(n):
        sheeps.append("🐑")
    yield sheeps

for i in range(count):
    print(*(sheep(i)))

