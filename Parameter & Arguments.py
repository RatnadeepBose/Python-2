#Parameter & Arguments


# ============================================
# FUNCTION WITH PARAMETER
# ============================================

def greet(name):
    # body
    print("good morning", name)

# Call the function with a value
greet("Rahul")        # good morning Rahul
greet("Rajesh")       # good morning Rajesh
greet("Priya")        # good morning Priya

# ❌ Wrong way - using variable name that doesn't exist
# greet(name)  # NameError: name 'name' is not defined






def add(a, b):  # Don't forget the colon!
    c = a + b
    print("a =", a)
    print("b =", b)
    print("Sum =", c)

# Call with two arguments
add(2, 3)  # ✅ Correct way