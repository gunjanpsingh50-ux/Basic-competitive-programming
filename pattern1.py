#Grid pattern
rows = int(input("Enter the value of N: "))
column= int(input("Enter the value of M: "))
for i in range(0,rows):
    for j in range(0,column):
        print("*", end="")
    print()  