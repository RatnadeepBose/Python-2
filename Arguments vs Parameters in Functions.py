# ============================================
# ARGUMENTS vs PARAMETERS IN FUNCTIONS
# ============================================

# Parameters: name and hobby (variables in function definition)
def intro(name, hobby):
    print(f"Hi {name}")
    print(f"Your hobby is {hobby}")
    print("-" * 20)

# Arguments: values passed to function
print("🔹 CORRECT ORDER:")
intro("Ram", "walking")      # name="Ram", hobby="walking"

print("🔸 WRONG ORDER (positional args matter!):")
intro("walking", "ram")      # name="walking", hobby="ram" - makes no sense!

print("✅ FIXED: Using keyword arguments (order doesn't matter):")
intro(hobby="walking", name="Ram")  # Explicitly assign parameters

