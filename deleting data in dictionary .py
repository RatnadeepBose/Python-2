# ============================================
# DELETING DATA IN DICTIONARY
# ============================================

fruits = {"Apple": 120, "mango": 100, "pineapple": 50}
print("Original:", fruits)

# Check if key exists
print("Apple" in fruits)    # True
print("hajmola" in fruits)   # False

# Method 1: pop(key) - removes specific key and returns value
removed = fruits.pop("Apple")
print(f"Removed Apple with value: {removed}")
print("After pop('Apple'):", fruits)

# Method 2: popitem() - removes last inserted item (Python 3.7+)
removed_item = fruits.popitem()
print(f"Removed last item: {removed_item}")
print("After popitem():", fruits)

# Method 3: del - deletes entire dictionary
del fruits
# print(fruits)  # ❌ This would cause NameError - fruits no longer exists!