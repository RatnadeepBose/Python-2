# ============================================
# HETEROGENEOUS LISTS - Different Data Types
# ============================================

l = [2, "ram,", 1.3, True]

print(f"List: {l}")
print(f"Type of list: {type(l)}")  # <class 'list'>

print("\n📊 ELEMENTS WITH THEIR TYPES:")
print("-" * 35)
for item in l:
    print(f"Value: {item:<8} | Type: {type(item)}")