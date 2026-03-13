#String Slicing in Python
name = "Rahul"

# Basic slicing [start:end]
print(name[0:3])   # Rah  (index 0 to 2)
print(name[3:5])   # ul   (index 3 to 4)
print(name[1:4])   # ahu  (index 1 to 3)

# Shortcuts
print(name[:3])    # Rah  (same as [0:3])
print(name[2:])    # hul  (index 2 to end)
print(name[:])     # Rahul (whole string)

# Step
print(name[::2])   # Rhl  (every 2nd character)

# Reverse
print(name[::-1])  # luhaR (backwards)