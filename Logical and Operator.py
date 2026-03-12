# AND Operator - Both must be True
print(2 > 3 and 5 > 4)   # False (2>3 is False, 5>4 is True → False and True = False)
print(3 > 2 and 5 > 4)   # True  (3>2 is True, 5>4 is True → True and True = True)
print(2 > 3 and 4 > 5)   # False (False and False = False)
print(3 > 2 and 4 > 5)   # False (True and False = False)

# OR Operator - At least one must be True
print(2 > 3 or 5 > 4)    # True  (False or True = True)
print(2 > 3 or 4 > 5)    # False (False or False = False)
print(3 > 2 or 4 > 5)    # True  (True or False = True)

# NOT Operator - Reverses the result
print(not(3 > 2))        # False (not True = False)
print(not(2 > 3))        # True  (not False = True)