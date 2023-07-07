def main():
    yell("This" ,"is","CS50")

def yell(*words):
    temp = [word.upper()for word in words]
    print(*temp)

if __name__ == "__main__":
    main()