# ============================================
# HANDLING BINARY FILES
# ============================================

# READ binary file
with open("image.png", "rb") as f:
    data = f.read()  # Read entire file

print(type(data))     # <class 'bytes'>
print(len(data))      # Size in bytes
print(data[:10])      # First 10 bytes

# WRITE binary file
with open("image_copy.png", "wb") as f:
    f.write(data)     # Copy image

# READ in chunks (for large files)
with open("image.png", "rb") as f:
    while chunk := f.read(1024):  # Read 1KB at a time
        print(f"Read {len(chunk)} bytes")