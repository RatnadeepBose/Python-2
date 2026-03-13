# ============================================
# PRINTING MULTIPLE VALUES
# ============================================

# Basic printing with multiple values (default separator = space)
print("Hello", "World", "Welcome", "to", "Python", 25, 36, 877.56)
# Output: Hello World Welcome to Python 25 36 877.56

# Custom separator and end
print("Rahul", 26, sep=" ", end=" ")
# Output: Rahul 26 (with space at end, no newline)

# Changing separator to newline (each value on new line)
print("Hello", "World", "Welcome", "to", "Python", 25, 36, 877.56, sep="\n")
# Output: 
# Hello
# World
# Welcome
# to
# Python
# 25
# 36
# 877.56

# Custom separator with arrow
print("Rahul", 26, sep="->", end=" ")
# Output: Rahul->26 (with space at end)

# ============================================
# MORE PRINT EXAMPLES
# ============================================

print("\n" + "="*40)
print("ADDITIONAL EXAMPLES")
print("="*40)

# Different separators
print("apple", "banana", "orange", sep=", ")        # apple, banana, orange
print("2024", "03", "13", sep="-")                  # 2024-03-13
print("name", "age", "city", sep=" | ")             # name | age | city

# Combining sep and end
print("Loading", end="")
print(".", end="")
print(".", end="")
print(".")                                           # Loading....

# Practical example
first = "John"
last = "Doe"
age = 25
print(first, last, "- Age:", age, sep=" ")           # John Doe - Age: 25