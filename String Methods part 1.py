#String Methods part 1
name= "rahul"
jhame= "MULLA"
shame= "Rahul Mulla"
print(name.capitalize())   # Rahul


print(name.upper())        # RAHUL
print(jhame.lower())        # mulla

print(name.title())        # Rahul
print(jhame.title())        # Mulla

print(name.swapcase())     # RAHUL
print(jhame.swapcase())     # mulla

print(name.find("r"))     # 0
print(jhame.find("M"))     # 0


print(name.count("a"))     # 1
print(jhame.count("L"))     # 2


print(name.index("r"))     # 0
print(jhame.index("M"))     # 0

print(name.replace("r", "R"))     # RahuL
print(jhame.replace("M", "m"))     # mULLA


print(shame.split())     # ['Rahul', 'Mulla']