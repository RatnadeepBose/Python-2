# ============================================
# BREAK, CONTINUE & PASS STATEMENTS
# ============================================

# 1. PASS - Does nothing (placeholder)
print("--- PASS ---")
for i in range(1, 6):
    pass  # Does nothing
print("Loop completed")

# 2. CONTINUE - Skips current iteration
print("\n--- CONTINUE ---")
for j in range(1, 6):
    if j == 3:
        continue  # Skip when j=3
    print(j)      # Prints: 1,2,4,5

# 3. BREAK - Exits loop completely
print("\n--- BREAK ---")
for k in range(1, 6):
    if k == 3:
        break     # Exit loop when k=3
    print(k)      # Prints: 1,2