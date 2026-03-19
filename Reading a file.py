# ============================================
# READING A FILE - seek() and tell()
# ============================================

# First, let's create a sample file to read
with open("name.txt", "w") as f:
    f.write("dipak kalal is learning python programming")

print("🔹 FILE CONTENT: 'dipak kalal is learning python programming'\n")

# Now read it with position tracking
with open("name.txt", "r") as f:
    
    # Read first 3 characters
    data = f.read(3)
    print(f"read(3) → '{data}'")
    
    # Read next 9 characters
    data = f.read(9)
    print(f"read(9) → '{data}'")
    
    # Check current position
    pos = f.tell()
    print(f"Current position: {pos}")
    
    # Move to position 2
    f.seek(2)
    print(f"After seek(2), position: {f.tell()}")
    
    # Read from new position
    data = f.read(5)
    print(f"Read from position 2: '{data}'")
    
    # Go back to start
    f.seek(0)
    print(f"After seek(0), position: {f.tell()}")
    
    # Read all
    print(f"Full file: '{f.read()}'")