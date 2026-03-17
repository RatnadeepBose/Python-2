# ============================================
# CHALLENGE: Find Unique Words
# ============================================

sent = "my name is rajesh maffatwal and i am a good guy"

# Method 1: Your code (perfect!)
lst = sent.split()      # Split into words list
s = set(lst)            # Convert to set (removes duplicates)
print(len(s))           # Count unique words

# Method 2: One-liner
print(len(set(sent.split())))

# Method 3: See the unique words
unique_words = set(sent.split())
print(f"Unique words: {unique_words}")
print(f"Count: {len(unique_words)}")