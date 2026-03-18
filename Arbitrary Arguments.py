# ============================================
# ARBITRARY ARGUMENTS (*args)
# ============================================

def test(*args):
    print("Tuple of arguments:", args)
    print("Type:", type(args))  # <class 'tuple'>
    print("Elements squared:")
    for i in args:
        if isinstance(i, (int, float)):  # Only square numbers
            print(i * i, end=" ")
        else:
            print(f"'{i}' (not a number)", end=" ")
    print()  # New line at end

# Test with mixed arguments
test("raj", 69, 4, 54, 4, 54, 545, 4)