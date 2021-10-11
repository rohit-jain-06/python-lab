# Q. Write a program to calculate the factorial of the given number

num = int(input("Enter positive Number: "))
fact=1
while(num>0):
    fact=fact*num;
    num-=1

print("Factorial of number = ", fact)

# Output: Enter positive Number: 5
#         Factorial of number =  120
