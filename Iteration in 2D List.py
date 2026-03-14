# ============================================
# ITERATION IN 2D LIST
# ============================================

# Creating individual lists
l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9]
l3 = [10, 11, 12, 13]

# Creating a 2-D list (list of lists)
l = [l1, l2, l3]

print("📋 2D LIST:")
print(l)
print()

# ============================================
# METHOD 1: Nested Loops (Correct Way)
# ============================================
print("🔍 NESTED LOOP ITERATION:")
print("-" * 30)

for i in l:          # i = each row (list)
    print(f"Row: {i}")
    for j in i:      # j = each element in the row
        print(f"  Element: {j}")
    print()  # Blank line between rows