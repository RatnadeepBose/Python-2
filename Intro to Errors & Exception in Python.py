

# ============================================
# ERRORS & EXCEPTIONS IN PYTHON
# ============================================

# 1️⃣ SYNTAX ERROR - Code violates Python grammar
print("\n🔹 1. SYNTAX ERROR")
print("   ❌ Example: print('Hello'")  # Missing closing parenthesis
# print("Hello"  # Uncomment to see SyntaxError

# 2️⃣ NAME ERROR - Variable not defined
print("\n🔹 2. NAME ERROR")
try:
    print(x)  # x is not defined
except NameError as e:
    print(f"   ❌ {e}")

# 3️⃣ TYPE ERROR - Operation on wrong type
print("\n🔹 3. TYPE ERROR")
try:
    result = "5" + 3  # Can't add string and int
except TypeError as e:
    print(f"   ❌ {e}")

# 4️⃣ VALUE ERROR - Wrong value for type
print("\n🔹 4. VALUE ERROR")
try:
    num = int("abc")  # Can't convert "abc" to int
except ValueError as e:
    print(f"   ❌ {e}")

# 5️⃣ INDEX ERROR - List index out of range
print("\n🔹 5. INDEX ERROR")
try:
    lst = [1, 2, 3]
    print(lst[5])  # Index 5 doesn't exist
except IndexError as e:
    print(f"   ❌ {e}")

# 6️⃣ KEY ERROR - Dictionary key not found
print("\n🔹 6. KEY ERROR")
try:
    d = {"name": "Rahul", "age": 25}
    print(d["city"])  # Key 'city' doesn't exist
except KeyError as e:
    print(f"   ❌ Key '{e}' not found")

# 7️⃣ ATTRIBUTE ERROR - Object has no attribute
print("\n🔹 7. ATTRIBUTE ERROR")
try:
    num = 5
    num.append(10)  # int has no append method
except AttributeError as e:
    print(f"   ❌ {e}")

# 8️⃣ ZERO DIVISION ERROR - Divide by zero
print("\n🔹 8. ZERO DIVISION ERROR")
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"   ❌ {e}")

# 9️⃣ FILE NOT FOUND ERROR - File doesn't exist
print("\n🔹 9. FILE NOT FOUND ERROR")
try:
    with open("nonexistent.txt", "r") as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"   ❌ {e}")

# 🔟 IMPORT ERROR - Module not found
print("\n🔹 10. IMPORT ERROR")
try:
    import nonexistent_module
except ImportError as e:
    print(f"   ❌ {e}")

# 1️⃣1️⃣ INDENTATION ERROR - Wrong indentation
print("\n🔹 11. INDENTATION ERROR")
print("   ❌ Example:")
print("      def func():")
print("      print('Hello')  # Wrong indentation")

# 1️⃣2️⃣ EOF ERROR - End of file unexpectedly
print("\n🔹 12. EOF ERROR")
print("   ❌ Example: input() with no input")

# 1️⃣3️⃣ MEMORY ERROR - Out of memory
print("\n🔹 13. MEMORY ERROR")
try:
    huge_list = [1] * (10**10)  # Too big
except MemoryError as e:
    print(f"   ❌ {e}")

print("\n" + "="*60)
print("✅ USING TRY-EXCEPT TO HANDLE ERRORS")
print("="*60)

# General try-except block
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"Result: {result}")
except ValueError:
    print("❌ That's not a valid number!")
except ZeroDivisionError:
    print("❌ Cannot divide by zero!")
except Exception as e:
    print(f"❌ Something went wrong: {e}")
else:
    print("✅ No errors occurred!")
finally:
    print("👋 This always runs!")