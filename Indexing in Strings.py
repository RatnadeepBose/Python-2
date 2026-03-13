# ============================================
# STRING INDEXING - Accessing Characters
# ============================================

name = "Rahul"
print("=" * 40)
print(f"📝 String: '{name}'")
print(f"📏 Length: {len(name)} characters")
print("=" * 40)

# Positive Indexing (Left to Right: 0 to n-1)
print("\n🔹 POSITIVE INDEXING [0 to 4]")
print("-" * 30)
print(f"name[0] → '{name[0]}'  # First character")
print(f"name[1] → '{name[1]}'  # Second character")
print(f"name[2] → '{name[2]}'  # Third character")
print(f"name[3] → '{name[3]}'  # Fourth character")
print(f"name[4] → '{name[4]}'  # Fifth character")

# Negative Indexing (Right to Left: -1 to -n)
print("\n🔸 NEGATIVE INDEXING [-1 to -5]")
print("-" * 30)
print(f"name[-1] → '{name[-1]}'  # Last character")
print(f"name[-2] → '{name[-2]}'  # Second last")
print(f"name[-3] → '{name[-3]}'  # Third last")
print(f"name[-4] → '{name[-4]}'  # Fourth last")
print(f"name[-5] → '{name[-5]}'  # Fifth last (first)")

print("\n" + "=" * 40)
print("📊 INDEX MAPPING")
print("=" * 40)

# Visual representation
print("\nString:  R     a     h     u     l")
print("Index:   0     1     2     3     4")
print("        -5    -4    -3    -2    -1")

print("\n" + "=" * 40)
print("🎯 ACCESSING EACH CHARACTER")
print("=" * 40)

# Loop through with positive indices
print("\n👉 Using positive indices:")
for i in range(len(name)):
    print(f"name[{i}] = '{name[i]}'")

# Loop through with negative indices
print("\n👉 Using negative indices:")
for i in range(-1, -len(name)-1, -1):
    print(f"name[{i}] = '{name[i]}'")