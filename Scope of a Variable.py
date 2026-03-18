# ============================================
# SCOPE OF VARIABLES
# ============================================

# 1️⃣ GLOBAL VARIABLE - accessible everywhere
a = 5

def func():
    print(a)  # Can access global variable

func()        # 5
print(a)      # 5

print("\n" + "="*40)

# 2️⃣ LOCAL VARIABLE - only inside function
b = 3

def yo():
    x = 5    # Local variable (only inside yo())
    print(x)  # 5

yo()          # 5
# print(x)    # ❌ ERROR! x is not defined outside

print("\n" + "="*40)

# 3️⃣ LOCAL vs GLOBAL - same name, different scope
o = 3        # Global o

def yoo():
    o = 69   # Local o (different from global)
    print("Inside function:", o)  # 69

yoo()         # 69
print("Outside function:", o)      # 3 (global unchanged)

print("\n" + "="*40)

# 4️⃣ GLOBAL KEYWORD - modify global variable
l = 420      # Global l

def suu():
    global l   # Use the global variable, not create local
    l = 25     # Modifies global l
    print("Inside function:", l)  # 25

print("Before:", l)  # 420
suu()               # 25
print("After:", l)   # 25 (global changed!)