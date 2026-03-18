# ============================================
# KEYWORD ARGUMENTS (**kwargs)
# ============================================

# Basic **kwargs
def intro(**kwargs):
    print(kwargs)  # {'name': 'rahul', 'age': 65, 'hobbies': 'cycling'}
    for k, v in kwargs.items():
        print(f"{k}:{v}")

intro(name="rahul", age=65, hobbies="cycling")

# Mixed arguments (correct order)
def mix(a, b, c, age=54, *args, **kwargs):
    print(a, b, c)          # 25 54 98
    print(age)               # 54
    print(args)              # ()
    print(kwargs)            # {'name': 'rahul', 'hobbies': 'cricket'}

mix(25, 54, 98, name="rahul", hobbies="cricket")


