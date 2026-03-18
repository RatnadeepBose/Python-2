# ============================================
# RETURN STATEMENT - Getting values back
# ============================================

# Example 1: Return numeric value
def add(a, b):
    c = a + b
    print("a =", a)
    print("b =", b)
    print("Sum =", c)
    return c

b = add(3, 4)
print("Returned value:", b, "Type:", type(b))  # 7 <class 'int'>

print("\n" + "="*40)

# Example 2: Return stops function execution
def func():
    print("before return")
    return "rahul"      # Function stops here
    print("after return")  # ❌ This NEVER runs!

func()  # Prints: before return
a = func()  # Prints: before return
print("Returned value:", a)  # rahul