# [*] Sum of First N Natural Numbers:
#     	Write a program that takes an input n from the user and prints the sum of the first n natural numbers using a for loop.

n = int(input("Enter the ending number: "))
sum = 0
for i in range(n+1):
    sum += i

print(f"The sum of the first {n} natural numbers is equal to {sum}.")
