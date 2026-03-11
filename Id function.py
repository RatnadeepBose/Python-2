# ID FUNCTION - Shows memory address
x = 5
print(id(x))  # 140734982674568

y = 45
print(id(y))  # 140734982676488

name = "Rahul"
print(id(name))  # 2175052675952

# Same value = same ID (for small ints)
a = 10
b = 10
print(id(a) == id(b))  # True