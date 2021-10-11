# Q. Write a program to store seven fruits in a list entered by the user

list = []
print("Enter Seven Fruits Name: ")
for i in range(7):   
	list.append(input("Enter Fruits: "))
print(list)

# Output: Enter Seven Fruits Name: 
#         Enter Fruits: Mango
#         Enter Fruits: Banana
#         Enter Fruits: Papaya
#         Enter Fruits: Kiwi
#         Enter Fruits: Apple
#         Enter Fruits: Grapes
#         Enter Fruits: Cherry
#         ['Mango', 'Banana', 'Papaya', 'Kiwi', 'Apple', 'Grapes', 'Cherry']
