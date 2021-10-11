# Q. Write a program to enter marks of 6 students and display them in sorted order

marks = []
print("Enter marks of 6 students: ")
for i in range(6):
    marks.append(input("Enter marks: "))

print("Unsorted list = ")
print(marks)

marks.sort()

print("sorted listss = ")
print(marks)


# Output: Enter marks of 6 students: 
#         Enter marks: 10
#         Enter marks: 89
#         Enter marks: 26
#         Enter marks: 45 
#         Enter marks: 35
#         Enter marks: 67
#         Unsorted list = 
#         ['10', '89', '26', '45', '35', '67']
#         sorted marks = 
#         ['10', '26', '35', '45', '67', '89']
