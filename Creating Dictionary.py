# ============================================
# CREATING DICTIONARIES
# ============================================

# Empty dictionary
d = {}
print(type(d))  # <class 'dict'>
print(d)        # {}

# Non-empty dictionary (Method 1: Direct)
fruits = {
    "Apple": 120,
    "mango": 60,
    "orange": 20
}
print(type(fruits))  # <class 'dict'>
print(fruits)        # {'Apple': 120, 'mango': 60, 'orange': 20}

# Non-empty dictionary (Method 2: Using zip)
name = ["Apple", "pineapple", "grape", "orange"]
prices = [100, 200, 300, 60]

fruit = dict(zip(name, prices))
print(fruit)  # {'Apple': 100, 'pineapple': 200, 'grape': 300, 'orange': 60}