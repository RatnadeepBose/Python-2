# ============================================
# STRING CONCATENATION - Joining Strings
# ============================================

first = "Rahul"
last = "Mulla"

print("=" * 40)
print("📝 ORIGINAL STRINGS")
print("=" * 40)
print(f"First name: '{first}'")
print(f"Last name:  '{last}'")

# ============================================
# 1️⃣ BASIC CONCATENATION (+)
# ============================================
print("\n" + "=" * 40)
print("🔹 BASIC CONCATENATION")
print("=" * 40)

# Joining with space
full_name = first + " " + last
print(f"first + ' ' + last → '{full_name}'  # Rahul Mulla")

# Joining without space
print(f"first + last       → '{first + last}'      # RahulMulla")

# Joining with different separators
print(f"first + '-' + last → '{first + '-' + last}'  # Rahul-Mulla")
print(f"first + '@' + last → '{first + '@' + last}'  # Rahul@Mulla")

# ============================================
# 2️⃣ NUMBERS vs STRINGS
# ============================================
print("\n" + "=" * 40)
print("🔸 NUMBERS vs STRINGS")
print("=" * 40)

print(f"2 + 2       → {2 + 2}        # Integer addition (math)")
print(f"'2' + '2'   → {'2' + '2'}        # String concatenation")
print(f"'2' + str(2) → {'2' + str(2)}      # Mixing types (need str())")

# ============================================
# 3️⃣ STRING REPETITION (*)
# ============================================
print("\n" + "=" * 40)
print("🔹 STRING REPETITION")
print("=" * 40)

letter = "a"
print(f"'a' * 3  → '{letter * 3}'     # 'aaa'")
print(f"'Hi' * 4 → '{'Hi' * 4}' # 'HiHiHiHi'")
print(f"'-' * 20 → '{'-' * 20}'")

# ============================================
# 4️⃣ MULTIPLE STRINGS
# ============================================
print("\n" + "=" * 40)
print("🔸 JOINING MULTIPLE STRINGS")
print("=" * 40)

print(f"'a' + 'b' + 'c' → '{'a' + 'b' + 'c'}'  # abc")
print(f"'Hello' + ' ' + 'World' → '{'Hello' + ' ' + 'World'}'")

# Using join() method (alternative)
words = ["Python", "is", "awesome"]
print(f"' '.join(words) → '{' '.join(words)}'")

# ============================================
# 5️⃣ PRACTICAL EXAMPLES
# ============================================
print("\n" + "=" * 40)
print("🎯 PRACTICAL EXAMPLES")
print("=" * 40)

# Email address
username = "rahul.mulla"
domain = "@gmail.com"
email = username + domain
print(f"Email: {email}")

# Greeting message
greeting = "Hello"
name = "Rahul"
message = greeting + ", " + name + "!"
print(f"Message: {message}")

# Path building
folder = "users"
subfolder = "docs"
file = "resume.pdf"
path = "/" + folder + "/" + subfolder + "/" + file
print(f"Path: {path}")

# ============================================
# 6️⃣ QUICK REFERENCE TABLE
# ============================================
print("\n" + "=" * 40)
print("📋 CONCATENATION RULES")
print("=" * 40)

print("""
┌──────────────────┬────────────────────────────────┐
│ Operation        │ Result                         │
├──────────────────┼────────────────────────────────┤
│ "Rahul" + " " + "Mulla" → "Rahul Mulla" (with space) │
│ "Rahul" + "Mulla"        → "RahulMulla" (no space)    │
│ "2" + "2"                → "22" (string join)         │
│ 2 + 2                    → 4 (number addition)        │
│ "a" * 3                  → "aaa" (repetition)         │
└──────────────────┴────────────────────────────────┘
""")

print("=" * 40)
print("✨ END OF CONCATENATION DEMO ✨")
print("=" * 40)