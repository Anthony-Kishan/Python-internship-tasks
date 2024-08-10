# [*] Check for Palindrome:
#     Write a program to check if a string entered by the user is a palindrome using a for loop.

user_string = input("Enter a string: ").lower()
is_palindrome = False

for i in range(len(user_string) // 2):
    if user_string[i] == user_string[len(user_string) - i - 1]:
        is_palindrome = True

if is_palindrome:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")