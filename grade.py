per = float(input("Enter your percentage: "))

if per< 25:
    print("Grade: D")
elif per < 45:
    print("Grade: C")
elif per < 65:
    print("Grade: B")
elif per < 85:
    print("Grade: A")
else:
    print("Grade: A+")