#List Comprehension


# Simple loop
for i in range(10):
    print(i, end=" ")  # 0 1 2 3 4 5 6 7 8 9

# Building with append
l = []
for i in range(10):
    l.append(i)
print(l)  # [0,1,2,3,4,5,6,7,8,9]

# List comprehension (clean way)
l = [i for i in range(20)]
print(l)  # [0-19]

# Squares
squares = [i**2 for i in range(10)]
print(squares)  # [0,1,4,9,16,25,36,49,64,81]

