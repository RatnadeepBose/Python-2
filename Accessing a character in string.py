# ============================================
# ACCESSING CHARACTERS IN A STRING
# ============================================

name = "Rahul"
print("=" * 40)
print(f"String: '{name}'")
print("=" * 40)

# POSITIVE INDEXING (Left to Right: 0 to 4)
print("\n✅ POSITIVE INDEXING:")
print(f"name[0] → '{name[0]}'  # First character")
print(f"name[1] → '{name[1]}'  # Second character")
print(f"name[2] → '{name[2]}'  # Third character")
print(f"name[3] → '{name[3]}'  # Fourth character")
print(f"name[4] → '{name[4]}'  # Fifth character")

# STRING LENGTH
print("\n📏 STRING LENGTH:")
print(f"len(name) → {len(name)}  # Total characters")

# NEGATIVE INDEXING (Right to Left: -1 to -5)
print("\n✅ NEGATIVE INDEXING:")
print(f"name[-1] → '{name[-1]}'  # Last character")
print(f"name[-2] → '{name[-2]}'  # Second last")
print(f"name[-3] → '{name[-3]}'  # Third last")
print(f"name[-4] → '{name[-4]}'  # Fourth last")
print(f"name[-5] → '{name[-5]}'  # Fifth last (first)")

print("\n" + "=" * 40)
print("📊 VISUAL INDEX MAP")
print("=" * 40)
print("\nString:  R     a     h     u     l")
print("Index:   0     1     2     3     4")
print("        -5    -4    -3    -2    -1")
print("=" * 40)