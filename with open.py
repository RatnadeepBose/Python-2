# ============================================
# WITH OPEN - FILE HANDLING (Auto-close)
# ============================================

# 1️⃣ READING a file with 'with'
print("🔹 READING FILE:")
with open("name.txt", "r") as f:
    content = f.read()
    print(f"Content: {content}")
    print(f"Inside block - Closed? {f.closed}")  # False

# After block ends, file is auto-closed
print(f"Outside block - Closed? {f.closed}")  # True

print("\n" + "="*50)

# 2️⃣ WRITING to a file with 'with'
print("🔹 WRITING FILE:")
with open("name.txt", "w") as f:
    f.write("i am ram rahim")
    print(f"Write completed")
    print(f"Inside block - Closed? {f.closed}")  # False

# After block ends, file is auto-closed
print(f"Outside block - Closed? {f.closed}")  # True

print("\n" + "="*50)

# 3️⃣ VERIFY the write worked
print("🔹 VERIFYING CONTENT:")
with open("name.txt", "r") as f:
    new_content = f.read()
    print(f"New content: {new_content}")

print("\n" + "="*50)

# 4️⃣ APPENDING to a file
print("🔹 APPENDING TO FILE:")
with open("name.txt", "a") as f:
    f.write(" and i am learning Python")

with open("name.txt", "r") as f:
    print(f"After append: {f.read()}")