# Q. Write a program to print multiplication table for a given number using for as well as while loop

num = int(input("Enter Number: "))
print("Table of " + str(num) + " =")
while(num>0):
        for i in range(1,11):
                print(num, 'x', i, '=', num*i)
        break

# Output: Enter Number: 2
#         Table of 2 =
#         2 x 1 = 2
#         2 x 2 = 4
#         2 x 3 = 6
#         2 x 4 = 8
#         2 x 5 = 10
#         2 x 6 = 12
#         2 x 7 = 14
#         2 x 8 = 16
#         2 x 9 = 18
#         2 x 10 = 20
