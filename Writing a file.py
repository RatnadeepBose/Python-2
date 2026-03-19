# ============================================
# WRITING, CREATING, AND EDITING FILES
# ============================================

# 1️⃣ CREATING + WRITING a new file ('w' mode)
print("🔹 CREATING AND WRITING A NEW FILE")
with open("new_file.txt", "w") as f:
    f.write("This is a new file!\n")
    f.write("I am learning file handling in Python.\n")
    f.write("This is line 3.")

print("✅ File 'new_file.txt' created and written")

# Verify
with open("new_file.txt", "r") as f:
    print(f.read())

print("\n" + "="*50)

# 2️⃣ APPENDING to existing file ('a' mode)
print("🔹 APPENDING TO EXISTING FILE")
with open("new_file.txt", "a") as f:
    f.write("\nThis line is appended.")
    f.write("\nAdding more content!")

print("✅ Content appended")

# Verify
with open("new_file.txt", "r") as f:
    print(f.read())

print("\n" + "="*50)

# 3️⃣ EDITING - Reading and writing together ('r+' mode)
print("🔹 EDITING FILE (replace text)")
with open("new_file.txt", "r+") as f:
    content = f.read()
    print(f"Original:\n{content}")
    
    # Move cursor to beginning to overwrite
    f.seek(0)
    f.write("--- EDITED VERSION ---\n")
    f.write(content.replace("Python", "PYTHON"))

print("✅ File edited")

# Verify
with open("new_file.txt", "r") as f:
    print(f"\nAfter edit:\n{f.read()}")

print("\n" + "="*50)

# 4️⃣ CREATING FILE ONLY IF IT DOESN'T EXIST ('x' mode)
print("🔹 CREATING FILE (only if doesn't exist)")
try:
    with open("brand_new.txt", "x") as f:
        f.write("This file is brand new!")
    print("✅ New file created")
except FileExistsError:
    print("❌ File already exists!")

print("\n" + "="*50)

# 5️⃣ WRITING MULTIPLE LINES with writelines()
print("🔹 WRITING MULTIPLE LINES")
lines = ["Line 1\n", "Line 2\n", "Line 3\n", "Line 4\n"]

with open("multi_lines.txt", "w") as f:
    f.writelines(lines)

print("✅ Multiple lines written")

# Verify
with open("multi_lines.txt", "r") as f:
    print(f.read())