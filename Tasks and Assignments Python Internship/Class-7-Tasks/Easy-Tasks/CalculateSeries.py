# [*] Calculate the below series:
# 		1 + 3 + 5 + .... + N = ? [N given by user]
# 		2 * 4 * 6 * .... * N = ? [N given by user]

N = int(input("Enter the Nth number: "))
odd_sum = 0
even_multiplication = 1

for i in range(1, N+1):
    if i % 2 != 0:
        odd_sum += i
    else:
        print(i)
        even_multiplication *= i

print("Odd series sum:",odd_sum)
print("Even series multiplication:",even_multiplication)