#Print Multiplication table
n = int(input("Enter a number to print its multiplication table: "))
print("Multiplication Table of", n)
for i in range(1, 11):
    print(n, "x", i, "=", n * i)