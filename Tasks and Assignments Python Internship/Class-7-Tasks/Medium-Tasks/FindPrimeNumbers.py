# [*] Find Prime Numbers:
#     Write a program that prints all prime numbers between 1 and 100 using nested for loops.

for i in range(1, 101):
    if i == 1:
        continue
    for j in range(2, i):
        if i%j == 0:
            break
    else:
        print(i)
