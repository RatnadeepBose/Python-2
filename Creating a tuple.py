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