# ============================================
# OOP CONCEPTS - DEFINITIONS WITH EXAMPLES
# ============================================

# 1️⃣ CLASS
# Definition: A blueprint or template for creating objects
# Example: Student admission form (blank form)

class Student:
    """🏗️ CLASS - Blueprint for students"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def study(self):
        print(f"{self.name} is studying")

print("1️⃣ CLASS = Blueprint")
print("   Example: Student class is like a blank form")
print()

# 2️⃣ OBJECT
# Definition: An instance of a class (actual thing created from blueprint)
# Example: Filled admission form with actual data

s1 = Student("Rahul", 20)   # 🏠 OBJECT 1
s2 = Student("Priya", 22)   # 🏠 OBJECT 2

print("2️⃣ OBJECT = Instance of class")
print(f"   s1 object: {s1.name}, {s1.age} years old")
print(f"   s2 object: {s2.name}, {s2.age} years old")
print()

# 3️⃣ INHERITANCE
# Definition: Child class gets all properties and methods from parent class
# Example: Child inherits features from parents

class Person:
    """👨 PARENT CLASS"""
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating")

class Student(Person):  # 👦 CHILD CLASS inherits from Person
    """Student inherits from Person"""
    def __init__(self, name, roll_no):
        super().__init__(name)  # Calling parent's constructor
        self.roll_no = roll_no
    
    def study(self):
        print(f"{self.name} (Roll: {self.roll_no}) is studying")

print("3️⃣ INHERITANCE = Child gets parent's features")
s = Student("Rahul", 101)
s.eat()   # ✅ From parent (Person)
s.study() # ✅ From child (Student)
print()

# 4️⃣ POLYMORPHISM
# Definition: Same method name works differently for different classes
# Example: "sound()" method - Dog barks, Cat meows

class Dog:
    def sound(self):
        return "🐕 Woof! Woof!"

class Cat:
    def sound(self):
        return "🐈 Meow! Meow!"

class Cow:
    def sound(self):
        return "🐄 Moo! Moo!"

def make_sound(animal):  # Same function works for any animal
    print(animal.sound())

print("4️⃣ POLYMORPHISM = Same method, different behavior")
make_sound(Dog())
make_sound(Cat())
make_sound(Cow())
print()

# 5️⃣ ENCAPSULATION
# Definition: Hiding internal data and providing controlled access
# Example: ATM machine - you can't directly access money, only through proper methods

class BankAccount:
    """💰 ENCAPSULATION - Data hiding"""
    def __init__(self, balance):
        self.__balance = balance  # __ means PRIVATE (hidden)
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount}")
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ₹{amount}")
        else:
            print("Insufficient balance!")
    
    def check_balance(self):
        return f"Balance: ₹{self.__balance}"

print("5️⃣ ENCAPSULATION = Data hiding with controlled access")
acc = BankAccount(5000)
# print(acc.__balance)  # ❌ ERROR! Can't access directly
acc.deposit(2000)
acc.withdraw(1000)
print(acc.check_balance())  # ✅ Controlled access
print()

# 6️⃣ ABSTRACTION
# Definition: Hiding complex implementation details, showing only necessary features
# Example: Car - you just press accelerator, don't need to know how engine works

class Car:
    """🚗 ABSTRACTION - Hide complexity"""
    def start(self):
        self.__check_engine()
        self.__check_fuel()
        self.__check_battery()
        print("🏁 Car started! Ready to drive")
    
    # Hidden methods (complexity hidden from user)
    def __check_engine(self):
        print("   🔧 Engine check... OK")
    
    def __check_fuel(self):
        print("   ⛽ Fuel check... OK")
    
    def __check_battery(self):
        print("   🔋 Battery check... OK")

print("6️⃣ ABSTRACTION = Hide complexity, show only what's needed")
my_car = Car()
my_car.start()  # User just sees start, all complexity hidden
print()