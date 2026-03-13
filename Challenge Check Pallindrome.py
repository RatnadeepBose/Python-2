#Challenge: Check Pallindrome

s = input("Enter a string to check if it's a palindrome: ")
if s == s[::-1]:
    print(f"'{s}' is a palindrome!")
else:
    print(f"'{s}' is not a palindrome.")