#String Formatting


name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Using f-strings for string formatting
print(f"Hello, {name}! You are {age} years old.")


name = input("Enter your name: ")
age = int(input("Enter your age: "))
# Using str.format() method for string formatting
print("Hello, {}! You are {} years old.".format(name, age))


name = input("Enter your name: ")
age = int(input("Enter your age: "))
# Using % operator for string formatting 
print("Hello, %s! You are %d years old." % (name, age))