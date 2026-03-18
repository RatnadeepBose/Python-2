# ============================================
# CHALLENGE: RETURN LIST WITH UNIQUE NUMBERS
# ============================================

lst = [1, 2, 3, 6, 5, 4, 7, 8, 9, 6, 5, 4, 1, 2, 3, 8, 7, 4, 5, 6, 8, 4]

def unique(li):
    new = []  # Initialize empty list
    for i in li:
        if i not in new:
            new.append(i)
    return new  # Return the result

# Call the function
result = unique(lst)

print(f"Original list: {lst}")
print(f"Original length: {len(lst)}")
print(f"\nUnique list: {result}")
print(f"Unique length: {len(result)}")