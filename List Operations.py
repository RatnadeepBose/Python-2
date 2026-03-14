# ============================================
# LIST OPERATIONS - Including insert()
# ============================================

budget = [100, 200, 450, 500, 100]

# COUNT & INDEX
print(budget.count(100))  # 2
print(budget.index(100))  # 0

# ============================================
# INSERT() - Add at specific position
# ============================================

name = ["Harry", "emma", "romnnie"]
print(f"Original: {name}")  # ['Harry', 'emma', 'romnnie']

# insert(index, value)
name.insert(1, "John")  # Insert "John" at index 1
print(f"After insert: {name}")  # ['Harry', 'John', 'emma', 'romnnie']

name.insert(0, "Zara")  # Insert at beginning
print(f"At start: {name}")  # ['Zara', 'Harry', 'John', 'emma', 'romnnie']

name.insert(len(name), "Last")  # Insert at end (like append)
print(f"At end: {name}")  # ['Zara', 'Harry', 'John', 'emma', 'romnnie', 'Last']

# ============================================
# POP() - Remove & Return
# ============================================

name = ["Harry", "emma", "romnnie"]  # Reset list

removed = name.pop()
print(f"pop() → {removed}, list: {name}")  # romnnie, ['Harry', 'emma']

removed = name.pop(0)
print(f"pop(0) → {removed}, list: {name}")  # Harry, ['emma']