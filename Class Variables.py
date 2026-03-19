# ============================================
# CLASS VARIABLES
# ============================================

class Human:
    population = 0  # Shared by all
    data = []       # Shared list

    def __init__(self, name):
        self.name = name  # Unique to each
        Human.population += 1
        Human.data.append(name)

# Create objects
h1 = Human("Rahul")
h2 = Human("Emma")
h3 = Human("Priya")

# Check class variables (same for all)
print(Human.population)  # 3
print(Human.data)        # ['Rahul', 'Emma', 'Priya']

# Check instance variables (unique to each)
print(h1.name)  # Rahul
print(h2.name)  # Emma
print(h3.name)  # Priya