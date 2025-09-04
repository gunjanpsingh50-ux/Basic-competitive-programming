n = int(input("Enter the value of N: "))
for i in range(n, 0, -1):
    print("*", end="")
    for j in range(1, i):
        print("_", end="")
    print("*")
    print()