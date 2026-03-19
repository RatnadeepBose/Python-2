# ============================================
# CLASS CONSTRUCTOR (__init__ method)
# ============================================

class Human:
    def __init__(self, name, age, hobby):
        print("✨ Creating a new Human...")
        self.name = name
        self.age = age
        self.hobby = hobby
    
    def intro(self):
        print(f"👤 {self.name} | Age: {self.age} | Hobby: {self.hobby}")

# Create objects
rahul = Human("Rahul", 25, "cricket")
emma = Human("Emma", 22, "dancing")
priya = Human("Priya", 24, "reading")

print("\n" + "="*50)
print("📊 OBJECTS CREATED:")
print("="*50)

print(f"\n🔹 rahul: {rahul}")
print(f"   Type: {type(rahul)}")
rahul.intro()

print(f"\n🔹 emma: {emma}")
print(f"   Type: {type(emma)}")
emma.intro()

print(f"\n🔹 priya: {priya}")
print(f"   Type: {type(priya)}")
priya.intro()

print("\n" + "="*50)
print("✅ All objects created successfully!")
print("="*50)