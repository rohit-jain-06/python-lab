# Q. Write a program to print the sum of first n natural numbers using while loop.

num = int(input("Enter positive Number: "))
sum = 0

while(num > 0):
    sum += num
    num -= 1
print("The sum is", sum)

# Output: Enter positive Number: 12
#         The sum is 78
