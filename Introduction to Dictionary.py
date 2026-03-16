#Introduction to Dictionary



# Creating dictionaries
empty_dict = {}                    # Empty dictionary
student = {"name": "Rahul", "age": 25, "city": "Jalpaiguri"}

print(type(empty_dict))  # <class 'dict'>
print(student)           # {'name': 'Rahul', 'age': 25, 'city': 'Jalpaiguri'}

# Accessing values
print(student["name"])   # Rahul
print(student["age"])    # 25
print(student.get("city"))  # Jalpaiguri (safer way)

# Adding/Updating
student["email"] = "rahul@email.com"
student["age"] = 26
print(student)  # {'name': 'Rahul', 'age': 26, 'city': 'Jalpaiguri', 'email': 'rahul@email.com'}

# Dictionary methods
print(student.keys())    # dict_keys(['name', 'age', 'city', 'email'])
print(student.values())  # dict_values(['Rahul', 26, 'Jalpaiguri', 'rahul@email.com'])
print(student.items())   # dict_items([('name','Rahul'), ('age',26), ...])

# Iteration
for key, value in student.items():
    print(f"{key}: {value}")