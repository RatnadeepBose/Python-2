# ============================================
# TRY & EXCEPT - Error Handling
# ============================================

# Example 1: Basic try-except
a = 5
b = 0

print("Example 1: Division by zero")
try:
    result = a / b
    print("Result:", result)
except:
    print("Cannot divide by zero!")

print("\n" + "="*40)

# Example 2: Multiple except blocks
print("Example 2: Multiple except blocks")
try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print("Result:", result)
except ValueError:
    print("Error: Please enter a valid number")
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
except Exception as e:
    print("Error:", e)

print("\n" + "="*40)

# Example 3: try-except-else
print("Example 3: try-except-else")
try:
    num = int(input("Enter a number: "))
    result = 100 / num
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Success! Result:", result)

print("\n" + "="*40)

# Example 4: try-except-finally
print("Example 4: try-except-finally")
try:
    file = open("test.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found")
finally:
    print("This always runs - cleaning up")
    try:
        file.close()
    except:
        pass