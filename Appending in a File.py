# ============================================
# APPENDING TO A FILE - name.txt
# ============================================

# 1️⃣ FIRST, LET'S CREATE THE FILE WITH INITIAL CONTENT
with open("name.txt", "w") as f:
    f.write("Rahul\n")
    f.write("Priya\n")
    f.write("Amit\n")

print("✅ Initial file created with names")

# Show initial content
with open("name.txt", "r") as f:
    print("\n📋 INITIAL CONTENT:")
    print(f.read())

print("\n" + "="*50)

# 2️⃣ APPENDING NEW NAMES ('a' mode)
with open("name.txt", "a") as f:
    f.write("Rajesh\n")
    f.write("Sneha\n")
    f.write("Vikram\n")

print("✅ New names appended")

# Show updated content
with open("name.txt", "r") as f:
    print("\n📋 AFTER APPENDING:")
    print(f.read())

print("\n" + "="*50)

# 3️⃣ APPENDING MULTIPLE NAMES AT ONCE
new_names = ["Anjali\n", "Rohan\n", "Deepa\n"]

with open("name.txt", "a") as f:
    f.writelines(new_names)

print("✅ More names appended using writelines()")

# Show final content
with open("name.txt", "r") as f:
    print("\n📋 FINAL CONTENT:")
    print(f.read())

print("\n" + "="*50)

# 4️⃣ APPEND WITH USER INPUT
print("🔹 ADD A NEW NAME:")
new_name = input("Enter name to append: ")

with open("name.txt", "a") as f:
    f.write(new_name + "\n")

print(f"✅ '{new_name}' appended")

# Show updated content
with open("name.txt", "r") as f:
    print("\n📋 UPDATED CONTENT:")
    print(f.read())