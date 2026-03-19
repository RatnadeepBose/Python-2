# ============================================
# CLASS & OBJECT IN PYTHON
# ============================================

# 🏗️ Define a class (blueprint)
class Car:
    pass  # Empty class for now

# 🏠 Create objects (instances of the class)
honda = Car()
toyota = Car()
bmw = Car()

# Check types
print(f"Type of honda: {type(honda)}")    # <class '__main__.Car'>
print(f"Type of toyota: {type(toyota)}")  # <class '__main__.Car'>
print(f"Type of bmw: {type(bmw)}")        # <class '__main__.Car'>

# Check if they're different objects
print(f"\nAre they different objects?")
print(f"honda is toyota: {honda is toyota}")  # False (different objects)