# ============================================
# FILE OPERATIONS IN PYTHON - ALL MODES
# ============================================

# 1️⃣ READ MODE ('r') - Default
print("🔹 READ MODE ('r')")
f = open("edit.txt", "r")  # Open for reading
content = f.read()          # Read entire file
print(f"Content: {content}")
f.close()                   # Always close!

# 2️⃣ WRITE MODE ('w') - Overwrites file!
print("\n🔹 WRITE MODE ('w')")
f = open("edit.txt", "w")  # Opens for writing (CREATES NEW/OVERWRITES)
f.write("Hello World!")     # Write text to file
f.close()                   # Close to save

# Verify write worked
f = open("edit.txt", "r")
print(f"After write: {f.read()}")
f.close()

# 3️⃣ APPEND MODE ('a') - Adds to end
print("\n🔹 APPEND MODE ('a')")
f = open("edit.txt", "a")  # Opens for appending
f.write(" Adding more text!")  # Adds to end
f.close()

# Verify append worked
f = open("edit.txt", "r")
print(f"After append: {f.read()}")
f.close()

# 4️⃣ READ & WRITE MODE ('r+') - Can read and write
print("\n🔹 READ+WRITE MODE ('r+')")
f = open("edit.txt", "r+")  # Opens for reading AND writing
content = f.read()
print(f"Current: {content}")
f.write(" ADDED WITH r+")    # Writes at current position
f.close()

# 5️⃣ WRITE & READ MODE ('w+') - Overwrites then read
print("\n🔹 WRITE+READ MODE ('w+')")
f = open("edit.txt", "w+")  # Overwrites file, then can read
f.write("Brand new content!")
f.seek(0)                    # Move cursor to beginning
print(f"New content: {f.read()}")
f.close()

# 6️⃣ APPEND & READ MODE ('a+') - Append then read
print("\n🔹 APPEND+READ MODE ('a+')")
f = open("edit.txt", "a+")  # Append and read
f.write(" Appended at end!")
f.seek(0)                    # Move to beginning to read
print(f"After append: {f.read()}")
f.close()

# ✅ BEST PRACTICE: Using 'with' (auto-closes)
print("\n🔹 USING 'with' STATEMENT (Recommended)")
with open("edit.txt", "r") as f:
    print(f.read())  # File auto-closed after this block