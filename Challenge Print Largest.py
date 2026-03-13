#Challenge: Print Largest

marks=[85, 92, 78, 90, 88]
highest_mark = marks[0]
for i in marks:

    if i > highest_mark:
        highest_mark = i
print("The highest mark is:", highest_mark)