# ============================================
# LIST OPERATIONS - Minimal & Complete
# ============================================

budget = [100, 200, 450, 500, 100]

# COUNT - How many times 100 appears
print(budget.count(100))  # 2

# INDEX - First position of 100 (0-based)
print(budget.index(100))  # 0

# ============================================
# POP() - Remove & Return Elements
# ============================================

name = ["Harry", "emma", "romnnie"]

# pop() - removes LAST item
removed = name.pop()
print(removed)        # romnnie
print(name)           # ['Harry', 'emma']

# pop(0) - removes FIRST item
removed = name.pop(0)
print(removed)        # Harry
print(name)           # ['emma']



