# ============================================
# SET OPERATIONS - add, update, remove, pop
# ============================================

s = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print("Original:", s)

# add() - adds single element
s.add(69420)
print("After add(69420):", s)

# update() - adds multiple elements
name = "rajesh"
s.update(name)
print(f"After update('{name}'):", s)

# remove() - removes specific element (error if missing)
s.remove(5)
print("After remove(5):", s)

# pop() - removes and returns ARBITRARY element (no index!)
removed = s.pop()
print(f"After pop() - removed: {removed}")
print(f"Remaining set: {s}")

# pop() again (removes another random element)
removed2 = s.pop()
print(f"After second pop() - removed: {removed2}")
print(f"Final set: {s}")