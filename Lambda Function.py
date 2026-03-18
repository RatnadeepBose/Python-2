# ============================================
# LAMBDA FUNCTIONS - Complete Guide
# ============================================

print("=" * 50)
print("1️⃣ REGULAR FUNCTION vs LAMBDA")
print("=" * 50)

# Regular function
def add(a, b):
    return a + b

print("Regular function:")
print(add(3, 3))        

# Lambda function
print("\nLambda function:")
print((lambda a, b: a + b)(9, 3))  

# Lambda stored in variable
func = lambda z, x: z + x
print(func(9, 4))       

print("\n" + "=" * 50)
print("2️⃣ LAMBDA WITH CONDITIONALS")
print("=" * 50)

# Regular function for comparison
def larger(u, i):
    if u > i:
        return u
    else:
        return i

print("Regular function:")
print(larger(10, 5))    # 10
print(larger(3, 8))     # 8
print(larger(7, 7))     # 7

# Lambda with ternary operator
print("\nLambda with ternary:")
print((lambda p, o: p if p > o else o)(78, 69))  # 78
print((lambda p, o: p if p > o else o)(45, 99))  # 99
print((lambda p, o: p if p > o else o)(50, 50))  # 50

print("\n" + "=" * 50)
print("3️⃣ SORTING WITH LAMBDA")
print("=" * 50)

lst = [(12, 58), (2, 5), (1, 8), (3, 5)]
print(f"Original list: {lst}")

# ❌ Common mistake - print(lst.sort()) returns None
print("\n❌ Wrong: print(lst.sort()) →", lst.sort())  # None

# ✅ Correct - sort() modifies in-place
lst.sort()
print(f"✅ After default sort: {lst}")  # [(1, 8), (2, 5), (3, 5), (12, 58)]

# Reset list
lst = [(12, 58), (2, 5), (1, 8), (3, 5)]

# Sort by second element using named function
def k(x):
    return x[1]

lst.sort(key=k)
print(f"✅ Using named function (key=k): {lst}")  # [(2, 5), (3, 5), (1, 8), (12, 58)]

# Reset list
lst = [(12, 58), (2, 5), (1, 8), (3, 5)]

# Sort by second element using lambda (BEST!)
lst.sort(key=lambda x: x[1])
print(f"✅ Using lambda: {lst}")  # [(2, 5), (3, 5), (1, 8), (12, 58)]

# Using sorted() - returns new list
lst = [(12, 58), (2, 5), (1, 8), (3, 5)]
new_lst = sorted(lst, key=lambda x: x[1])
print(f"✅ Using sorted(): {new_lst}")  # [(2, 5), (3, 5), (1, 8), (12, 58)]
print(f"   Original unchanged: {lst}")

print("\n" + "=" * 50)
print("4️⃣ MORE LAMBDA EXAMPLES")
print("=" * 50)

# Map with lambda
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(f"Map (squares): {squares}")  # [1, 4, 9, 16, 25]

# Filter with lambda
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Filter (evens): {evens}")  # [2, 4]

# Multiple operations
operations = [
    ("Add", lambda x, y: x + y),
    ("Subtract", lambda x, y: x - y),
    ("Multiply", lambda x, y: x * y),
    ("Divide", lambda x, y: x / y)
]

a, b = 10, 5
for name, op in operations:
    print(f"{name}: {op(a, b)}")