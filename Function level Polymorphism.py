#Function level Polymorphism

# ============================================
# FUNCTION LEVEL POLYMORPHISM
# Same function name, different behaviors
# ============================================

# 1️⃣ BUILT-IN len() FUNCTION - Works with different types
print("🔹 len() POLYMORPHISM")
print(len("Hello"))        # 5 (string)
print(len([1,2,3,4]))      # 4 (list)
print(len((1,2,3)))        # 3 (tuple)
print(len({"a":1,"b":2}))  # 2 (dict)
print(len(range(10)))      # 10 (range)

# 2️⃣ SAME FUNCTION NAME IN DIFFERENT CLASSES
class Dog:
    def sound(self):
        return "Woof!"
    
    def move(self):
        return "Running on four legs"

class Cat:
    def sound(self):
        return "Meow!"
    
    def move(self):
        return "Walking silently"

class Bird:
    def sound(self):
        return "Chirp!"
    
    def move(self):
        return "Flying in sky"

# Polymorphic function - works with any animal
def animal_actions(animal):
    print(f"Sound: {animal.sound()}")
    print(f"Move: {animal.move()}")

print("\n🔹 DOG:")
animal_actions(Dog())

print("\n🔹 CAT:")
animal_actions(Cat())

print("\n🔹 BIRD:")
animal_actions(Bird())

# 3️⃣ SAME FUNCTION NAME WITH DIFFERENT PARAMETERS
class Calculator:
    # Method overloading (simulated in Python)
    def add(self, a, b=None, c=None):
        if c is not None:
            return a + b + c
        elif b is not None:
            return a + b
        else:
            return a

print("\n🔹 CALCULATOR POLYMORPHISM:")
calc = Calculator()
print(f"add(5): {calc.add(5)}")              # 5
print(f"add(5,3): {calc.add(5,3)}")          # 8
print(f"add(5,3,2): {calc.add(5,3,2)}")      # 10

# 4️⃣ DUCK TYPING - "If it walks like a duck and quacks like a duck..."
class Duck:
    def quack(self):
        return "Quack!"

class Person:
    def quack(self):
        return "I'm imitating a duck!"

def make_it_quack(thing):
    print(thing.quack())  # Doesn't care about type, just needs quack() method

print("\n🔹 DUCK TYPING:")
make_it_quack(Duck())     # Quack!
make_it_quack(Person())   # I'm imitating a duck!

# 5️⃣ REAL-WORLD EXAMPLE - Shape area calculation
class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h
    
    def area(self):
        return self.w * self.h

class Circle:
    def __init__(self, r):
        self.r = r
    
    def area(self):
        return 3.14 * self.r * self.r

class Triangle:
    def __init__(self, b, h):
        self.b = b
        self.h = h
    
    def area(self):
        return 0.5 * self.b * self.h

# Polymorphic function
def print_area(shape):
    print(f"Area: {shape.area()}")

print("\n🔹 SHAPE AREA POLYMORPHISM:")
print_area(Rectangle(5, 4))    # Area: 20
print_area(Circle(3))           # Area: 28.26
print_area(Triangle(6, 4))      # Area: 12.0