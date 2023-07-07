def main():
    yell("This" ,"is","CS50")

def yell(*words):
    temp = []
    for word in words:
        temp.append(word.upper())
    print(temp)

if __name__ == "__main__":
    main()