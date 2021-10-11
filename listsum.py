# Q. Write a program to sum a list with 4 numbers.

number = []
print("Enter 4 numbers: ")
x=1
for i in range(4):
    number.append(int(input("Number " + str(x) + " =")))
    x=x+1

print("Sum of 4 numbers = ",sum(number))

# Output: Enter 4 numbers: 
#         Number 1 =200
#         Number 2 =100
#         Number 3 =300
#         Number 4 =400
#         Sum of 4 numbers =  1000
