t = (9, 8, 7, 6)

# Basic operations
print(type(t))        # <class 'tuple'>
print(t)              # (9, 8, 7, 6)
print(t.count(1))     # 0
print(t.count(9))     # 1
print(t.index(7))     # 2
print(len(t))         # 4
print(t.index(8))     # 1

# Iteration
for i in t:
    print(i)          # 9 8 7 6

# Concatenation
t1 = (1, 2, 3, 4)
t3 = t + t1
print(t3)             # (9, 8, 7, 6, 1, 2, 3, 4)

# Tuple ↔ List conversion
lst = list(t)
print(type(lst))      # <class 'list'>
t = tuple(lst)
print(type(t))        # <class 'tuple'>