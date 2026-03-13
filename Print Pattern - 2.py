#Print Pattern - 2


# Print Pattern - Right Triangle
n= int(input("Enter the number of rows for the right triangle pattern: "))
for i in range(1, n+1 ):
    for j in range(i):
        print("#", end="")
    print()  # Move to next line after each row