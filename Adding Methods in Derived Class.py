

# ============================================
# ADDING ATTRIBUTES IN DERIVED CLASS
# ============================================

# PARENT CLASS
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# CHILD CLASS - adds new attributes
class Student(Human):
    def __init__(self, name, age, student_id, grade):
        # Call parent constructor to set name and age
        super().__init__(name, age)
        
        # NEW ATTRIBUTES (only Student has)
        self.student_id = student_id
        self.grade = grade
    
    def show_student(self):
        print(f"Student: {self.name}, ID: {self.student_id}, Grade: {self.grade}")

# Create objects
h = Human("Rahul", 30)
s = Student("Priya", 20, "S123", "A")

# Access parent attributes
print(h.name)        # Rahul
print(s.name)        # Priya (inherited)
print(s.age)         # 20 (inherited)

# Access child-specific attributes
print(s.student_id)  # S123 (new)
print(s.grade)       # A (new)

# Call methods
h.display()          # Name: Rahul, Age: 30
s.display()          # Name: Priya, Age: 20 (inherited)
s.show_student()     # Student: Priya, ID: S123, Grade: A