# ============================================
# ORD() & CHR() - Character Conversion
# ============================================

print("=" * 45)
print("🔤 ORD() - Character to ASCII/Unicode")
print("=" * 45)

# ord() - Returns the Unicode code point of a character
print(f"📝 ord('5') → {ord('5')}")        # 53 (ASCII value of '5')
print(f"📝 ord('a') → {ord('a')}")        # 97 (ASCII value of 'a')
print(f"📝 ord('A') → {ord('A')}")        # 65
print(f"📝 ord('!') → {ord('!')}")        # 33
print(f"📝 ord('😊') → {ord('😊')}")      # 128522 (emoji Unicode)

print("\n" + "=" * 45)
print("🎯 CHR() - Unicode/ASCII to Character")
print("=" * 45)

# chr() - Returns the character for the given Unicode code point
print(f"🎨 chr(53)      → {chr(53)}")          # '5'
print(f"🎨 chr(97)      → {chr(97)}")          # 'a'
print(f"🎨 chr(65)      → {chr(65)}")          # 'A'
print(f"🎨 chr(33)      → {chr(33)}")          # '!'
print(f"🎨 chr(128512)  → {chr(128512)}")      # 😀 (grinning face)

print("\n" + "=" * 45)
print("📊 ASCII RANGE TABLE")
print("=" * 45)

print("🔹 Digits (0-9):", [chr(i) for i in range(48, 58)])
print("🔹 Uppercase (A-Z):", [chr(i) for i in range(65, 91)])
print("🔹 Lowercase (a-z):", [chr(i) for i in range(97, 123)])

print("\n" + "=" * 45)
print("🎪 FUN WITH EMOJIS")
print("=" * 45)

# Range of smiley emojis
for code in range(128512, 128522):
    print(f"chr({code}) → {chr(code)}", end="  ")
print()