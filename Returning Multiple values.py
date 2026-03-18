# ============================================
# RETURNING MULTIPLE VALUES
# ============================================

def intro(name, age, hobby):
    return name, age, hobby  # Returns as a tuple

# Method 1: Unpack into separate variables
c, d, e = intro("Rahul", 25, "Travelling")
print(c, d, e)  # Rahul 25 Travelling

# Method 2: Catch as a single tuple
result = intro("Rajesh", 30, "Reading")
print(result)           # ('Rajesh', 30, 'Reading')
print(type(result))     # <class 'tuple'>
print(result[0])        # Rajesh (access by index)