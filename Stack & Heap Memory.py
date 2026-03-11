# STACK vs HEAP MEMORY

# Stack: Primitive types (int, float, bool)
x = 10  # Stored in stack
y = x   # Copy by value

# Heap: Objects (list, dict, custom objects)
list1 = [1, 2, 3]  # Stored in heap, reference in stack
list2 = list1      # Copy by reference

list2[0] = 99
print(list1[0])  # 99 (changed because same object)

print(id(list1))  # Same memory address
print(id(list2))  # Same memory address