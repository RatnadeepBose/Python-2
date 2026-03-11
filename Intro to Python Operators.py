# ============================================
# PYTHON OPERATORS - COMPLETE REFERENCE
# ============================================

# 1. ARITHMETIC OPERATORS
print("\n--- ARITHMETIC OPERATORS ---")
a, b = 10, 3
print(f"{a} + {b} = {a + b}")        # Addition: 13
print(f"{a} - {b} = {a - b}")        # Subtraction: 7
print(f"{a} * {b} = {a * b}")        # Multiplication: 30
print(f"{a} / {b} = {a / b}")        # Division: 3.333...
print(f"{a} // {b} = {a // b}")      # Floor Division: 3
print(f"{a} % {b} = {a % b}")        # Modulus (remainder): 1
print(f"{a} ** {b} = {a ** b}")      # Exponentiation: 1000

# 2. COMPARISON OPERATORS (return Boolean)
print("\n--- COMPARISON OPERATORS ---")
x, y = 5, 8
print(f"{x} == {y}: {x == y}")       # Equal to: False
print(f"{x} != {y}: {x != y}")       # Not equal: True
print(f"{x} > {y}: {x > y}")         # Greater than: False
print(f"{x} < {y}: {x < y}")         # Less than: True
print(f"{x} >= {y}: {x >= y}")       # Greater/equal: False
print(f"{x} <= {y}: {x <= y}")       # Less/equal: True

# 3. LOGICAL OPERATORS
print("\n--- LOGICAL OPERATORS ---")
p, q = True, False
print(f"{p} and {q}: {p and q}")     # AND: False
print(f"{p} or {q}: {p or q}")       # OR: True
print(f"not {p}: {not p}")           # NOT: False

# 4. ASSIGNMENT OPERATORS
print("\n--- ASSIGNMENT OPERATORS ---")
c = 5
print(f"c = {c}")                     # Assignment: 5
c += 3  # c = c + 3
print(f"c += 3 → {c}")                # 8
c -= 2  # c = c - 2
print(f"c -= 2 → {c}")                # 6
c *= 4  # c = c * 4
print(f"c *= 4 → {c}")                # 24
c /= 3  # c = c / 3
print(f"c /= 3 → {c}")                # 8.0
c //= 2 # c = c // 2
print(f"c //= 2 → {c}")               # 4.0
c %= 3  # c = c % 3
print(f"c %= 3 → {c}")                # 1.0
c **= 2 # c = c ** 2
print(f"c **= 2 → {c}")               # 1.0

# 5. IDENTITY OPERATORS
print("\n--- IDENTITY OPERATORS ---")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print(f"list1 is list2: {list1 is list2}")     # False (different objects)
print(f"list1 is list3: {list1 is list3}")     # True (same object)
print(f"list1 is not list2: {list1 is not list2}")  # True

# 6. MEMBERSHIP OPERATORS
print("\n--- MEMBERSHIP OPERATORS ---")
fruits = ["apple", "banana", "cherry"]
print(f"'apple' in fruits: {'apple' in fruits}")        # True
print(f"'mango' in fruits: {'mango' in fruits}")        # False
print(f"'mango' not in fruits: {'mango' not in fruits}")  # True

# 7. BITWISE OPERATORS
print("\n--- BITWISE OPERATORS ---")
m, n = 5, 3  # Binary: 5=101, 3=011
print(f"{m} & {n} = {m & n}")        # AND: 1 (001)
print(f"{m} | {n} = {m | n}")        # OR: 7 (111)
print(f"{m} ^ {n} = {m ^ n}")        # XOR: 6 (110)
print(f"~{m} = {~m}")                 # NOT: -6
print(f"{m} << 1 = {m << 1}")         # Left shift: 10 (1010)
print(f"{m} >> 1 = {m >> 1}")         # Right shift: 2 (10)

# 8. OPERATOR PRECEDENCE (PEMDAS)
print("\n--- OPERATOR PRECEDENCE ---")
result = 10 + 5 * 2  # Multiplication first: 10 + 10 = 20
print(f"10 + 5 * 2 = {result}")
result = (10 + 5) * 2  # Parentheses first: 15 * 2 = 30
print(f"(10 + 5) * 2 = {result}")

# 9. TERNARY OPERATOR (conditional expression)
print("\n--- TERNARY OPERATOR ---")
age = 18
status = "Adult" if age >= 18 else "Minor"
print(f"Age {age}: {status}")  # Adult

# 10. STRING OPERATORS
print("\n--- STRING OPERATORS ---")
print(f"'Hello' + 'World' = {'Hello' + 'World'}")  # Concatenation: HelloWorld
print(f"'Hi' * 3 = {'Hi' * 3}")                    # Repetition: HiHiHi

# ============================================
# QUICK REFERENCE TABLE
# ============================================
print("\n" + "="*40)
print("OPERATOR QUICK REFERENCE")
print("="*40)
print("""
┌──────────────┬─────────────┬────────────────┐
│ Category     │ Operators   │ Example        │
├──────────────┼─────────────┼────────────────┤
│ Arithmetic   │ + - * / %   │ 10 + 5 = 15    │
│              │ // **       │ 10 // 3 = 3    │
├──────────────┼─────────────┼────────────────┤
│ Comparison   │ == != > <   │ 5 > 3 = True   │
│              │ >= <=       │ 5 <= 3 = False │
├──────────────┼─────────────┼────────────────┤
│ Logical      │ and or not  │ True and False │
├──────────────┼─────────────┼────────────────┤
│ Assignment   │ = += -= *=  │ x += 5         │
│              │ /= //= %=   │ x *= 2         │
├──────────────┼─────────────┼────────────────┤
│ Identity     │ is is not   │ x is y         │
├──────────────┼─────────────┼────────────────┤
│ Membership   │ in not in   │ 'a' in list    │
├──────────────┼─────────────┼────────────────┤
│ Bitwise      │ & | ^ ~     │ 5 & 3 = 1      │
│              │ << >>       │ 5 << 1 = 10    │
└──────────────┴─────────────┴────────────────┘
""")