# UPDATING DICTIONARY

fruits = {"Apple": 120, "mango": 100, "pineapple": 50}

# Update existing
fruits["pineapple"] = {'small': 90, 'large': 120}
print(fruits)  # {'Apple': 120, 'mango': 100, 'pineapple': {'small': 90, 'large': 120}}

# Add new
fruits["Guava"] = 80
print(fruits)  # + 'Guava': 80

# Update multiple
fruits.update({"Grapes": 20, "kiwi": 20, "berry": 20})
print(fruits)  # + all new items