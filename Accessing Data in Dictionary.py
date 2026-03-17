# ============================================
# ACCESSING DATA IN DICTIONARY
# ============================================

fruits = {
    "Apple": 120,
    "mango": 100,
    "pineapple": 50
}

# Print entire dictionary
print(fruits)  # {'Apple': 120, 'mango': 100, 'pineapple': 50}

# Method 1: Square brackets []
print(fruits["Apple"])      # 120

# Method 2: get() - returns None if key missing
print(fruits.get("Apple"))  # 120

# Method 3: get() with default value
print(fruits.get("Apple", "Not Available"))   # 120
print(fruits.get("grapes", "Not Available"))  # Not Available