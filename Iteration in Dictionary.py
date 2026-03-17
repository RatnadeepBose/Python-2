#Iteration in Dictionary

fruits = {"Apple": 120, "mango": 100, "pineapple": 50}

for i in fruits:
    print(i)

for i in fruits:
    print(i,fruits[i])
    

print()

# dict.items

for key, value in fruits.items():
   print(key,value)


   print(fruits.items)