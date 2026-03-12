# ============================================
# 1. MEMBERSHIP OPERATOR: 'in'
# ============================================

# String membership
name = "Rahul"
print("R" in name)    # True - 'R' exists in "Rahul"
print("z" in name)    # False - 'z' not in "Rahul"
print("ah" in name)   # True - substring exists

# List membership
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)   # True
print("mango" in fruits)   # False

# Tuple membership
numbers = (1, 2, 3, 4, 5)
print(3 in numbers)    # True
print(10 in numbers)   # False

# Dictionary membership (checks keys)
student = {"name": "Rahul", "age": 25, "city": "Jalpaiguri"}
print("name" in student)     # True - key exists
print("Rahul" in student)    # False - checks keys, not values
print("age" in student)      # True

# 'not in' operator (opposite)
print("z" not in name)       # True - 'z' is NOT in name
print("mango" not in fruits) # True - mango NOT in fruits

# ============================================
# 2. IDENTITY OPERATOR: 'is'
# ============================================

# Integer caching (small integers -5 to 256 share memory)
a = 5
b = 5
print(f"a: {a}, id: {id(a)}")
print(f"b: {b}, id: {id(b)}")
print(a is b)  # True - same object (Python caches small ints)

# Large integers (may be different objects)
c = 1000
d = 1000
print(f"\nc: {c}, id: {id(c)}")
print(f"d: {d}, id: {id(d)}")
print(c is d)  # False - different objects (may vary by Python implementation)

# Strings (string interning)
s1 = "hello"
s2 = "hello"
print(f"\ns1: {s1}, id: {id(s1)}")
print(f"s2: {s2}, id: {id(s2)}")
print(s1 is s2)  # True - same object (string interning)

# Lists (always different objects)
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1  # Reference to same object

print(f"\nlist1 id: {id(list1)}")
print(f"list2 id: {id(list2)}")
print(f"list3 id: {id(list3)}")

print(list1 is list2)  # False - different lists with same values
print(list1 is list3)  # True - same object (reference copy)
print(list1 == list2)  # True - same values

# 'is not' operator
print(list1 is not list2)  # True - they are different objects

# ============================================
# PRACTICAL EXAMPLES
# ============================================

print("\n--- PRACTICAL EXAMPLES ---")

# Check if character is vowel
char = "a"
vowels = "aeiou"
print(f"Is '{char}' a vowel? {char in vowels}")  # True

# Validate user input
allowed_users = ["admin", "rahul", "john"]
username = "rahul"
print(f"Access granted? {username in allowed_users}")  # True

# Check for None (always use 'is' for None)
value = None
print(value is None)     # True (correct way)
print(value == None)     # True (works but not recommended)

# Check object type
x = 5
print(type(x) is int)    # True

# Check empty list
my_list = []
print(my_list is [])     # False (different objects)
print(len(my_list) == 0) # True (better way to check empty)