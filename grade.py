score = int(input("Score: "))

if score >= 90 and score <= 100:
    print("Grade: a")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score <80:
    print("Grade: C")
elif score >= 60 and score < 70:
    print("Grand: D")
else:
    print("Grade: F")
