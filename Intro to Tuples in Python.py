# Wrong way - this is still a list
planets = ["Mercury", "Venus", "Earth", "Mars"]
t = (planets)
print(type(t))  # <class 'list'>

# Right way - actual tuples
t1 = ("Mercury", "Venus", "Earth", "Mars")     # Tuple with ()
t2 = tuple(planets)                              # Tuple constructor
t3 = "Mercury", "Venus", "Earth", "Mars"         # Comma = tuple

print(type(t1))  # <class 'tuple'>
print(type(t2))  # <class 'tuple'>  
print(type(t3))  # <class 'tuple'>

# Single element tuple - comma is required!
single = ("Earth",)
print(type(single))  # <class 'tuple'>