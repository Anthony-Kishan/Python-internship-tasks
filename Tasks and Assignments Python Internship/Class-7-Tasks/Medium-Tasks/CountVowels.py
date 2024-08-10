# [*] Count Vowels in a String:
#     	Write a program that counts the number of vowels in a string provided by the user using a for loop.

vowels = "aeiou"
user_string = input("Enter the word: ").lower()
vowel_counter = 0

for i in user_string:
    if i in vowels:
        vowel_counter += 1
print(f"The word {user_string} has {vowel_counter} vowels.")
