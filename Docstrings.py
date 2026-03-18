# ============================================
# DOCSTRINGS - Function Documentation
# ============================================

def greet():
    """this function greets good morning"""
    # body
    print("good morning")

# Call the function
greet()  # good morning

# View docstring in different ways:
print(greet.__doc__)        # Method 1: Using __doc__
# Output: this function greets good morning

help(greet)                 # Method 2: Using help()
# Output will show:
# Help on function greet in module __main__:
# 
# greet()
#     this function greets good morning

# In Jupyter/Interactive mode:
# greet?  # This works in IPython/Jupyter, not regular Python