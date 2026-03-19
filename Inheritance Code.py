#Inheritance Code

# 🟦 PARENT CLASS (Base class)
class Human:
    population = 0
    alive_count = 0

    def __init__(self, name, age, alive=True):
        self.name = name
        self.age = age
        self.alive = alive
        Human.population += 1
        if alive:
            Human.alive_count += 1
        print(f"  👤 HUMAN created: {self.name}, Age: {self.age}")
    
    def kill(self):
        if self.alive:
            self.alive = False
            Human.alive_count -= 1
            print(f"  💀 {self.name} died")
    
    def revive(self):
        if not self.alive:
            self.alive = True
            Human.alive_count += 1
            print(f"  ✨ {self.name} revived")
    
    def status(self):
        status_text = "ALIVE" if self.alive else "DEAD"
        print(f"  👤 {self.name} ({self.age}) | Status: {status_text}")
    
    def work(self):
        print(f"  💼 {self.name} is working")
    
    @classmethod
    def summary(cls):
        print("\n" + "="*50)
        print("📊 HUMAN POPULATION SUMMARY")
        print("="*50)
        print(f"  Total humans: {cls.population}")
        print(f"  Alive: {cls.alive_count}")
        print(f"  Dead: {cls.population - cls.alive_count}")
        print("="*50)


# 🟩 CHILD CLASS 1: Student (inherits from Human)
class Student(Human):
    student_count = 0
    
    def __init__(self, name, age, student_id, grade, alive=True):
        # Call parent constructor FIRST
        super().__init__(name, age, alive)
        
        # Add new attributes specific to Student
        self.student_id = student_id
        self.grade = grade
        self.university = "Unknown"
        Student.student_count += 1
        
        print(f"  🎓 STUDENT created: {self.name}, ID: {self.student_id}, Grade: {self.grade}")
    
    # New method (only Student has this)
    def study(self, subject):
        print(f"  📚 {self.name} (ID: {self.student_id}) is studying {subject}")
    
    # New method
    def attend_class(self):
        print(f"  🏫 {self.name} is attending class")
    
    # Override parent's work() method (POLYMORPHISM)
    def work(self):
        print(f"  📝 {self.name} is doing homework")
    
    # Override status to show more info
    def status(self):
        base_status = "ALIVE" if self.alive else "DEAD"
        print(f"  🎓 STUDENT: {self.name} | ID: {self.student_id} | Grade: {self.grade} | Status: {base_status}")


# 🟨 CHILD CLASS 2: Teacher (inherits from Human)
class Teacher(Human):
    teacher_count = 0
    
    def __init__(self, name, age, employee_id, subject, salary, alive=True):
        # Call parent constructor
        super().__init__(name, age, alive)
        
        # Teacher-specific attributes
        self.employee_id = employee_id
        self.subject = subject
        self.salary = salary
        Teacher.teacher_count += 1
        
        print(f"  👨‍🏫 TEACHER created: {self.name}, Subject: {self.subject}")
    
    # New method
    def teach(self):
        print(f"  📖 {self.name} is teaching {self.subject}")
    
    # New method
    def grade_students(self):
        print(f"  ✏️ {self.name} is grading papers")
    
    # Override work() method
    def work(self):
        print(f"  📋 {self.name} is preparing lessons")
    
    # Override status
    def status(self):
        base_status = "ALIVE" if self.alive else "DEAD"
        print(f"  👨‍🏫 TEACHER: {self.name} | Subject: {self.subject} | Salary: ${self.salary} | Status: {base_status}")


# 🟪 CHILD CLASS 3: Athlete (inherits from Human)
class Athlete(Human):
    athlete_count = 0
    
    def __init__(self, name, age, sport, team, achievements=[], alive=True):
        super().__init__(name, age, alive)
        
        self.sport = sport
        self.team = team
        self.achievements = achievements
        Athlete.athlete_count += 1
        
        print(f"  🏃 ATHLETE created: {self.name}, Sport: {self.sport}, Team: {self.team}")
    
    def train(self):
        print(f"  🏋️ {self.name} is training for {self.sport}")
    
    def compete(self):
        print(f"  🏆 {self.name} is competing in {self.sport}")
    
    def add_achievement(self, achievement):
        self.achievements.append(achievement)
        print(f"  🥇 {self.name} got new achievement: {achievement}")
    
    def show_achievements(self):
        print(f"  🏅 {self.name}'s achievements: {', '.join(self.achievements) if self.achievements else 'None'}")
    
    def work(self):
        print(f"  💪 {self.name} is practicing {self.sport}")
    
    def status(self):
        base_status = "ALIVE" if self.alive else "DEAD"
        print(f"  🏃 ATHLETE: {self.name} | Sport: {self.sport} | Team: {self.team} | Status: {base_status}")


# ============================================
# DEMONSTRATION - USING ALL CLASSES
# ============================================

print("\n🔹 CREATING DIFFERENT HUMANS")
print("="*60)

# Create a regular Human
h1 = Human("Rahul", 35)

# Create Students
s1 = Student("Priya", 20, "S12345", "10th Grade")
s2 = Student("Amit", 22, "S67890", "12th Grade", alive=False)  # Created dead

# Create Teachers
t1 = Teacher("Sharma Sir", 45, "T001", "Mathematics", 50000)
t2 = Teacher("Patel Ma'am", 38, "T002", "Science", 55000)

# Create Athletes
a1 = Athlete("Virat", 32, "Cricket", "Indian Team", ["World Cup Winner"])
a2 = Athlete("Mary", 28, "Badminton", "National Team")

print("\n" + "="*60)
print("🔹 DEMONSTRATING INHERITANCE - COMMON METHODS")
print("="*60)

# All can use Human methods (inherited)
print("\n📌 STATUS OF ALL:")
h1.status()
s1.status()
t1.status()
a1.status()

print("\n📌 KILL AND REVIVE:")
s2.status()           # Amit is dead
s2.revive()           # Revive Amit
s2.status()           # Now alive

print("\n📌 WORK METHODS (Polymorphism - same method, different behavior):")
h1.work()    # Human working
s1.work()    # Student doing homework
t1.work()    # Teacher preparing lessons
a1.work()    # Athlete practicing

print("\n" + "="*60)
print("🔹 DEMONSTRATING CHILD-SPECIFIC METHODS")
print("="*60)

# Student-specific
print("\n📌 STUDENT ACTIVITIES:")
s1.study("Mathematics")
s1.attend_class()

# Teacher-specific
print("\n📌 TEACHER ACTIVITIES:")
t1.teach()
t1.grade_students()

# Athlete-specific
print("\n📌 ATHLETE ACTIVITIES:")
a1.train()
a1.compete()
a2.add_achievement("Olympic Silver Medal")
a2.show_achievements()

print("\n" + "="*60)
print("🔹 CLASS VARIABLES - TRACKING COUNTS")
print("="*60)

print(f"  Human.population: {Human.population}")        # Total humans
print(f"  Student.student_count: {Student.student_count}")  # Total students
print(f"  Teacher.teacher_count: {Teacher.teacher_count}")  # Total teachers
print(f"  Athlete.athlete_count: {Athlete.athlete_count}")  # Total athletes

print(f"\n  Alive count: {Human.alive_count}")
print(f"  Dead count: {Human.population - Human.alive_count}")

print("\n" + "="*60)
print("🔹 FINAL SUMMARY")
print("="*60)

# Show all statuses
print("\n📌 ALL INDIVIDUALS:")
for person in [h1, s1, s2, t1, t2, a1, a2]:
    person.status()

# Global summary