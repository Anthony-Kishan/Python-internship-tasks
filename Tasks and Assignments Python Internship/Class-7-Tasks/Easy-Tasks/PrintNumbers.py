# [*] Print Numbers from user input range:
# 	    Write a for loop to print the numbers from the user's give range [Say 20 to 35]

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

for i in range(start, end):
    print(i)