# ============================================
# APPEND vs EXTEND in LISTS
# ============================================

# Original list
l = [1, 2, 3, 4, 5, 6, 7]
print(f"Original l: {l}")

# ============================================
# APPEND() - Adds as SINGLE element
# ============================================
l.append("rajesh")
print(f"\n✅ After append('rajesh'): {l}")
# [1, 2, 3, 4, 5, 6, 7, 'rajesh']
# "rajesh" added as ONE element (string)

# ============================================
# EXTEND() - Adds MULTIPLE elements
# ============================================
l1 = [1, 2, 3, 4, 5, 6, 7]
l1.extend(l)
print(f"\n✅ After extend(l): {l1}")
# [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 'rajesh']
# Each element of l added separately

# ============================================
# EXTEND with STRING
# ============================================
l2 = [1, 2, 3]
s = " ram"

print(f"\n🔸 String '{s}' has {len(s)} characters")
for i in s:
    print(f"  Character: '{i}'")

l2.extend(s)  # String is iterable - adds each CHAR
print(f"\n✅ After extend('{s}'): {l2}")
# [1, 2, 3, ' ', 'r', 'a', 'm']
# Each character becomes separate element!

# ============================================
# VISUAL COMPARISON
# ============================================
print("\n" + "=" * 50)
print("📊 APPEND vs EXTEND - VISUAL")
print("=" * 50)

base = [1, 2, 3]
print(f"Base list: {base}")

# Append
a = base.copy()
a.append([4, 5])
print(f"\nappend([4,5]) → {a}")  # [1,2,3,[4,5]]

# Extend
e = base.copy()
e.extend([4, 5])
print(f"extend([4,5]) → {e}")    # [1,2,3,4,5]