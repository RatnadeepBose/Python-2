# Operator Level Polymorphism


# ============================================
# OPERATOR LEVEL POLYMORPHISM
# Same operator works differently for different types
# ============================================

# 1️⃣ + OPERATOR - Different behavior with different types
print("🔹 + OPERATOR")
print(5 + 3)           # 8 (integer addition)
print(5.5 + 3.2)       # 8.7 (float addition)
print("Hello" + "World")  # HelloWorld (string concatenation)
print([1,2] + [3,4])   # [1,2,3,4] (list concatenation)

# 2️⃣ * OPERATOR
print("\n🔹 * OPERATOR")
print(5 * 3)           # 15 (integer multiplication)
print(5.5 * 3)         # 16.5 (float multiplication)
print("Hi" * 3)        # HiHiHi (string repetition)
print([1,2] * 3)       # [1,2,1,2,1,2] (list repetition)

# 3️⃣ len() FUNCTION - Polymorphism with different types
print("\n🔹 len() FUNCTION")
print(len("Hello"))    # 5 (string length)
print(len([1,2,3,4]))  # 4 (list length)
print(len((1,2,3)))    # 3 (tuple length)
print(len({"a":1, "b":2}))  # 2 (dictionary length)

# 4️⃣ CUSTOM CLASS WITH OPERATOR OVERLOADING
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # Define how + works for Point objects
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    # Define how * works for Point objects
    def __mul__(self, scalar):
        return Point(self.x * scalar, self.y * scalar)
    
    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(2, 3)
p2 = Point(4, 5)

print("\n🔹 CUSTOM + OPERATOR")
p3 = p1 + p2
print(f"{p1} + {p2} = {p3}")  # (2,3) + (4,5) = (6,8)

print("\n🔹 CUSTOM * OPERATOR")
p4 = p1 * 3
print(f"{p1} * 3 = {p4}")     # (2,3) * 3 = (6,9)