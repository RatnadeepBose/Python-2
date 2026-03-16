# Tuple with mixed types
t = ([1,2,3,4,5,6], "Rahul")

print(f"Tuple: {t}")
print(f"Type of t: {type(t)}")        # <class 'tuple'>
print(f"Type of t[0]: {type(t[0])}")  # <class 'list'> (mutable)
print(f"Type of t[1]: {type(t[1])}")  # <class 'str'> (immutable)

# CAN modify the list inside tuple (list is mutable)
t[0].append(7)
t[0][0] = 99
print(f"\nAfter modifying list: {t}")  # List changed

# CANNOT modify tuple itself
# t[1] = "Raj"  # ❌ Error! Tuple doesn't support item assignment

# CANNOT reassign tuple elements
# t[0] = [9,8,7]  # ❌ Error!