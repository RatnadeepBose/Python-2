# ============================================
# 2-D LISTS - Lists inside a list
# ============================================

# Creating individual lists
l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9]
l3 = [10, 11, 12, 13]

# Creating a 2-D list (list of lists)
l = [l1, l2, l3]

print("📋 2-D LIST:")
print(l)
# Output: [[1, 2, 3, 4, 5], [6, 7, 8, 9], [10, 11, 12, 13]]

# ============================================
# ACCESSING ELEMENTS
# ============================================
print("\n🔍 ACCESSING ELEMENTS:")
print("-" * 30)

# Access entire first row
print(f"l[0] → {l[0]}")        # [1, 2, 3, 4, 5]

# Access specific element: l[row][column]
print(f"l[2][0] → {l[2][0]}")  # 10 (3rd row, 1st column)

# More examples
print(f"l[0][2] → {l[0][2]}")  # 3 (1st row, 3rd column)
print(f"l[1][3] → {l[1][3]}")  # 9 (2nd row, 4th column)