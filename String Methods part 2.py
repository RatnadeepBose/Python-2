# ============================================
# STRING METHODS - Case Checking & Conversion
# ============================================

# Sample strings
name = "rahul"           # All lowercase
jhame = "MULLA"          # All uppercase
shame = "Rahul Mulla"    # Mixed case + space

print("=" * 50)
print("📝 ORIGINAL STRINGS")
print("=" * 50)
print(f"name  → '{name}'   (all lowercase)")
print(f"jhame → '{jhame}'   (all uppercase)")
print(f"shame → '{shame}' (mixed case with space)")

# ============================================
# 1️⃣ CASE CONVERSION
# ============================================
print("\n" + "=" * 50)
print("🔄 CASE CONVERSION")
print("=" * 50)

print(f"name.upper()  → '{name.upper()}'    # Convert to uppercase")
print(f"jhame.lower() → '{jhame.lower()}'    # Convert to lowercase")
print(f"shame.title() → '{shame.title()}'  # First letter of each word uppercase")

# ============================================
# 2️⃣ CASE CHECKING
# ============================================
print("\n" + "=" * 50)
print("✅ CASE CHECKING")
print("=" * 50)

# Check if uppercase
print("\n🔹 isupper() - Checks if ALL characters are uppercase")
print("-" * 45)
print(f"name.isupper()  → {name.isupper()}   # '{name}' is all lowercase?")
print(f"jhame.isupper() → {jhame.isupper()}   # '{jhame}' is all uppercase?")
print(f"shame.isupper() → {shame.isupper()}   # '{shame}' is all uppercase?")

# Check if lowercase
print("\n🔸 islower() - Checks if ALL characters are lowercase")
print("-" * 45)
print(f"name.islower()  → {name.islower()}   # '{name}' is all lowercase?")
print(f"jhame.islower() → {jhame.islower()}   # '{jhame}' is all lowercase?")
print(f"shame.islower() → {shame.islower()}   # '{shame}' is all lowercase?")

# ============================================
# 3️⃣ CHARACTER TYPE CHECKING
# ============================================
print("\n" + "=" * 50)
print("📊 CHARACTER TYPE CHECKING")
print("=" * 50)

print("\n🔹 isalpha() - Checks if ALL characters are letters (A-Z, a-z)")
print("-" * 50)
print(f"name.isalpha()  → {name.isalpha()}   # '{name}' - only letters?")
print(f"jhame.isalpha() → {jhame.isalpha()}   # '{jhame}' - only letters?")
print(f"shame.isalpha() → {shame.isalpha()}   # '{shame}' - only letters? (space is not a letter)")

# ============================================
# 4️⃣ ADDITIONAL USEFUL METHODS
# ============================================
print("\n" + "=" * 50)
print("🎯 ADDITIONAL STRING METHODS")
print("=" * 50)

test = "   Hello World   "
print(f"\nOriginal: '{test}'")
print(f"strip()   : '{test.strip()}'    # Removes spaces from both ends")
print(f"startswith('H'): {test.strip().startswith('H')}  # Check if starts with 'H'")
print(f"endswith('d'): {test.strip().endswith('d')}      # Check if ends with 'd'")

# ============================================
# 5️⃣ QUICK REFERENCE TABLE
# ============================================
print("\n" + "=" * 50)
print("📋 QUICK REFERENCE")
print("=" * 50)

print("""
┌──────────────┬──────────────────────────────┬─────────────┐
│ Method       │ What it does                  │ Example    │
├──────────────┼──────────────────────────────┼─────────────┤
│ upper()      │ Converts to UPPERCASE         │ 'rahul'→'RAHUL' │
│ lower()      │ Converts to lowercase         │ 'MULLA'→'mulla' │
│ title()      │ First letter of each word cap │ 'rahul mulla'→'Rahul Mulla' │
│ isupper()    │ Checks if ALL are uppercase   │ 'ABC'→True, 'Abc'→False │
│ islower()    │ Checks if ALL are lowercase   │ 'abc'→True, 'Abc'→False │
│ isalpha()    │ Checks if ALL are letters     │ 'abc'→True, 'abc123'→False │
│ strip()      │ Removes spaces from ends      │ ' hello '→'hello' │
└──────────────┴──────────────────────────────┴─────────────┘
""")

print("=" * 50)
print("✨ END OF STRING METHODS DEMO ✨")
print("=" * 50)