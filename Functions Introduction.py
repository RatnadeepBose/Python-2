# ============================================
# FUNCTIONS - Reusable blocks of code
# ============================================

# 1️⃣ SIMPLE FUNCTION (No parameters)
def greet():
    print("Hello! Welcome to Python.")

# Call the function
greet()  # Hello! Welcome to Python.
greet()  # Can call multiple times!

# 2️⃣ FUNCTION WITH PARAMETERS
def greet_person(name):
    print(f"Hello {name}! Welcome.")

greet_person("Rahul")  # Hello Rahul! Welcome.
greet_person("Rajesh") # Hello Rajesh! Welcome.

# 3️⃣ FUNCTION WITH RETURN VALUE
def add(a, b):
    result = a + b
    return result

sum = add(5, 3)
print(sum)  # 8

# 4️⃣ FUNCTION WITH DEFAULT PARAMETER
def power(base, exponent=2):
    return base ** exponent

print(power(5))      # 25 (5²)
print(power(5, 3))   # 125 (5³)

# 5️⃣ MULTIPLE RETURN VALUES
def get_min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([4, 7, 2, 9, 1])
print(f"Min: {minimum}, Max: {maximum}")  # Min: 1, Max: 9