#Adding more methods in Class

# ============================================
# HUMAN CLASS WITH ALIVE/DEAD TRACKING
# LINE-BY-LINE EXPLANATION
# ============================================

# Step 0: Define the class (blueprint)
class Human:
    # CLASS VARIABLES - These belong to the class itself, not to any single object
    # They start at 0 and will be shared by ALL humans
    
    population = 0      # Tracks TOTAL humans ever created (alive or dead)
    alive_count = 0     # Tracks ONLY humans currently alive

    # CONSTRUCTOR METHOD - Runs automatically when we create a new human
    # Parameters: self (the new object), name, alive (True by default)
    def __init__(self, name, alive=True):
        # INSTANCE VARIABLES - These belong to THIS SPECIFIC human object
        self.name = name        # Store this human's name
        self.alive = alive      # Store whether this human is alive
        
        # Update CLASS VARIABLES (shared by all)
        # Human.population means we're accessing the class variable
        Human.population += 1   # Increase total count by 1
        
        # If this human is created alive, increase alive count
        if alive:               # Same as: if alive == True
            Human.alive_count += 1  # Increase alive count by 1
        
        # Optional: Print confirmation
        print(f"  ✓ Created: {self.name} (Alive: {self.alive})")
    
    # METHOD: Kill a human
    def kill(self):
        # Check if this human is currently alive
        if self.alive:           # if self.alive == True
            self.alive = False    # Change status to dead
            Human.alive_count -= 1  # Decrease global alive count by 1
            print(f"  💀 {self.name} died")
        else:
            # Human is already dead
            print(f"  ❌ {self.name} is already dead")
    
    # METHOD: Revive a human
    def revive(self):
        # Check if this human is currently dead
        if not self.alive:        # if self.alive == False
            self.alive = True      # Change status to alive
            Human.alive_count += 1  # Increase global alive count by 1
            print(f"  ✨ {self.name} revived")
        else:
            # Human is already alive
            print(f"  ✅ {self.name} is already alive")
    
    # METHOD: Show current status of this human
    def status(self):
        # Using ternary operator: value_if_true if condition else value_if_false
        status_text = "ALIVE" if self.alive else "DEAD"
        print(f"  👤 {self.name}: {status_text}")
    
    # CLASS METHOD - Belongs to the class, shows summary of ALL humans
    @classmethod
    def summary(cls):
        print("\n" + "="*40)
        print("📊 GLOBAL SUMMARY")
        print("="*40)
        print(f"  Total humans ever created: {cls.population}")
        print(f"  Currently alive: {cls.alive_count}")
        print(f"  Currently dead: {cls.population - cls.alive_count}")
        print("="*40)


# ============================================
# NOW LET'S RUN THE CODE STEP BY STEP
# ============================================

print("\n🔹 STEP 1: Creating humans")
print("-" * 40)

# Line 1: Create Rahul (alive by default)
# What happens:
#   - __init__ method runs
#   - self.name = "Rahul"
#   - self.alive = True
#   - Human.population goes from 0 → 1
#   - Human.alive_count goes from 0 → 1
h1 = Human("Rahul")  

# Line 2: Create Emma (alive by default)
# What happens:
#   - self.name = "Emma"
#   - self.alive = True
#   - Human.population goes from 1 → 2
#   - Human.alive_count goes from 1 → 2
h2 = Human("Emma")

# Line 3: Create Priya (specifically dead)
# What happens:
#   - self.name = "Priya"
#   - self.alive = False (because we passed False)
#   - Human.population goes from 2 → 3
#   - Human.alive_count stays at 2 (because alive=False)
h3 = Human("Priya", False)

# Show summary after creation
Human.summary()


print("\n🔹 STEP 2: Checking initial status")
print("-" * 40)

# Check each human's status
h1.status()  # Should show Rahul: ALIVE
h2.status()  # Should show Emma: ALIVE
h3.status()  # Should show Priya: DEAD


print("\n🔹 STEP 3: Killing Emma")
print("-" * 40)

# Before killing, note alive_count = 2
print(f"  Before kill - Alive count: {Human.alive_count}")

# Kill Emma
# What happens inside kill():
#   - Checks if h2.alive is True ✓
#   - Sets h2.alive = False
#   - Human.alive_count decreases from 2 → 1
#   - Prints "Emma died"
h2.kill()

# After killing, alive_count should be 1
print(f"  After kill - Alive count: {Human.alive_count}")

# Check Emma's status now
h2.status()  # Should show Emma: DEAD


print("\n🔹 STEP 4: Reviving Priya")
print("-" * 40)

# Before revive, alive_count = 1
print(f"  Before revive - Alive count: {Human.alive_count}")

# Revive Priya
# What happens inside revive():
#   - Checks if h3.alive is False ✓
#   - Sets h3.alive = True
#   - Human.alive_count increases from 1 → 2
#   - Prints "Priya revived"
h3.revive()

# After revive, alive_count should be 2
print(f"  After revive - Alive count: {Human.alive_count}")

# Check Priya's status now
h3.status()  # Should show Priya: ALIVE


print("\n🔹 STEP 5: Trying to kill someone twice")
print("-" * 40)

# Kill Emma again (she's already dead)
# What happens:
#   - Checks if h2.alive is False
#   - Skips the kill block
#   - Goes to else and prints "already dead"
h2.kill()  # Second kill attempt - should say already dead

# Revive Rahul (he's already alive)
# What happens:
#   - Checks if h1.alive is True
#   - Skips the revive block
#   - Goes to else and prints "already alive"
h1.revive()  # Revive alive person - should say already alive


print("\n🔹 STEP 6: Final Status")
print("-" * 40)

# Check all final statuses
h1.status()  # Rahul: ALIVE
h2.status()  # Emma: DEAD
h3.status()  # Priya: ALIVE

# Final summary
Human.summary()


print("\n🔹 STEP 7: Understanding Class vs Instance variables")
print("-" * 40)

# Class variables can be accessed through the class OR any instance
print(f"  Via class:    Human.population = {Human.population}")
print(f"  Via h1:       h1.population     = {h1.population}")
print(f"  Via h2:       h2.population     = {h2.population}")
print(f"  Via h3:       h3.population     = {h3.population}")
print(f"  They all show the SAME value: {Human.population}")

# Instance variables are unique to each object
print(f"\n  Instance variables (unique):")
print(f"  h1.name = {h1.name}")  # Rahul
print(f"  h2.name = {h2.name}")  # Emma
print(f"  h3.name = {h3.name}")  # Priya
print(f"  h1.alive = {h1.alive}")  # True
print(f"  h2.alive = {h2.alive}")  # False
print(f"  h3.alive = {h3.alive}")  # True