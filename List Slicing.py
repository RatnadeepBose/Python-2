# ============================================
# LIST SLICING - [start:end:step]
# ============================================

l = [2, 3, 5, 7, 8, 5, 9, 7, 8, 9, 6, 5, 4, 1, 2, 3]
print("=" * 50)
print(f"📝 Original list: {l}")
print(f"📏 Length: {len(l)} elements")
print("=" * 50)

# BASIC SLICING [start:end] (end is exclusive)
print("\n🔹 BASIC SLICING")
print("-" * 35)
print(f"l[0:3]   → {l[0:3]}    # Index 0 to 2 (first 3 elements)")
print(f"l[3:7]   → {l[3:7]}    # Index 3 to 6")
print(f"l[:5]    → {l[:5]}     # Start to index 4")
print(f"l[10:]   → {l[10:]}    # Index 10 to end")

# SLICING WITH STEP
print("\n🔸 SLICING WITH STEP")
print("-" * 35)
print(f"l[::2]   → {l[::2]}     # Every 2nd element")
print(f"l[1::2]  → {l[1::2]}     # Every 2nd from index 1")

# REVERSE SLICING
print("\n🔹 REVERSE SLICING")
print("-" * 35)
print(f"l[5:0:-1] → {l[5:0:-1]}   # Index 5 down to 1 (excluding 0)")
print(f"l[5::-1]  → {l[5::-1]}    # Index 5 down to start")
print(f"l[::-1]   → {l[::-1]}     # Complete reverse")

# VISUAL GUIDE
print("\n" + "=" * 50)
print("📊 INDEX MAP")
print("=" * 50)
print("\nIndex:  0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15")
print("Value:  2   3   5   7   8   5   9   7   8   9   6   5   4   1   2   3")
print("-" * 65)
print(f"l[0:3]   → indices 0,1,2      → [2,3,5]")
print(f"l[5:0:-1]→ indices 5,4,3,2,1  → [5,8,7,5,3]")