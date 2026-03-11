# INPUT FUNCTION
name = input("Enter name: ")
print("Hello " + name)
print(name)
print(type(name))  # <class 'str'>

# Type conversion
a = float(input("Enter number: "))
print(a, type(a))  # 5.0 <class 'float'>

b = int(a)
print(b, type(b))  # 5 <class 'int'>