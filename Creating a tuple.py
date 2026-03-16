# Different ways to create tuples
t = ()                     # Empty tuple
t2 = ()                    # Another empty tuple  
t3 = (2,)                  # Single element (COMMA needed!)
t4 = tuple("ram")          # From string → ('r','a','m')

# Check types
print(type(t))   # <class 'tuple'>
print(type(t2))  # <class 'tuple'>
print(type(t3))  # <class 'tuple'>
print(type(t4))  # <class 'tuple'>

# Print values
print(t)         # ()
print(t2)        # ()
print(t4)        # ('r', 'a', 'm')

# Tuple with a list inside
t = (1, 2, ["ram", "rahul", "raj"], 3, 4)

print(t)
print(type(t))  # <class 'tuple'>
print(t[2])     # ['ram', 'rahul', 'raj']
print(t[2][0])  # 'ram' (access list element)

# You can modify the list inside tuple
t[2].append("rohan")
print(t)  # List changed, but tuple still tuple