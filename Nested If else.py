# NESTED IF-ELSE 
age = int(input("Enter your age: "))

if age >= 18:
    print("You can drive.")
    if age >= 65:
        print("You are a senior citizen. Drive carefully!")
    else:
        print("You are not a senior citizen.")
else:
    print("You are not old enough to drive.")
