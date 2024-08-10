# [*] Multiplication Table:
#     	Write a program that prints the multiplication table of a number entered by the user using a for loop.

num = int(input("Enter a number whose multiplication table is to be derived: "))
print(f"The Multiplication table of {num} is below:")
for i in range(1, 11):
    print(f"{num} X {i} = {num*i}")