# ============================================
# ITERATOR, ITERABLE & ITERATION
# ============================================

# Simple for loop
# i is the iterator (holds current value)
# range(1, 12) is the iterable (the sequence being looped through)
# Each loop run is an iteration

print("--- Basic for loop ---")
for i in range(1, 12):
    print(i)  # Output: 1 2 3 4 5 6 7 8 9 10 11

print("\n--- With explanation ---")
for i in range(1, 6):
    print(f"Iteration {i}: i = {i}")