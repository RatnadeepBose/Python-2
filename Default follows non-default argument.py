#Default follows non-default argument


# ✅ Multiple defaults at the end
def student(name, age=18, city="Delhi"):
    print(f"{name} is {age} years old from {city}")

student("Ram")              # Ram is 18 years old from Delhi
student("Ram", 20)          # Ram is 20 years old from Delhi
student("Ram", 20, "Mumbai") # Ram is 20 years old from Mumbai

# ✅ Mix of both
def calculate(a, b, operation="add"):
    if operation == "add":
        return a + b
    elif operation == "mul":
        return a * b
    else:
        return "Unknown operation"

print(calculate(5, 3))        # 8 (add)
print(calculate(5, 3, "mul")) # 15

# ✅ Multiple parameters with defaults
def greet(name, greeting="Hello", punctuation="!"):
    print(f"{greeting} {name}{punctuation}")

greet("Ram")                 # Hello Ram!
greet("Ram", "Hi")           # Hi Ram!
greet("Ram", "Hey", "?")     # Hey Ram?

