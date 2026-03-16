#Tuple unpacking

# Basic variable assignment
a, b, c = 4, 3, 8
print(a, b, c)  # 4 3 8

# Tuple unpacking
t = (9, 8, 7, 6)
z, x, y, w = t  # Unpack tuple into variables

print(t[0])     # 9 (direct index)
print(z, x, y, w)  # 9 8 7 6 (unpacked)