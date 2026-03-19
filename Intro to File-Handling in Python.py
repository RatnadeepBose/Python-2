#Intro to File-Handling in Python


f = open("name.txt")  # Opens file in read mode (default)

print(f"File object: {f}")
print(f"File name: {f.name}")
print(f"File mode: {f.mode}")
print(f"Is closed? {f.closed}")  # False

# Read and display content
content = f.read()
print(f"\nFile content:\n{content}")

# ALWAYS close the file
f.close()
print(f"Is closed? {f.closed}")  # True

print("\n" + "="*50)

# ✅ BETTER WAY - Using 'with' (auto-closes)
print("Using 'with' statement (recommended):")
with open("name.txt", "r") as f:
    for line in f:
        print(f"  {line}", end="")
# File auto-closed here

print(f"\nFile closed? {f.closed}")  # True
