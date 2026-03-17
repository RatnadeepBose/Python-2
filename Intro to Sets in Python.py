# ============================================
# INTRO TO SETS IN PYTHON
# ============================================

# List vs Set
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]  # List allows duplicates
print("List:", lst)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]

# ❌ Wrong way to create empty set (creates dict)
s = {}
print(type(s))  # <class 'dict'> (not set!)

# ✅ Correct way to create empty set
a = set()
print(type(a))  # <class 'set'>
print("Empty set:", a)  # set()

# ✅ Non-empty set (duplicates automatically removed)
b = {5, 9, 7, 52, 9, 4, 6, 89, 5}
print(type(b))  # <class 'set'>
print("Set (no duplicates):", b)  # {4, 5, 6, 7, 9, 52, 89} (order may vary)

# ✅ Iteration
print("\nIterating through set:")
for i in b:
    print(i, end=" ")  # 4 5 6 7 9 52 89