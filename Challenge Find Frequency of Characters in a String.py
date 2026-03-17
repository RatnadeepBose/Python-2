#Challenge: Find Frequency of Characters in a String


# ============================================
# LETTER FREQUENCY COUNTER
# ============================================
text = input()

freq = {}
for char in text:
    if char != ' ':  # Remove this line if you want to count spaces too
        freq[char] = freq.get(char, 0) + 1

for letter, count in freq.items():
    print(f'"{letter}": {count}')