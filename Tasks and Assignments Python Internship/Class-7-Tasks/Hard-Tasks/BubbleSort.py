# [*] Bubble Sort Algorithm:
#     Write a program to sort a list of numbers using the bubble sort algorithm with nested for loops.

my_list = [8, 5, 6, 2, 1, 3, 9, 7, 0, 4]
n = len(my_list)

# Traverse through all elements in the list
for i in range(n):
    for j in range(0, n-i-1):
        # Swap if the element found is greater than the next element
        if my_list[j] > my_list[j+1]:
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

print(my_list)