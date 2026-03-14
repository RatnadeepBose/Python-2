# ============================================
# INTRODUCTION TO LISTS IN PYTHON
# ============================================

# Creating lists
l = list()                    # Empty list using list() constructor
print(type(l))                 # <class 'list'>

l1 = [1, 2, 3, 4]             # List with elements using square brackets
print(type(l1))                # <class 'list'>

# Basic list operations
print("\n📊 LIST PROPERTIES")
print("=" * 25)
print(f"List l1: {l1}")
print(f"Length of list: {len(l1)}")        # Number of elements
print(f"Memory address: {id(l1)}")         # Unique ID in memory

# Iterating through a list
print("\n🔄 ITERATING THROUGH LIST")
print("=" * 25)
for i in l1:
    print(f"Element: {i}")