def main():
    yell("This" ,"is","CS50")

def yell(*words):
    temp = map(str.upper,words) 
    print(*temp)

if __name__ == "__main__":
    main()