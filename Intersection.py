# ============================================
# SET INTERSECTION - Common elements
# ============================================

python = {"Iron man", "Hulk", "harry potter"}
java = {"Iron man", "Rajesh Mafatwala", "shinchan"}

# Method 1: intersection()
print(python.intersection(java))  # {'Iron man'}
print(java.intersection(python))  # {'Iron man'}

# Method 2: & operator (shorter)
print(python & java)  # {'Iron man'}