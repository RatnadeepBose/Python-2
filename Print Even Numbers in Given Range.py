# Print Even Numbers from 1 to 10
i = 1
while i <= 10:
    if i % 2 == 0:  # Check if number is divisible by 2
        print(i)
    i += 1

# Output: 2, 4, 6, 8, 10

# Print Odd Numbers from 1 to 10
i = 10
while i >= 1:
    if i % 2 != 0:  # Check if number is NOT divisible by 2
        print(i)
    i -= 1

# Output: 9, 7, 5, 3, 1