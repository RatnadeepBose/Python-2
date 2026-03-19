# ============================================
# ADDING ATTRIBUTES IN DERIVED CLASS
# ============================================

# PARENT CLASS
class Human:
    def __init__(self, name, age):
        print("Human __init__")
        self.name = name
        self.age = age
    
    def intro(self):
        print(f"{self.name} ({self.age})")

# CHILD CLASS - adds new attributes
class Student(Human):
    def __init__(self, name, age, student_id, grade):
        print("Student __init__ start")
        
        # super() calls parent constructor
        # This sets name and age attributes
        super().__init__(name, age)
        
        print("Student __init__ resume")
        
        # NEW ATTRIBUTES (only Student has)
        self.student_id = student_id
        self.grade = grade
    
    def student_info(self):
        print(f"{self.name} | ID: {self.student_id} | Grade: {self.grade}")

# Create objects
print("Creating Human:")
h = Human("Rahul", 30)

print("\nCreating Student:")
s = Student("Priya", 20, "S123", "10th")

print("\nAccess:")
print(f"h.name: {h.name}")           # Rahul
print(f"s.name: {s.name}")            # Priya
print(f"s.student_id: {s.student_id}") # S123

print("\nMethods:")
h.intro()        # Rahul (30)
s.intro()        # Priya (20)
s.student_info() # Priya | ID: S123 | Grade: 10th