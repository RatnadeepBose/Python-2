# ============================================
# ERRORS & EXCEPTIONS - MINIMALIST
# ============================================

print("1. SYNTAX ERROR")
print("   Missing parenthesis: print('Hello'")

print("\n2. NAME ERROR")
try:
    print("x")
except NameError:
    print("   Variable not defined")

print("\n3. TYPE ERROR")
try:
    print("5" + 3)
except TypeError:
    print("   String + int not allowed")

print("\n4. VALUE ERROR")
try:
    print(int("abc"))
except ValueError:
    print("   Cannot convert to int")

print("\n5. INDEX ERROR")
try:
    print([1,2,3][5])
except IndexError:
    print("   Index out of range")

print("\n6. KEY ERROR")
try:
    print({"name":"Rahul"}["age"])
except KeyError:
    print("   Key not found")

print("\n7. ZERO DIVISION")
try:
    print(10/0)
except ZeroDivisionError:
    print("   Cannot divide by zero")

print("\n8. FILE ERROR")
try:
    open("missing.txt")
except FileNotFoundError:
    print("   File not found")