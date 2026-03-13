# Print Sum of Numbers in given Range

i = 1
add = 0
while i <= 10:
    add += i
    print(i)      # Print current number
    i += 1        # Increment i (MUST be inside loop)

print("The sum of numbers from 1 to 10 is:", add)



# Sum of even numbers from 1 to 10
i = 1
total = 0

while i <= 10:
    if i % 2 == 0:  # Check if number is even
        total = total + i
    i = i + 1

print("Sum of even numbers:", total)  # 30




# Sum of odd numbers from 1 to 10
i = 1
total = 0

while i <= 10:
    if i % 2 != 0:  # Check if number is odd
        total = total + i
    i = i + 1

print("Sum of odd numbers:", total)  # 25